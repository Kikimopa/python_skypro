import random
import json
import os

def get_word(file_name= "lesson6/data/words.txt"):
    with open(file_name, "r") as file:
        src = file.read().split()
    random_word = random.choice(src)
    return random_word

def get_shuffle_word(word):
    return ''.join(random.sample(word, len(word)))

def create_file(file_name = "lesson6/data/statistic.json"):
    players = {'players': {}}
    with open(file_name, "a") as file:
        json.dump(players, file, ensure_ascii=False, indent=4)

def write_statitic(name, true_words, points, file_name = "lesson6/data/statistic.json"):
    if not os.path.exists(file_name):
        create_file()           
    with open(file_name, "r") as src:
        file = json.load(src)
    
    if file['players'].get(name, None) == None:      
        file['players'][name] = []
        file['players'][name].append(
        {'games': 1,
        'true_words': true_words,
        'points': points})
        with open (file_name, 'w') as file_out:
            file_out.write(json.dumps(file))
 
    else:
        if points > file['players'][name][0]['points']:
            file['players'][name][0]['points'] = points
        file['players'][name][0]['games'] = file['players'][name][0]['games'] + 1
        file['players'][name][0]['true_words'] = file['players'][name][0]['true_words'] + true_words
        with open(file_name, 'w') as file_out:
            file_out.write(json.dumps(file))

    
def get_statistic(name, file_name= "lesson6/data/statistic.json"):
    with open(file_name, "r") as file:
        src = json.load(file)
    print(f"Всего сыграно игр: {src['players'][name][0]['games']}\nМаксимально количество очков: {src['players'][name][0]['points']}")

def main():
    flag = True
    while flag:
        points = 0
        true_words = 0
        name = input("Введите свое имя:\n")
        while flag:
            word = get_word()
            shufle_word = get_shuffle_word(word)
            print(f'Угадайте слово: {shufle_word}')
            answer = input()
            if answer.lower() == word:
                print("\033[32mВерный ответ!\033[0m")
                points += 10
                true_words += 1
            else:
                print(f"\033[3;31mНеправильно!\033[0m\nСлово было: {word}")
            
            exit_word = input("Для выходы введите: exit\n")
            if exit_word.lower() == 'exit':
                flag = False

    write_statitic(name, true_words, points)
    get_statistic(name)

if __name__ == "__main__":
    main()