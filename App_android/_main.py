from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

if platform == 'android':
    from plyer import tts
    from jnius import autoclass

    # For speech recognition on Android
    SpeechRecognizer = autoclass('android.speech.SpeechRecognizer')
    Intent = autoclass('android.content.Intent')
    RecognizerIntent = autoclass('android.speech.RecognizerIntent')
else:
    import speech_recognition as sr 

class AssistantApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform == 'android':
            self.sr = SpeechRecognizer.createSpeechRecognizer(autoclass('android.app.Activity').mActivity)
        else:
            self.recognizer = sr.Recognizer()

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Speak to Assistant')
        self.button.bind(on_press=self.on_button_press)
        layout.add_widget(self.button)
        return layout

    def on_button_press(self, instance):
        if platform == 'android':
            self.recognize_speech()
        else:
            self.recognize_speech_desktop()

    def recognize_speech(self):
        intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
        intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1)
        self.sr.startListening(intent)

    def recognize_speech_desktop(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            response = self.process_command(text)
            if platform == 'android':
                tts.speak(response)
            else:
                print(response)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

    def process_command(self, command):
        if "hello" in command.lower():
            return "Hello! How can I help you?"
        else:
            return "I'm sorry, I didn't understand that command."

if __name__ == '__main__':
    AssistantApp().run()