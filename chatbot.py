import google.generativeai as ai
import pyttsx3 as px

en=px.init()
def speak(text):
    en.say(text)
    en.runAndWait()


API_KEY='api-key'  #generate your own api key
ai.configure(api_key=API_KEY)
model=ai.GenerativeModel("gemini-pro")
chat= model.start_chat()


while True:
    message= input('you: ')
    if message.lower() =="bye":
        print("Friday: goodbye")
        break
    response=chat.send_message(message)
    print("Friday: ",response.text)
    speak(response.text)



