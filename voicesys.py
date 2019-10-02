from gtts import gTTs
import speech_recognition as sr
from pygame import mixer

from gtts import gTTS
import speech_recognition as sr
from pygame import mixer

def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()


def myCommand():
    #Initialize the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('TARS is Ready...')
        r.pause_threshold = 1
        #wait for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        #listens for the user's input
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

