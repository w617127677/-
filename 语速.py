import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+100)
engine.say('I will always love you')
engine.runAndWait()
#控制语速(频率处理）