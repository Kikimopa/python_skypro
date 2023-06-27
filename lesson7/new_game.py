import json
import prettytable



def load_prices(value):
    res = []
    for val in value:
        if 'price' in val and not val['asked']:
            res.append(val['price'])
        else :
            res.append(' - ')
    return res 

def print_table(src):
    x = prettytable.PrettyTable()
    for k, v in src.items():
        x.add_column(
            k, load_prices(v)
        )
    print(x)



def get_question_answer(src, user_input):
    if src.get(user_input[0], "Нет такой категории!"):
        for v in src[user_input[0]]:
            if v['price'] ==  user_input[1] :
                if v['asked'] == False :
                    return (v['question'], v['answer'])
                else:
                    print("Такого вопроса нет. Попробуйте еще раз!")
    
        print("В данной категории больше не осталось вопросов! Введите другую категорию")
        




def save_statistic(points, r_quest, w_quest, file_name = "lesson7/data/statistic.json"):
    with open(file_name, "w") as file:
        statistic = {"game": []}
        statistic["game"].append({
            'points': points,
            "correct": r_quest,
            "incorrect": w_quest
        })
        file.write(json.dumps(statistic))




def main():
    with open("lesson7/data/questions.json") as file:
        src = json.loads(file.read())
    points = 0
    wright_questions = 0
    wrong_questions = 0
    
    flag = True
    while flag:
        print_table(src)
        user_input = input("Ведите категорию и стоимость...\n").split(' ')
        question, answer = get_question_answer(src, user_input)
        print(f"Слово {question} в переводе означает ...")
        user_answer = input("Ответ ...\n")
        if user_answer.lower() == answer:
            points += 200
            wright_questions += 1
            print(f"\033[32mВерно, +200, Ваш счет: {points}\033[0m")  
        else:
            wrong_questions += 1
            print(f"\033[3;31mНеверно!\033[0m\ Правильный ответ: {answer}")
        for v in src[user_input[0]]:
            if v['price'] == user_input[1]:
                v['asked'] = True

    save_statistic(points, wright_questions, wrong_questions)

if __name__ == "__main__":
    main()