#imports
import speech_recognition as sr

#variables
recognizer = sr.Recognizer()


#A loop sending input to the API then printing the return
with sr.Microphone() as source:
    print('Please start speaking:\n')
    while True:
        audio_input = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_input)
            print(str(text))
        except Exception as e:
            print()
