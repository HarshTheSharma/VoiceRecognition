import speech_recognition as sr

def VoiceRecog():
    def recognize_speech_from_mic(recognizer, microphone):

        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
            audio = recognizer.listen(source)

        # Respond
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable
            response["success"] = False
            response["error"] = "API unavailable/unresponsive"
        except sr.UnknownValueError:
            response["error"] = "Unable to recognize speech"

        return response

    if __name__ == "__main__":
        recognizer = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        response = recognize_speech_from_mic(recognizer, mic)
        print('\nSuccess : {}\nError   : {}\n\nText from Speech\n{}\n\n{}' \
              .format(response['success'],
                      response['error'],
                      '-'*17,
                      response['transcription']))
VoiceRecog()
