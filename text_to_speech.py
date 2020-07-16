from math import ceil

import speech_recognition as sr

r = sr.Recognizer()

for i in range(38, 41):
    audio = f"video9/video9-{i}.wav"

    with sr.AudioFile(audio) as source:
        audio = r.record(source)
        print('Done! ' + "video9-" + str(i) + ".wav")

    try:
        text = r.recognize_google(audio)
        with open('video9/video9_new.txt', 'a') as f:
            f.write(text)

    except Exception as e:
        print(e)
