from datetime import datetime
import speech_recognition  as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha


# Speech Initialization
Speech = pyttsx3.init()
voices = Speech.getProperty('voices')
Speech.setProperty('voice', voices[0].id) # 0 for male, 1 for female
activationword = 'computador'


# Browser Configuration
opera_path = r"C:\Users\Windows_PC\AppData\Local\Programs\Opera GX\opera.exe"
webbrowser.register("opera", None, webbrowser.BackgroundBrowser(opera_path))

def speak(text, rate=200):
    Speech.setProperty('rate', rate)
    Speech.say(text)
    Speech.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print("Listening for a command")
    
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)
        
    
    try:
        print("Recogninzing Speech...")
        query = listener.recognize_google(input_speech, language='pt-BR')
        print(f"The input speech was: {query}")
    except Exception as exception:
        print("I did not quite catch that")
        speak("Eu não entendi")
        print(exception)
        return 'None'
    
    return query
    
    
# Main function
if __name__ == '__main__':
    speak("Iniciando Sistema")
    
    while True:
        query = parseCommand().lower().split()
        
        if query[0] == activationword:
            query.pop(0)
            
            if query[0] == 'fale':
                if 'olá' in query:
                    speak("Ola Mundo")
                else:
                    query.pop(0)
                    speech = " ".join(query)
                    speak(speech)
            elif query[0] == 'vá' and query[1] == 'para' or query[0] == 'abra':
                query = " ".join(query[2:])
                speak(f"Abrindo {query}")
                webbrowser.get("opera").open_new(query)
            elif query[0] == 'exit':
                exit()
    
    