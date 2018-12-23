import re
MSTR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890!.,'\":; "

def start():
    number = 1
    print("-"*15)
    print("1. Записать")
    print("2. Прочитать")
    print("3. Закодировать")
    print("4. Декодировать")
    print("5. Прекратить выполнение")
    decision = input()
    if decision == "1":
        print("Введите текст:")
        with open('input.txt', 'w') as file:
            line = input()
            while line != "0":
                file.write(line + '\n')
                number += 1
                line = input()
        start()
    elif decision == "2":
        with open('input.txt', 'r') as rto:
            for line in rto.readlines():
                print(line[:-1])
        start()
    elif decision == "3":
        encryption()
        start()
    elif decision == "4":
        decoding()
        start()
    else:
        pass

def encryption():
    another = ""
    with open('input.txt') as text:
        print("Введите тип шифрования (Трёхзначное число):")
        try:
            code = int(input())
        except ValueError:
            code = 100
            print("Было введено не ЧИСЛО")
            encryption()
        if 100 <= code <= 999:
            code1 = code%10
            code2 = (code//10)%10
            code = code//100
            r = 0
            for line in text:
                r += 1
                i = -2
                for l in line:
                    i += 1
                    if i >= 0:
                        for b in range(len(MSTR)):
                            if line[i] == MSTR[b]:
                                pace = (b + code2**r + code1*code**i)%136
                        try:
                            line = line[:i] + re.sub(line[i], MSTR[pace], line[i]) + line[(i + 1):]
                            pace = 1000
                        except ValueError and re.error and UnboundLocalError and IndexError:
                            continue
                    else:
                        pass
                another = another + line[:-1] + '\n'
            with open('input.txt', 'w') as fl1:
                fl1.write(another)
        else:
            print("Было введено не ТРЁХЗНАЧНОЕ число")
            encryption()

def decoding():
    another = ""
    with open('input.txt') as text:
        print("Введите тип шифрования (Трёхзначное число):")
        try:
            code = int(input())
        except ValueError:
            code = 100
            print("Было введено не ЧИСЛО")
            decoding()
        if 100 <= code <= 999:
            code1 = code%10
            code2 = (code//10)%10
            code = code//100
            r = 0
            for line in text:
                r += 1
                i = -2
                for l in line:
                    i += 1
                    if i >= 0:
                        for b in range(len(MSTR)):
                            if line[i] == MSTR[b]:
                                pace = (b - code2**r - code1*code**i)%136
                        try:
                            line = line[:i] + re.sub(line[i], MSTR[pace], line[i]) + line[(i + 1):]
                            pace = 1000
                        except ValueError and re.error and UnboundLocalError and IndexError:
                            continue
                    else:
                        pass
                another = another + line[:-1] + '\n'
            with open('input.txt', 'w') as fl2:
                fl2.write(another)
        else:
            print("Было введено не ТРЁХЗНАЧНОЕ число")
            decoding()

print("Запись прекращается цифрой \"0\"")

start()
