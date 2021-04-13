#控制音量
import pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')
#engine.setProperty('volume', volume-0.25) 不明显
engine.setProperty('volume', 1)
engine.say('I will always love you')
engine.runAndWait()