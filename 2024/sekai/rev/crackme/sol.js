const firebase = require('firebase/app');
const { getAuth, signInWithEmailAndPassword } = require('firebase/auth');
require('firebase/firestore');
const { getDatabase, ref, get } = require('firebase/database');

var c = {
    apiKey: 'AIzaSyCR2Al5_9U5j6UOhqu0HCDS0jhpYfa2Wgk',
    authDomain: 'crackme-1b52a.firebaseapp.com',
    projectId: 'crackme-1b52a',
    storageBucket: 'crackme-1b52a.appspot.com',
    messagingSenderId: '544041293350',
    appId: '1:544041293350:web:2abc55a6bb408e4ff838e7',
    measurementId: 'G-RDD86JV32R',
    databaseURL: 'https://crackme-1b52a-default-rtdb.firebaseio.com',
};

const app = firebase.initializeApp(c);
const auth = getAuth(app);
signInWithEmailAndPassword(auth, 'admin@sekai.team', 's3cr3t_SEKAI_P@ss').then((userCredential) => {
    const uid = userCredential.user.uid;
    
    const db = getDatabase(app);
    const dbRef = ref(db, 'users/' + uid + '/flag');

    
    get(dbRef).then((snapshot) => {
        if (snapshot.exists()) {
            console.log('data:', snapshot.val());
        } else {
            console.log('!');
        }
    });
})