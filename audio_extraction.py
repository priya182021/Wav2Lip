import os
from moviepy.editor import VideoFileClip

def extract_audio(PATH_TO_YOUR_VIDEO, audio_output_path):
    video_clip = VideoFileClip(PATH_TO_YOUR_VIDEO)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_output_path)
    video_clip.close()
# from deep_translator import PonsTranslator
# langs_list = PonsTranslator.get_supported_languages(as_dict=True) 
# print(langs_list)