import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize the speech recognition engine
r = sr.Recognizer()

# Set the default voice for text-to-speech synthesis
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change the index to use a different voice if needed


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning!")

    elif 12 <= hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("How can I assist you?")


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return ""
    return query


def search_web(query):
    speak(f"Searching for {query} on the web...")
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)


def execute_command(command):
    if "hello" in command:
        speak("Hello there!")

    elif 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak('According to Wikipedia')
        print(results)
        speak(results)
        
    elif "search" in command:
        search_query = command.split("search")[-1].strip()
        search_web(search_query)

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'play music' in command:
        # Add code to play music from a local directory or a streaming service (e.g., Spotify)
        webbrowser.open("spotify.com")

    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")

    elif 'date' in command:
        now = datetime.datetime.now().strftime("%D-%m-%Y")
        speak(f"The date is {now}")

    elif 'exit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm sorry, I couldn't understand your command.")


if __name__ == "__main__":
    greet()
    while True:
        command = listen().lower()
        if command:
            execute_command(command)