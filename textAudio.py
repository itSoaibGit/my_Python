
from gtts import gTTS

Text = input("Enter the text you want to convert to audio: ")

tts = gTTS(text=Text, lang='en')
tts.save("output.mp3")

print("Audio file 'output.mp3' has been created successfully.")
