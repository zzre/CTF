+#define CTF_MENU "/id\n/send <id> <message>\n/list\n/delete <idx>\n"
 #define SUB_OVERLAP 300
+#define MAX_MAIL 16
+#define MAX_RESPONSE 512
+#define MAX_MAIL_LEN 512
+
+struct mailbox {
+	switch_memory_pool_t *pool;
+	char **mail;
+};
+
+typedef struct mailbox mailbox_t;
+
 struct state_helper {
 	switch_hash_t *hash;
 	sofia_profile_t *profile;
@@ -98,10 +111,196 @@ struct presence_helper {
 
 };
 
+/* /send <id> <message> */
+char *mailbox_handle_send(sofia_profile_t *profile, const char *id, char *msg, int msg_len)
+{
+	switch_hash_t *mailbox_hash = profile->mailbox_hash;
+	switch_memory_pool_t *pool = NULL;
+	mailbox_t *mailbox = NULL;
+	char *response = (char *)calloc(32, 1);
+	switch_mutex_lock(profile->flag_mutex);
+	mailbox = (mailbox_t *)switch_core_hash_find(mailbox_hash, id);
+
+	if (mailbox == NULL) {
+		switch_core_new_memory_pool(&pool);
+		mailbox = (mailbox_t *)switch_core_alloc(pool, sizeof(mailbox_t));
+		mailbox->pool = pool;
+		mailbox->mail = (char **)switch_core_alloc(pool, MAX_MAIL * sizeof(char *));
+		switch_core_hash_insert(mailbox_hash, id, mailbox);
+	}
+	else {
+		pool = mailbox->pool;
+	}
+
+	for (int i = 0; i < MAX_MAIL; i++) {
+		if (mailbox->mail[i] == NULL)
+		{
+			mailbox->mail[i] = (char *)switch_core_alloc(pool, MAX_MAIL_LEN);
+			if (msg != NULL) strncpy(mailbox->mail[i], msg, msg_len);
+			switch_snprintf(response, 32, "sent: %d", i);
+			goto end;
+		}
+	}
+	strcpy(response, "mailbox full");
+end:
+	switch_mutex_unlock(profile->flag_mutex);
+	return response;
+}
+
+/* /list */
+char *mailbox_handle_list(sofia_profile_t *profile, const char *id)
+{
+	switch_hash_t *mailbox_hash = profile->mailbox_hash;
+	mailbox_t *mailbox = NULL;
+	char *response = (char *)calloc(MAX_MAIL,  MAX_RESPONSE);
+	char tmp[MAX_RESPONSE] = {0,};
+
+	switch_mutex_lock(profile->flag_mutex);
+	mailbox = (mailbox_t *)switch_core_hash_find(mailbox_hash, id);
+
+	if (mailbox == NULL) {
+		strcpy(response, "no mailbox");
+		goto end;
+	}
+
+	for (int i = 0; i < MAX_MAIL; i++) {
+		if (mailbox->mail[i] != NULL) {
+			switch_snprintf(tmp, MAX_RESPONSE, "%d: %s\n", i, mailbox->mail[i]);
+			strcpy(response + strlen(response), tmp);
+		}
+	}
+end:
+	switch_mutex_unlock(profile->flag_mutex);
+	return response;
+}
+
+/* /delete <idx> */
+char *mailbox_handle_delete(sofia_profile_t *profile, const char *id, int idx)
+{
+	switch_hash_t *mailbox_hash = profile->mailbox_hash;
+	switch_memory_pool_t *pool = NULL;
+	mailbox_t *mailbox;
+	char *response = (char *)calloc(32, 1);
+	switch_bool_t is_all_deleted = SWITCH_TRUE;
+
+
+	switch_mutex_lock(profile->flag_mutex);
+	if (idx >= MAX_MAIL && idx < 0)
+	{
+		strcpy(response, "invalid index");
+		goto end;
+	}
+
+	mailbox = (mailbox_t *)switch_core_hash_find(mailbox_hash, id);
+
+	if (mailbox == NULL) {
+		strcpy(response, "no mailbox");
+		goto end;
+	}
+	else {
+		pool = mailbox->pool;
+	}
+
+	if (mailbox->mail[idx] != NULL) {
+		bzero(mailbox->mail[idx], MAX_MAIL_LEN);
+		strcpy(response, "deleted");
+	}
+
+	for (int i=0; i<MAX_MAIL; i++) {
+		if (mailbox->mail[idx] != NULL) is_all_deleted = SWITCH_FALSE;
+	}
+
+	if (is_all_deleted != SWITCH_TRUE) {
+		switch_core_destroy_memory_pool(&pool);
+		switch_core_hash_delete(mailbox_hash, id);
+	}
+
+end:
+	switch_mutex_unlock(profile->flag_mutex);
+	return response;
+}
+
+/* /edit <idx> <msg> */
+char *mailbox_handle_edit(sofia_profile_t *profile, const char *id, int idx, char *msg, int msg_len)
+{
+	switch_hash_t *mailbox_hash = profile->mailbox_hash;
+	mailbox_t *mailbox;
+	char *response = (char *)calloc(32, 1);
+
+	switch_mutex_lock(profile->flag_mutex);
+	mailbox = (mailbox_t *)switch_core_hash_find(mailbox_hash, id);
+
+	if (mailbox == NULL) {
+		strcpy(response, "no mailbox");
+		goto end;
+	}
+
+	if (mailbox->mail[idx] != NULL) {
+		strncpy(mailbox->mail[idx], msg, msg_len);
+		strcpy(response, "edited");
+	}
+end:
+	switch_mutex_unlock(profile->flag_mutex);
+	return response;
+}
+
+char *mailbox_handle_body(sofia_profile_t *profile, const char* user, const char *body, int body_len)
+{
+	char *tmp = (char *)body;
+	char *id;
+	char *msg;
+	int msg_len;
+	char *str_idx;
+	int idx;
+
+	if (tmp[0] == '/') {
+		tmp++;
+		if (strncmp(tmp, "send", 4) == 0) {
+			strtok(tmp, " ");
+			id = strtok(NULL, " ");
+			msg = strtok(NULL, " ");
+			msg_len = body_len - 5 - strlen(id) - 2;
+			if (id == NULL) {
+				return 0;
+			}
+			return mailbox_handle_send(profile, id, msg, msg_len);
+		}
+		else if(strncmp(tmp, "list", 4) == 0) {
+			return mailbox_handle_list(profile, user);
+		}
+		else if(strncmp(tmp, "delete", 6) == 0) {
+			strtok(tmp, " ");
+			str_idx = strtok(NULL, " ");
+			if (strlen(str_idx) > 2) {
+				return 0;
+			}
+			idx = atoi(str_idx);
+			return mailbox_handle_delete(profile, user, idx);
+		}
+		else if(strncmp(tmp, "edit", 4) == 0) {
+			strtok(tmp, " ");
+			str_idx = strtok(NULL, " ");
+			if (strlen(str_idx) > 2) {
+				return 0;
+			}
+			idx = atoi(str_idx);
+			msg = strtok(NULL, " ");
+			msg_len = body_len - 5 - strlen(str_idx) - 2;
+			if (msg == NULL)
+			{
+				return 0;
+			}
+			return mailbox_handle_edit(profile, user, idx, msg, msg_len);
+		}
+	}
+	return 0;
+}
+
 switch_status_t sofia_presence_chat_send(switch_event_t *message_event)
 
 {
 	char *prof = NULL, *user = NULL, *host = NULL;
+	char *from_user = NULL, *from_host = NULL;
 	sofia_profile_t *profile = NULL;
 	char *ffrom = NULL;
 	nua_handle_t *msg_nh;
@@ -110,6 +309,7 @@ switch_status_t sofia_presence_chat_send(switch_event_t *message_event)
 	switch_status_t status = SWITCH_STATUS_FALSE;
 	const char *ct = "text/html";
 	sofia_destination_t *dst = NULL;
+	sofia_destination_t *me_dst = NULL;
 	char *to_uri = NULL;
 	switch_console_callback_match_t *list = NULL;
 	switch_console_callback_match_node_t *m;
@@ -125,6 +325,7 @@ switch_status_t sofia_presence_chat_send(switch_event_t *message_event)
 	//const char *subject;
 	const char *body;
 	const char *type;
+	const char *content_len_str;
 	const char *from_full;
 	char header[256] = "";
 	char *route_uri = NULL;
@@ -142,6 +343,7 @@ switch_status_t sofia_presence_chat_send(switch_event_t *message_event)
 	//subject = switch_event_get_header(message_event, "subject");
 	body = switch_event_get_body(message_event);
 	type = switch_event_get_header(message_event, "type");
+	content_len_str = switch_event_get_header(message_event, "length");
 	from_full = switch_event_get_header(message_event, "from_full");
 	blocking = switch_event_get_header(message_event, "blocking");
 	is_blocking = switch_true(blocking);
@@ -196,6 +398,49 @@ switch_status_t sofia_presence_chat_send(switch_event_t *message_event)
 		}
 	}
 
