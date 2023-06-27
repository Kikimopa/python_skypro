errors = {
    "out":"Вы вышли из системы",
    "noaccess":"У вас нет доступа в раздел",
    "unknown":"Неизвестная ошибка",
    "timeout":"Система долго не отвечает",
    "robot":"Ваши действия похожи на робота"
}

def get_error(*args):
    err_list = []
    for k in args:
        err_list.append(errors[k])

    return print(err_list)

def main():
    get_error("robot", "timeout")

if __name__ == "__main__":
    main()