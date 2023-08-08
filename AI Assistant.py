def main():
    import pyttsx3
    import datetime
    import pywhatkit as kit
    from AppOpener import run
    import time
    import requests
    import subprocess
    import smtplib
    import wikipedia
    import googlesearch
    import googlesearch
    from googlesearch import search

    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 2.0)
    engine.runAndWait()

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    speak("Hello I am Gokul, an AI-powered virtual assistant. To get started, please type your name:")
    user = input("Type your name: ")

    def greet_user():
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak(f"Good morning, {user}")
        elif hour >= 12 and hour < 17:
            speak(f"Good afternoon, {user}")
        else:
            speak(f"Good evening, {user}")

    greet_user()

    def robot():
        if __name__ == "__main__":
            if True:
                speak(f"How can I assist you, {user}")
                query = input("How can I assist you :  ").lower()

                if "notepad" in query:
                    try:
                        speak("Opening Notepad")
                        subprocess.Popen("notepad")
                    except:
                        speak("Unknown error occurred")

                elif "spotify" in query:
                    try:
                        speak("Opening Spotify")
                        subprocess.Popen("Spotify")
                    except:
                        speak("Unknown error occurred")

                elif "word" in query:
                    try:
                        speak("opening word")
                        subprocess.Popen("word")
                    except:
                        speak("Unknown error occurred")

                elif "whatsapp" in query:
                    try:
                        speak("opening whatsapp")
                        run("WhatsApp")
                    except:
                        subprocess.Popen("Unknown error occurred")

                elif "netflix" in query:
                    try:
                        speak("opening netflix")
                        subprocess.Popen("Netflix")
                    except:
                        speak("Unknown error occurred")


                elif "play on youtube" in query:
                    try:
                        speak("What do you want to play on YouTube?")
                        req = input("Enter your request: ")  # Use input() to get text input from the user
                        kit.playonyt(req)
                    except Exception as e:
                        speak("Unknown error occurred")
                        print(e)

                elif "date" in query:
                    try:
                        speak(datetime.date.today())
                    except:
                        speak("Unknown error occurred")

                elif "time" in query:
                    try:
                        speak(time.strftime("%H:%M:%S", time.localtime()))
                    except:
                        speak("Unknown error occurred")

                elif "file explorer" in query:
                    try:
                        speak("opening file explorer")
                        subprocess.Popen("file explorer")
                    except:
                        speak("Unknown error occurred")

                elif "calculater" in query:
                    try:
                        speak("opening calculater")
                        subprocess.Popen("calculator")
                    except:
                        speak("Unknown error occurred")

                elif "camera" in query:
                    try:
                        speak("opening camera")
                        subprocess.Popen("camera")
                    except:
                        speak("Unknown error occurred")

                elif "settings" in query:
                    try:
                        speak("opening settings")
                        subprocess.Popen("settings")
                    except:
                        speak("Unknown error occurred")

                elif "vlc" in query:
                    try:
                        speak("opening vlc")
                        subprocess.Popen("vlc media player")
                    except:
                        speak("Unknown error occurred")

                elif "chrome" in query:
                    try:
                        speak("opening chrome")
                        subprocess.Popen("google chrome")
                    except:
                        speak("Unknown error occurred")

                elif "message" in query:
                    try:
                        speak(
                            "Sure, please type the number with the country code to whom I have to message")
                        number = (input("Enter the Number here"))
                        speak("now enter the message you want to send")
                        msg = input("Enter the message here")
                        kit.sendwhatmsg_instantly(number, msg)
                    except:
                        speak("Unknown error occurred")

                elif "joke" in query:
                    try:
                        def joke():
                            headers = {'Accept': 'application/json'}
                            res = requests.get(
                                "https://icanhazdadjoke.com/", headers=headers).json()
                            return res["joke"]

                        jokee = joke()
                        speak(jokee)
                        print(jokee)
                    except:
                        speak("Unknown error occurred")

                elif "advice" in query:
                    try:
                        def advice():
                            res = requests.get(
                                "https://api.adviceslip.com/advice").json()
                            return res["slip"]["advice"]

                        advicee = advice()
                        speak(advicee)
                        print(advicee)
                    except:
                        speak("Unknown error occurred")

                elif " email" in query:
                    try:
                        senderEmailId = input("Please type your email address  ")
                        senderPassword = input("Please type the password  ")
                        receiver = input("Enter receivers email address  ")
                        li = [senderEmailId, receiver]
                        for des in li:
                            s = smtplib.SMTP('smtp.gmail.com', 587)
                            s.starttls()
                            s.login(senderEmailId, senderPassword)
                            message = "Message_you_need_to_send"
                            s.sendmail("sender_email_id", des, message)
                            s.quit()
                    except:
                        speak("Unknown error occurred")

                # ...

                else:
                    try:
                        speak("I found this on the web")
                        user_query = input("What would you like to search for on the web? ")

                        # Wikipedia Search
                        wikipedia_summary = wikipedia.summary(user_query, sentences=5)
                        print(wikipedia_summary)
                        speak(wikipedia_summary)

                        # Google Search
                        num_page = 3
                        search_results = googlesearch.search(user_query, num_page)
                        for result in search_results:
                            print(result.description)
                            speak(result.description)

                    except Exception as e:
                        speak("Unknown error occurred")
                        print(e)

                # ...

    robot()

    while True:
        speak("Would you like to run this tool again? (yes/no)")
        query = input().lower()

        if query in ["yes", "yep", "yup", "sure"]:
            speak(f"Very well. What else would you like me to do?, {user}")
            robot()
        elif query in ["no", "not now", "nope", "nah"]:
            speak(f"Cool. Thanks for using the program, {user}")
            print(f"Cool. Thanks for using the program.", user)
            hour = datetime.datetime.now().hour
            if 22 <= hour < 6:
                speak(f"Good night, {user}")
            else:
                speak(f"Have a good day, {user}")
                print(f"Have a good day, {user}")
            break
        else:
            speak(f"That may be beyond my abilities at the moment. I'm Sorry {user}")


main()