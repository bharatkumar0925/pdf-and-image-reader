import pyttsx3

# Function to perform text-to-speech
def tts(text, output_path, voice_index=1, speed=10, save_file=False):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('speed', speed)
    if not save_file:
        engine.say(text)
    else:
        engine.save_to_file(text, output_path+'.mp3')
    engine.runAndWait()

