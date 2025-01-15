import random

answers = {
    "Вопрос 1": ["Ответ 1", "Ответ 2", "Ответ 3"],
    "Вопрос 2": ["Ответ 5", "Ответ 6"],
    "Вопрос 3": ["Ответ 7", "Ответ 8", "Ответ 9", "Ответ 10"],
}

while True:
    question = input('Задайте ваш вопрос: ')

    if question in answers:
        print(random.choice(answers[question]))
    else:
        print("Не знаю ответ на данный вопрос")