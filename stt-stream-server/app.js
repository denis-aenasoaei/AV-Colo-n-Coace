var express = require('express');
var BinaryServer = require('binaryjs').BinaryServer;
var fs = require('fs');
var wav = require('wav');
const path = require('path');
var cors = require('cors')

var { speechToText } = require('./deepspeechCaller');

var port = 3700;
var outFile = path.join(__dirname, './audio/audio.wav');
var app = express();

app.use(cors())
app.use('/public', express.static(__dirname + '/public'))

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, '/index.html'));
});


app.post('/speech/to/text', function (req, res) {
  speechToText();

  setTimeout(() => {
    res.send("triggered deepspeech - results ready")
  }, 2000)

});

app.get('/results', function (req, res) {
  setTimeout(() => {
    const filePath = path.resolve(__dirname, './audio/coloncoace-output.txt')
    console.log('\x1b[36m%s\x1b[0m', filePath);
    const data = fs.readFileSync(filePath, 'utf8');
    console.log('\x1b[36m%s\x1b[0m', data);
    res.send(data)
  }, 1000)

});

app.listen(port);

console.log('server open on port ' + port);

binaryServer = BinaryServer({ port: 9101 });

binaryServer.on('connection', function (client) {
  console.log('new connection');

  var fileWriter = new wav.FileWriter(outFile, {
    channels: 1,
    sampleRate: 48000,
    bitDepth: 16
  });

  client.on('stream', function (stream, meta) {
    console.log('new stream');
    stream.pipe(fileWriter);

    stream.on('end', function () {
      fileWriter.end();
      console.log('wrote to file ' + outFile);
    });
  });
});
