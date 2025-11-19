import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command
    except:
        return ""

def run_jarvis():
    command = listen()

    if "hello" in command:
        talk("Hello sir, how can I help you?")

    elif "your name" in command:
        talk("I am Jarvis, your AI assistant.")

    elif "time" in command:
        import datetime
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The time is " + time)

    elif "open youtube" in command:
        import webbrowser
        webbrowser.open("https://youtube.com")
        talk("Opening YouTube.")

    elif "stop" in command or "bye" in command:
        talk("Goodbye sir.")
        exit()

    else:
        talk("Sorry, I did not understand that.")

while True:
    run_jarvis()
