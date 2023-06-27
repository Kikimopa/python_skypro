# HW
print("Привет! Предлагаю проверить свои знания английского!\n Расскажи как тебя зовут!")
name = str(input())
print(f"Привет, {name}, начнем тренировку!")
count_questions = 0
total = 0
# 1 question
print(f"My name ____ Vova")
word = str(input())
if word.lower() == "is":
    total += 10
    count_questions += 1
    print("Ответ верный!\n Вы получаете 10 балов!")
else: print("Неправильно.\n Правильный ответ: is")
# 2 question
print(f"I ____ a coder")
word = str(input())
if word.lower() == "am":
    total += 10
    count_questions += 1
    print("Ответ верный!\n Вы получаете 10 балов!")
else: print("Неправильно.\n Правильный ответ: am")
# 3 question
print(f"I live ____ Moscow")
word = str(input())
if word.lower() == "in":
    total += 10
    count_questions += 1
    print("Ответ верный!\n Вы получаете 10 балов!")
else: print("Неправильно.\n Правильный ответ: in")
percent = (100/ 3)* count_questions
print(f"Вот и все, {name}")
print(f"Вы ответили на {count_questions} вопросов из 3 верно.")
print(f"Вы заработали {total} балов")
print(f"Это {percent} процентов.")