import speech_recognition as sr
from word2number import w2n
import moviepy.editor as mp

import constant
import pygame


def writeToFile(text):
   # Write audio to a text file
   with open(constant.FILE_PATH_SPEECH + constant.FILE_NAME_TXT, "w") as f:
      f.write(text)

def saveToWAVFile(audio):
   # Write audio to a WAV file
   with open(constant.FILE_PATH_RECORDINGS + constant.FILE_NAME_WAV, "wb") as f:
      f.write(audio.get_wav_data())

def wordToNum(text_list):
   for i in text_list:
      try:
         output = output + str(w2n.word_to_num(i)) + " "
      except:
         output = output + i + " "
   return output

def playClip(file_path):
   clip = mp.VideoFileClip(file_path).subclip(0, 5)
   print("Playing the video: {0}".format(clip.filename))
   clip.preview()
   pygame.quit()


# Create variable to have speech recognition
recording = sr.Recognizer()

while True:
   with sr.Microphone() as source:
      # Adjust noise
      recording.adjust_for_ambient_noise(source, duration=1)
      print("Please Say something:")
      # Create variable to store the speech
      audio = recording.listen(source)

   try:
      # Output the code in the terminal
      print("You said: \n" + recording.recognize_google(audio))

      # Store speech in a string variable
      text = recording.recognize_google(audio)
      text = text.lower()
      text_list = text.split()

      if 'quit' in text_list:
         break

      elif 'one' in text_list:
         playClip(constant.FILE_PATH_RECORDINGS+constant.OUTPUT_ONE)

      elif 'two' in text_list:
         playClip(constant.FILE_PATH_RECORDINGS+constant.OUTPUT_TWO)

      else:
         print("Can you repeat your answer?")
   except Exception as e:
      print(e)

print('Thank you and good bye!')


# saveToWAVFile(audio)


