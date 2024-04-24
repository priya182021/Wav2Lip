import os
from gtts import gTTS
import speech_recognition as sr
from translate import Translator
import os
from deep_translator import GoogleTranslator
# from deep_translator import PonsTranslator


def translate(language,audio_output_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_output_path) as source:
        audio = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return False
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return False

    translation = GoogleTranslator(source='auto', target=language).translate(transcript) 
    # translator = Translator(to_lang="hi")
    # translation = translator.translate(transcript)
    print(translation)
    return translation


def translate_voice(language,audio_output_path,output_audio_file_location):
    text =translate(language,audio_output_path)
    voice = gTTS(text, lang=language)
    voice.save(output_audio_file_location)
    print("audio_saved")
    return True
