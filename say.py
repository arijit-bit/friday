import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
engine.say('chymoral forte')
engine.runAndWait()