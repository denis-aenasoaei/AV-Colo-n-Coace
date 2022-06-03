# Integration API

1. install nodejs `(> v16.x.x) (ex: v16.15.0)`
2. go to api folder `cd AV-Colo-n-Coace/stt-stream-server/`
3. install dependencies `npm install`
4. To start run: `node app.js`

------------

## Stream server

It will starts a streaming server to accept WebRTC connection from browser. 
Binary server : `http://localhost:9101` 
The websocket listens to connection, stream and end  events. Once the stream ends it will save the stream on disk as audio file: `/stt-stream-server/audio/audio.wav`

## Nodejs express REST API

through which backend modules (deepspeech, bot.py, nodejs) are called from frontend
 - `/text/to/speech`
    This endpoind looks in stt-stream-server/audio/ and checks if there is an audio.wav and if it finds it will convert the file to a 16000 Hz SampleRate Then calls deepspeach 
 - `/bot` 
Exposes the bot.py script. The input of the script is taken from the deepspeech output /stt-stream-server/audio/coloncoace-output.txt 
 - `/results`
Reads the results from /bot and text-to-speech and brings to front end for display

    


