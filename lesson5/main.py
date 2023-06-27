import string
import json
import secrets

def get_random_word(lenght):
    word = "".join(secrets.choice(string.ascii_letters) for i in range(lenght))
    return str(word)


def morse_encode(lenght):
    word = get_random_word(lenght).lower()
    split_word = []
    for i in range(lenght):
        split_word.append(word[i])
    code_list = []
    with open("lesson5/morse-code.json", "r")as file:
        morse_code: morse_code = json.load(file)
    print(split_word)
    for i in split_word:
        k = morse_code[i]
        code_list.append(k)

    coded_word = '|'.join(code_list)

    return [coded_word, word]   


def print_statistic(true_ans, false_ans):
    answers = len(true_ans) + len(false_ans)
    return print(f'Всего вопросов: {answers}\nПравильных ответов: {len(true_ans)}\nНеправильных ответов: {len(false_ans)}')



def main():
    flag = True
    true_ans = []
    false_ans= []
    print("Сегодня мы потренируемся расшифровывать морзянку.\nВведите ENTER и начнем ")
    input()
    while flag:
        
        exit = input("Для выходы введите: exit\n")
        if exit.lower() == 'exit':
            flag = False
            break
        print("Ведите количество символов: ")
        lenght = int(input())
        word = morse_encode(int(lenght))
        print(f'Слово: {word[0]}\nОтвет: ')
        answer = str(input())
        
        if answer == word[1]:
            true_ans.append("True")
            print("\033[32mВерный ответ!\033[0m")
        else:
            false_ans.append("False")
            print(f"\033[3;31mНеправильно!\033[0m\nСлово было: {word[1]}")
    
    if len(true_ans) == 0 and len(false_ans) == 0:
        pass
    else:
        print_statistic(true_ans, false_ans)      
        

if __name__ == "__main__":
    main()