+	if (strcmp(user, "mailbox") == 0) {
+		char me[1024] = "";
+		char *payload;
+		dup = strdup(from);
+		if ((from_host = strchr(dup, '@'))) {
+			*from_host++ = '\0';
+		}
+		from_user = dup;
+		profile = sofia_glue_find_profile("internal"); // sip_profiles/internal.xml
+		sofia_reg_find_reg_url(profile, from_user, from_host, me, sizeof(me));
+		me_dst = sofia_glue_get_destination(me);
+		switch_uuid_str(uuid_str, sizeof(uuid_str));
+
+		msg_nh = nua_handle(profile->nua, NULL,
+							TAG_END());
+
+		nua_handle_bind(msg_nh, &mod_sofia_globals.destroy_private);
+
+		payload = mailbox_handle_body(profile, from_user, body, atoi(content_len_str));
+		if (payload == 0) {
+			nua_message(msg_nh,
+			SIPTAG_FROM_STR(from_full),
+			SIPTAG_TO_STR(me_dst->to),
+			SIPTAG_CALL_ID_STR(uuid_str),
+			SIPTAG_CONTENT_TYPE_STR("text/plain"),
+			SIPTAG_PAYLOAD_STR(CTF_MENU),
+			TAG_END());
+		}
+		else {
+			nua_message(msg_nh,
+			SIPTAG_FROM_STR(from_full),
+			SIPTAG_TO_STR(me_dst->to),
+			SIPTAG_CALL_ID_STR(uuid_str),
+			SIPTAG_CONTENT_TYPE_STR("text/plain"),
+			SIPTAG_PAYLOAD_STR(payload),
+			TAG_END());
+		}
+
+		sofia_glue_free_destination(me_dst);
+
+		goto end;
+	}
+