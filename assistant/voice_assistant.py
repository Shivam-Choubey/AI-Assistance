import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine once
engine = pyttsx3.init()

def recognize_speech():
    r = sr.Recognizer()

    # Using the microphone for speech input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        print("Listening...")
        audio = r.listen(source)

        try:
            # Recognize speech using Google's speech recognition
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError as e:
            return f"Could not request results; check your internet connection. {e}"

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    while True:
        print("Say something:")
        spoken_text = recognize_speech()
        print(f"You said: {spoken_text}")
        
        # Speak the recognized text
        speak_text(spoken_text)
        
        # Exit on a specific command (optional)
        if "exit" in spoken_text.lower():
            print("Exiting...")
            break
