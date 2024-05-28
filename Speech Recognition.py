import speech_recognition  as sr

filename="filename"
r=sr.Recognizer()
with sr.AudioFile(filename) as source:
  audio_date = r.record(source)
  text = r.recognize_google(audio_date)
  print(text)
