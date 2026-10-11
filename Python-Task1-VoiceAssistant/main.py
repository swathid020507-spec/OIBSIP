import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice assistant
engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    
    with sr.Microphone() as source:
        print("\nListening... Speak now!")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I could not understand.")
        except sr.RequestError:
            speak("Speech recognition needs an internet connection.")

    return ""


def run_assistant():
    speak("Hello! I am your Python voice assistant.")
    speak("You can ask me the time, date, or open Google and YouTube.")
    speak("Say exit to stop.")

    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "search" in command:
            query = command.replace("search", "", 1).strip()
            if query:
                speak("Searching Google for " + query)
                webbrowser.open(
                    "https://www.google.com/search?q=" +
                    query.replace(" ", "+")
                )
            else:
                speak("Please say what you want to search for.")

        elif "exit" in command or "stop" in command or "goodbye" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I do not know that command yet.")


if __name__ == "__main__":
    try:
        run_assistant()
    except OSError:
        print("Microphone error. Please check your microphone connection.")
    except KeyboardInterrupt:
        print("\nVoice assistant stopped.")