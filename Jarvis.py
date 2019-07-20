import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random

speech=sr.Recognizer()

greeting_dict={'hello':'hello','hi':'hi'}
open_launch_dict={'open':'open','launch':'launch'}
social_media_dict={'facebook':'http://www.facebook.com','instagram':'http://www.instagram.com'}
google_searches_dict={'what':'what','which':'which','how':'how','why':'why'}

try:
    engine=pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initialize')
    
voices=engine.getProperty('voices')   


    
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

rate=engine.getProperty('rate')
engine.setProperty('rate',rate==100) 

def is_valid_google_search(phrase):
    if(google_searches_dict).get(phrase.split(' ')[0]==phrase.split(' ')[0]):
        return True
    

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()
    
def read_voice_cmd():
    voice_text=' '
    print('Listening...')
    with sr.Microphone() as source:      
        audio=speech.listen(source=source,timeout=5,phrase_time_limit=10)
        
        try:                        
            voice_text=speech.recognize_google(audio)
            print('Network Problem')
        except sr.UnknownValueError:            
            pass        
        return voice_text
    
def is_valid_note(greet_dict,voice_note):
    for key,value in greet_dict.iteratitem():
        try:
            if value==voice_note.split(' ')[0]:
                return True 
                break
        except IndexError:
            pass
        return False
        
if __name__=='__main__':
    speak_text_cmd('hello jayant this is gwen your artificial intelligence')
    
while True:    
    voice_note=read_voice_cmd()
    print('cmd:{}'.format(voice_note))   
    
    if 'hello' in voice_note:               
        speak_text_cmd('hello sir how can i help you')
        continue      
      
    elif is_valid_note(open_launch_dict,voice_note):               
        print('Opening')
        speak_text_cmd('sure sir') 
        if(is_valid_note(social_media_dict,voice_note)):
            key=voice_note.split(' ')[1]
            webbrowser.open(social_media_dict.get(key))
            
        else:         
            os.system('explore C:\\"{}"'.format(voice_note.replace('open',' ').replace('launch','')))
        continue
    
    elif is_valid_google_search(voice_note):
        print('searching...')
        speak_text_cmd('getting sir')
        webbrowser.open('http://www.google.co.in/search?q={}'.format(voice_note))
        continue
        
    elif 'bye' in voice_note:         
         speak_text_cmd('bye sir happy to help have a nice day')
         exit()
