import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary
import requests
from duckgpt import DuckGPT # Now this dose't work , use generative api  
import pyautogui
import time
import pyperclip

engine = pyttsx3.init()
newsapi = ""

def speak (text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
def ai (c):
    client = DuckGPT(model="gpt-4o-mini")
    models = client.Models()
    response = client.Chat(c, [])
    print(response)
    return response

def comandprocess (c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower() or "open insta" == c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in  c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        # print(song)
        link = musiclibrary.music[song]
        webbrowser.open(link)
        return False
    elif "news" in c.lower():
        print("searching....")
        speak("searching....")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        
        # Check if the request was successful
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Debugging: Print the raw response to see the structure
            print("Response data:", data)
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            if articles:
                print("HEADLINES:")
                speak("HEADLINES")
                for article in articles:
                    title = article.get('title')
                    if title:
                        speak(title)
                    else:
                        print("No title found for an article.")
            else:
                print("No articles found.")
        
            print(f"Failed to fetch news. Status code: {r.status_code}")

    elif "activate chatbot" == c.lower() or "activate chat bot" == c.lower() or "activate chat box" == c.lower() :
        print("Enter sender's name : ")
        speak("Enter sender's name : ")
        
        
        try: 
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3)
            print("Recognizing...")
        
            #listen for the sender name
            sender = r.recognize_google(audio)
            print(sender)
        except Exception as e :
            print(e)
            
        
        webbrowser.open("https://web.whatsapp.com")
        # pyautogui.click(1041, 1058)

        # Wait for 2 seconds
        time.sleep(20)

        # pyautogui.click(662, 463)
        # time.sleep(5)
        # pyautogui.write("web whatsapp")
        # pyautogui.press('enter')

        # pyautogui.click(259, 449)
        # time.sleep(10)

        pyautogui.click(231, 241)
        pyautogui.write(sender)

        pyautogui.press('enter')
        time.sleep(4)


        i = 0
        # Move to starting point of drag (753, 220), then drag to (876, 957)
        while i == 0:
            pyautogui.moveTo(744, 228)
            pyautogui.dragTo(1870, 912, duration=1, button='left')

            # Copy content (Ctrl + C)
            pyautogui.hotkey('ctrl', 'c')

            # Wait to ensure content is copied
            time.sleep(3)

            # Retrieve the copied content using pyperclip
            copied_content = pyperclip.paste()
            if copied_content != "":
                pyautogui.click(876,957)
                
                message = copied_content.split("2024]")[-1]
                if  message.lower().endswith("bye"):
                    i=1 
                    pyautogui.write("Bye see you...")
                    pyautogui.press("enter")
                    pyautogui.hotkey('alt', 'tab')
                    break
                if sender.lower() in message.lower():
                    # Click at coordinate (1284, 880) to unselect
                    pyautogui.click(686, 243)

                    # Print or store the copied content
                    print(copied_content)

                    pyautogui.click(876,957)

                    # AI PROCESS 
                    try:
                        client = DuckGPT(model="gpt-4o-mini")
                        # models = client.Models()
                        text = client.Chat(f"response like a human in chat, read the chat history and response like a human , replyes will be short and to the piont, here your name is arijit and another person is your friend, you can communicate with him in hindi,english and also in bengali as per the sender's language. output should be reply of the next chat, don't include time, date and : at the begining of the output, here is the chat history {copied_content}", [])
                        print(text)
                        
                        pyautogui.write(text)

                        # Simulate pressing the 'Enter' key
                        pyautogui.press('enter')
                    except Exception as e :
                        print(e)           
    else:
        #let AI to handel this code
        print("Working on it...")
        speak("Working on it...")
        data = ai (c)
        speak(data.split(":")[0])
        

if __name__ == "__main__":
    speak("initializing friday")

    #listening our comand
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit= 2)
            print("Recognizing...")
        
            #listen for the wake word "sangeeta"
            word = r.recognize_google(audio)
            if(word.lower() == "friday"):
                onword = "lISTENING BOSS.."
                print(onword)
                speak(onword)
                with sr.Microphone() as source:
                    print("ACTIVATED...")
                    audio = r.listen(source)
                    comand = r.recognize_google(audio)
                    if comand.lower() == "stop":
                        print ("See you soon sir ...") 
                        speak("See you soon sir ...")
                        break 
                    print(comand)    
                    comandprocess (comand) 
                
        except Exception as e:
            print("")

