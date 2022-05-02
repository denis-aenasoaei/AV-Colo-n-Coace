import ffmpeg
import argparse
import os


parser = argparse.ArgumentParser(description='Converteste fisier audio la sample rate 16000')
parser.add_argument('infile', help='Input filename (`-` for stdin)')

### 
def convert_audio(in_filename, **input_kwargs):
    try:
        out, err = (ffmpeg
            .input(in_filename, **input_kwargs)
            .output('ga.wav', format='wav', acodec='pcm_s16le', ac=1, ar='16k')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(1)
    return out




if __name__ == '__main__':
    args = parser.parse_args()
    print(args.infile)
    print(os.path.abspath("LJ001-0001.wav"))
    audio_data = convert_audio("LJ001-0001.wav")
    ## print(os.path.join(os.getcwd(), os.path.dirname("LJ001-0001.wav")))
    # audio_data = convert_audio(os.path.abspath("LJ001-0001.wav"))
    
    #stream = ffmpeg.input(os.path.abspath("LJ001-0001.wav"))
    #audio = stream.audio
    #stream = ffmpeg.output(audio, os.path.abspath("LJ001-00012.wav"), **{'ar': '16000','acodec':'flac'})