import moviepy.editor as mp
import speech_recognition as sr
import constant

# Load the video file
clip = mp.VideoFileClip(constant.FILE_PATH_RECORDINGS + constant.FILE_NAME_MKV)


# Extract audio from the video
audio = clip.audio


# Save the audio to a temporary WAV file
temp_audio_path = constant.FILE_PATH_RECORDINGS + "temp_audio.wav"
audio.write_audiofile(temp_audio_path)

# Initialize the speech recognition object
recognizer = sr.Recognizer()

# Convert audio to text
with sr.AudioFile(temp_audio_path) as source:
    audio_data = recognizer.record(source)

try:
    # Recognize speech using Google Web Speech API
    recognized_text = recognizer.recognize_google(audio_data)
    print("Transcribed Text: ", recognized_text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
