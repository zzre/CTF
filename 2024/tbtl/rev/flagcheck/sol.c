#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

int target[63] = { 51, 132, 61, 63, 42, 147, 123, 130, 26, 172, 142, 244, 177, 203, 141, 33, 14, 183, 103, 150, 44, 129, 211, 188, 41, 108, 75, 13, 0, 237, 253, 238, 86, 64, 82, 213, 5, 109, 144, 62, 122, 27, 105, 35, 31, 182, 29, 188, 152, 209, 166, 131, 233, 235, 19, 33, 61, 248, 43, 121, 83, 79, 161 };

void* search(void* arg) {
    unsigned long long thread_id = *(int*)arg;
    unsigned long long start = thread_id << 16;
    unsigned long long end = start + 0x1000000;

    for (unsigned long long i = start; i < end; i++) {
        char buf[64] = {0,};
        srand((unsigned int)i);
        for (int j=0; j<63; j++) {
            buf[j] = (char)((rand() % 256) ^ target[j]);
        }
        // if (buf[62] == '}') {
        if (strncmp(buf, "TBTL{", 5) == 0) {
            printf("flag : %s\n", buf);
            break;
        }
    }
    // printf("%d done!\n", thread_id);
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[0x100];
    int thread_args[0x100];

    for (int i = 0; i < 0x100; i++) {
        thread_args[i] = i;
        pthread_create(&threads[i], NULL, search, &thread_args[i]);
    }

    for (int i = 0; i < 0x100; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}