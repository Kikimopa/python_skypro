questions = ["My name __ Vova", "I __ a coder", "I live __ Moscow", "Fuck you?"]
answers = ["is", "am", "in", "yes"]
total = 0
points = [3,2,1]


ready = str(input("Привет! Предлагаю проверить свои знания английского! Набери 'ready', чтобы начать!\n"))
if ready.lower() == 'ready':
    question = 0
    answer = 0
    total_quest = len(questions)
    total = 0
    true_answer = 0
    
    question_flag = True
    flag = True
    while flag:
        attempt = 3
        for i in range(3):
            print(f"Question\n{questions[question]}")
            answer_word = str(input())
            if answer_word == answers[answer]:
                print("Ответ верный!")
                question += 1
                answer += 1
                total += points[i]
                true_answer += 1
                break
            else: 
                attempt -= 1
                print(f"Неправильно. Осталось попыток {attempt}")
            if attempt == 0:
                print(f"Правильный ответ: {answers[answer]}")
                question += 1
                answer += 1
        
        total_quest-= 1
               
        if total_quest != 0:
            continue
        else: 
            flag = False
    print(f"Вот и все! Вы ответили на {true_answer} вопросов из {len(questions)} верно, это {(100 / len(questions) * true_answer)} процентов.\nИтог: {total} баллов.")   

else: print("Кажется, вы не хотите играть. очень жаль.")