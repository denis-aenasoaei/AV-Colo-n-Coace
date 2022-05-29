
const { exec } = require("child_process");
const path = require('path');


function _conversion_16hz(id) {

    var conda_exec = "%homedrive%%homepath%\\miniconda3\\Scripts\\conda.exe"
    var env_name = "deepspeech3"
    var sub_cmd = "python ..\\speech-to-text\\sample-rate-convertor.py .\\audio\\audio.wav"

    var command = [conda_exec, 'run', '-n', env_name, sub_cmd].join(" ")

    exec(`( ${command} )`, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(id, `stdout: ${stdout}`);
    });

}


/** 
 * înregistrarea webrtc folosește 48000 hz (binaryServer cu 16000 înregistreaza sunet cu pb @see app.js) 
 * Întăi se face conversia la 16000 rata de eșantionare altfel modelul va arunca eroare 
 */
async function speechToText(id) {
    _conversion_16hz(id);

    setTimeout(() => {
        var conda_exec = "%homedrive%%homepath%\\miniconda3\\Scripts\\conda.exe"
        var env_name = "deepspeech3"
        var sub_cmd = "deepspeech --model ..\\speech-to-text\\deepspeech-0.9.3-models.pbmm --scorer ..\\speech-to-text\\deepspeech-0.9.3-models.scorer --audio .\\audio\\audio-16hz.wav  > .\\audio\\coloncoace-output.txt"

        var command = [conda_exec, 'run', '-n', env_name, sub_cmd].join(" ")

        exec(`( ${command} )`, (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`);
                return;
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
                return;
            }
            console.log(id, `stdout: ${stdout}`);
        });

    }, 2000)


}

module.exports = {
    speechToText
}