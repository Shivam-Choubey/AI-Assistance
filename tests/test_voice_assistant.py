import unittest
from unittest.mock import patch
from assistant.voice_assistant import recognize_speech, speak_text

class TestVoiceAssistant(unittest.TestCase):

    @patch('assistant.voice_assistant.sr.Recognizer.listen')
    @patch('assistant.voice_assistant.sr.Recognizer.recognize_google')
    def test_recognize_speech(self, mock_recognize_google, mock_listen):
        # Mock the Google speech recognition result
        mock_recognize_google.return_value = "Hello world"
        
        # Simulate voice recognition
        result = recognize_speech()
        self.assertEqual(result, "Hello world")
    
    @patch('assistant.voice_assistant.pyttsx3.Engine.say')
    @patch('assistant.voice_assistant.pyttsx3.Engine.runAndWait')
    def test_speak_text(self, mock_runAndWait, mock_say):
        # Mock the pyttsx3 output
        speak_text("Hello world")
        
        # Assert that pyttsx3 methods were called
        mock_say.assert_called_once_with("Hello world")
        mock_runAndWait.assert_called_once()

if __name__ == '__main__':
    unittest.main()
