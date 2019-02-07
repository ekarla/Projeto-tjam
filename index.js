
const express = require('express');
const bodyParser = require('body-parser');
const Pusher = require('pusher');
const app = express();


// Body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
// Session middleware

// Create an instance of Pusher
const pusher = new Pusher({
    appId: '708425',
    key: '740d99c4c90bab3d1296',
    secret: '98c0e27730b576671de2',
    cluster: 'us2',
    encrypted: true
});


app.get('/', (req, res) => {
    return res.sendFile(__dirname + '/index.html');
});

// get authentictation for the channel;
app.post('/pusher/auth', (req, res) => {
        const socketId = req.body.socket_id;
        const channel = req.body.channel_name;
        var presenceData = {
            user_id: Math.random().toString(36).slice(2) + Date.now()
        }
        const auth = pusher.authenticate(socketId, channel, presenceData);
        res.send(auth);
});

//listen on the app
app.listen(3000, () => {
    return console.log('Server is up on 3000')
});
