from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


def talkrobot(words):
    # to text-to-audio with gTTS
    fp = BytesIO()
    tts = gTTS(words, lang='zh-CN')
    tts.write_to_fp(fp)
    fp.seek(0)
    # use pydub play the flow
    song = AudioSegment.from_file(fp, format="mp3")
    play(song)


def main():
    while True:
        words = input()
        if words == 'stop':
            break
        talkrobot(words)


if __name__ == '__main__':
    main()