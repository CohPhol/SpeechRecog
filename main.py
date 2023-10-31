import speech_recognition as sr
from word2number import w2n

import constant

# Create variable to have speech recognition
recording = sr.Recognizer()

with sr.Microphone() as source:
   # Adjust noise
   recording.adjust_for_ambient_noise(source, duration=1)
   print("Please Say something:")
   # Create variable to store the speech
   audio = recording.listen(source)
try:
   # Output the code in the terminal
   print("You said: \n" + recording.recognize_google(audio))
except Exception as e:
   print(e)

# Write audio to a WAV file
with open(constant.file_path_recordings + constant.file_name_wav, "wb") as f:
   f.write(audio.get_wav_data())

# Store speech in a string variable
text = recording.recognize_google(audio)
text = text.lower()

# Store string to a list
text_list = list(text.split(" "))

output = ""

for i in text_list:
   try:
      output = output + str(w2n.word_to_num(i)) + " "
   except:
      output = output + i + " "

# Write audio to a text file
with open(constant.file_path_speech + constant.file_name_text, "w") as f:
   f.write(output)
