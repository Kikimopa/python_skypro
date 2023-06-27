questions = {
"easy": {
    "cat" : "кошка",
    "dog": "собака",
    "elephant": "слон",
    "dolphin": "дельфин", 
    "horse": "лошадь"
},
"medium": {
    "chair": "стул",
    "table": "стол",
    "car": "автомобиль",
    "potato": "картошка",
    "carrot": "морковь"
},
"hard": {
    "charity": "благотворительность",
    "pressure": "давление",
    "historian": "историк",
    "storage": "хранилище",
    "kitchen": "кухня"
}
}

levels = {
    "1" : "easy",
    "2" : "medium",
    "3" : "hard"
}

answers = {}
points = 0
print("Привет! Дававй сыграем в игру.")
lvl = input("Выбери уровень словжности (easy, medium, hard)")
for k in questions[lvl]:
    print(f"{k}, {len(questions[lvl][k])} букв, первая буква: {questions[lvl][k][0]}")
    user_answer = input("Ответ: ")
    if user_answer.lower() == questions[lvl][k]:
        print(f"Верно! {k} это {user_answer}")
        answers[questions[lvl][k]] = "True"
    else: 
        print("Не правильно")
        answers[questions[lvl][k]] = "False"

good_mark = 0
for i in answers.values():
    if i == "True":
        good_mark += 1


print("Итог: ")
for k,v in answers.items(): print(f'{k} - {v}')
if 4 <= good_mark >= 5:
    print(f"Ваш ранг: Отлично")
elif good_mark == 3:
    print(f"Ваш ранг: Удовлетворительно")
else:
    print(f"Ваш ранг: Плохо")
