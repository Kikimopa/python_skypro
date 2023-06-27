import json
import os
import prettytable



def load_questions(file_path = "lesson7/data/questions.json"):
    with open(file_path) as file:
        src = json.loads(file.read())
    x = prettytable.PrettyTable()
    x.field_names = src.keys()
    count = 0
    for v in src.values():
        x.add_row(
             load_prices(v)
        )
    return print(x)

def load_prices(value):
    res = []
    for val in value:
        if 'price' in val and not val['asked']:
            res.append(val['price'])
        else :
            continue
    return res 


# def show_field(answer = False, pars_data = None):
#     src = load_questions()
#     questions_coast = []
#     count = 0
#     if pars_data == None:
#         pass
#     else:
#         src['questions'][pars_data[0]][pars_data[1]]["asked"] = True
    
#     for k in src['questions'].keys():
#         questions_coast.append([k])
#         for v in src['questions'][k]:
#             if src['questions'][k][v]["asked"] == False:
#                 if v in questions_coast[count]:
#                     continue
#                 else:
#                     questions_coast[count].append(v)
#             else:
#                 questions_coast[count].append(' ')
               
#         count += 1

#     for i in range(len(questions_coast)):
#         print(*questions_coast[i], sep=" | ")
    

def pars_input(data_input):
    if not data_input[0]:
        return print("Введите категорию")
    elif not data_input[1]:
        return print("Введите стоимость")
    
    else: 
        if data_input[0] and data_input[1]:
            label = data_input[0]
            coast = data_input[1]
            output_data = (label, coast)
            return output_data
   
        

def get_question(data):
    pars_data = pars_input(data)
    src = load_questions()
    question = src['questions'][pars_data[0]].get(pars_data[1],None)
    if question:
        word = src['questions'][pars_data[0]][pars_data[1]]['question']
        print(f"Слово {word} в переводе означает ...")
        
    else:
        print("Такого вопроса нет. Попробуйте еще раз!")
    

def save_statistic(points, r_quest, w_quest, file_name = "lesson7/data/statistic.json"):
    with open(file_name, "w") as file:
        statistic = {"game": []}
        statistic["game"].append({
            'points': points,
            "correct": r_quest,
            "incorrect": w_quest
        })
        file.write(json.dumps(statistic))

def save_progress(pars_data):
    with open("lesson7/data/questions.json", 'r') as file:
        src = json.loads(file.read())

    if os.path.exists("lesson7/data/progress.json"):
        pass
    else:
        with open("lesson7/data/progress.json", "w") as file:
            src['questions'][pars_data[0]][pars_data[1]]["asked"] = True
            file.write(json.dumps(src))

def processing(user_input, data):
    pass
    

def main():
    load_questions()


# def main():
#     flag = True
#     points = 0
#     right_questions = 0
#     wrong_questions = 0
#     while flag:
#         field = show_field(load_questions())
#         while flag:
#             user_input = input("Ведите категорию и стоимость...\n").split(' ')
#             get_question(user_input)
#             user_answer = input("Ответ ...\n")
#             pars_data = pars_input(user_input)
#             questions = load_questions()
#             right_answer = questions['questions'][pars_data[0]][pars_data[1]]['answer']
#             if user_answer.lower() == right_answer:
#                 points += 200
#                 right_questions += 1
#                 print(f"\033[32mВерно, +200, Ваш счет: {points}\033[0m")
#             else:
#                 wrong_questions += 1
#                 print(f"\033[3;31mНеверно!\033[0m\ Правильный ответ: {right_answer}")
            
#             exit_word = input("Для выходы введите: exit\n")
#             if exit_word.lower() == 'exit':
#                 flag = False
#             answer = True
#             save_progress(pars_data)

#     save_statistic(points=points, r_quest=right_questions, w_quest=wrong_questions)




if __name__ == "__main__":
    main()
