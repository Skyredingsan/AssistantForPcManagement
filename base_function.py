import os
import speech_recognition as sr


# Функция ответа от ИИ
def talk(words):
    print(words)
    os.system("say " + words)


# Анализ слов
def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        quest = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + quest)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        quest = command()

    return quest
