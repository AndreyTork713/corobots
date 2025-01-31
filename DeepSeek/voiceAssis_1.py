import speech_recognition as sr
import pyttsx3

# Инициализация распознавателя речи и синтезатора
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Функция для воспроизведения текста
def speack(text):
    engine.say(text)
    engine.runAndWait()

# Функция для распознавания речи
def listen():
    with sr.Microphone() as source:
        print('Слушаю...')
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ru-RU')
            print(f'Вы сказали: {text}')
            return text
        except sr.UnknownValueError:
            print('Извините, я не понял вас...')
            return ""
        except sr.RequestError:
            print('Произошла ошибка при запросе к сервису распознавания речи.')
            return ""


# Основной цикл работы помощника
def main():
    pyttsx3.speak('Привет! Чем я могу помочь?')
    while True:
        command = listen().lower()
        if "привет" in command:
            pyttsx3.speak('Привет! Как дела?')
        elif "пока" in command:
            pyttsx3.speak('До свидания!')
            break
        elif "как тебя зовут" in command:
            pyttsx3.speak('Меня зовут Помощник.')
        elif "что ты умеешь" in command:
            pyttsx3.speak('Я могу поздороваться, попрощаться и рассказать о себе.')
        else:
            pyttsx3.speak("Извините, я не понял вашу команду")


if __name__ == "__main__":
    main()

