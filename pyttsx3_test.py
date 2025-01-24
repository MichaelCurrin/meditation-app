import pyttsx3


print("init")
engine = pyttsx3.init()
print("say")
engine.say("I will speak this text")
print("run")
engine.runAndWait()


rate = engine.getProperty("rate")
print(rate)
# 200.0
engine.setProperty("rate", 150)

engine.say("I will speak this text slower")
engine.runAndWait()
