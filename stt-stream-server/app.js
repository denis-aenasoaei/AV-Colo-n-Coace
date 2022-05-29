var express = require('express');
var BinaryServer = require('binaryjs').BinaryServer;
var fs = require('fs');
var wav = require('wav');
const path = require('path');
var cors = require('cors')

var port = 3700;
var outFile = 'demo.wav';
var app = express();

app.use(cors())
app.use('/public', express.static(__dirname + '/public'))

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, '/index.html'));
});

app.listen(port);

console.log('server open on port ' + port);

binaryServer = BinaryServer({ port: 9001 });

binaryServer.on('connection', function (client) {
  console.log('new connection');

  var fileWriter = new wav.FileWriter(outFile, {
    channels: 1,
    sampleRate: 16000,
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
