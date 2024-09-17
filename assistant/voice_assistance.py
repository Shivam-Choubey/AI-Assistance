import speech_recognition as sr
import pyttsx3

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
