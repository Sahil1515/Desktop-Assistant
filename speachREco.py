

# sudo apt-get install python3-pyaudio
# sudo apt-get install portaudio19-dev python-pyaudio
# pip3 install PyAudio

# Bhoom...


# https://pypi.org/project/SpeechRecognition/1.2.3/


import speech_recognition as sr
import pyaudio

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything:\n")
    audio=r.listen(source,timeout=300)
    print("Hi")

    try:
        text=r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("Sorry, Could'nt recognize your voice ")