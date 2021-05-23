import datetime
now = datetime.datetime.now()
time = now.strftime("%H:%M")
date = now.strftime("%Y-%m-%d")

print(time)
print(date)

from gtts import gTTS
import os
myobj = gTTS(text=time, lang='en', slow=False)
myobj.save("hello.mp3")
os.system("mpg321 hello.mp3")

myobj = gTTS(text=date, lang='en', slow=False)
myobj.save("hello.mp3")
os.system("mpg321 hello.mp3")

