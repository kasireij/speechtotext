import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'
speech_client = speech.SpeechClient()

# Example1. Transcribe local media file
# File Size: < 10mbs, Length < 1 minute

## Step 1. Load the media files (transcribes media files)
media_file_name_mp3 = 'demo audio.mp3'
media_file_name_wav = 'demo audio.wav'

with open(media_file_name_mp3, 'rb') as f1:
    byte_data_mp3 = f1.read()
audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

with open(media_file_name_wav, 'rb') as f2:
    byte_data_wav = f1.read()
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

## Step 2. Configure Media Files Output
config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-us'
)

config_wav = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-us',
    audio_channel_count=2
)
