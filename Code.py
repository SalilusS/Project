import re
MSTR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890!.,'\":; "

def start():
    number = 1
    print("-"*15)
    print("1. Записать")
    print("2. Закодировать")
    print("3. Декодировать")
    print("4. Прекратить выполнение")
    decision = input()
    if decision == "1":
        print("Введите текст:")
        with open('input.txt', 'w') as f:
            line = input()
            while line != "0":
                f.write(line + '\n')
                number += 1
                line = input()
        start()
    elif decision == "2":
        encryption()
    elif decision == "3":
        decoding()
    else:
        pass

def encryption():
    with open('input.txt') as text:
        print("Введите тип шифрования (Трёхзначное число):")
        try:
            code = int(input())
        except ValueError:
            print("Было введено не ЧИСЛО")
        if 100 <= code <= 999:
            code1 = code%10
            code = code//10
            code2 = code%10
            r = 0
            for line in text:
                r += 1
                i = -2
                for l in line:
                    i += 1
                    if i >= 0:
                        for b in range(len(MSTR)):
                            if line[i] == MSTR[b]:
                                pace = (b + (code2**r)*code1*code**i)%136
                        try:
                            line = line[:i] + re.sub(line[i], MSTR[pace], line[i]) + line[(i + 1):]
                        except ValueError and re.error:
                            continue
                        except UnboundLocalError:
                            continue
                    else:
                        pass
                print(line[:-1])
        else:
            print("Было введено не ТРЁХЗНАЧНОЕ число")
    start()

def decoding():
    with open('input.txt') as text:
        print("Введите тип шифрования (Трёхзначное число):")
        try:
            code = int(input())
        except ValueError:
            print("Было введено не ЧИСЛО")
        if 100 <= code <= 999:
            code1 = code % 10
            code = code // 10
            code2 = code % 10
            r = 0
            for line in text:
                r +=1
                i = -2
                for l in line:
                    i += 1
                    if i >= 0:
                        for b in range(len(MSTR)):
                            if line[i] == MSTR[b]:
                                pace = (b - (code2**r)*code1*code**i)%136
                        try:
                            line = line[:i] + re.sub(line[i], MSTR[pace], line[i]) + line[(i + 1):]
                        except ValueError and re.error:
                            continue
                        except UnboundLocalError:
                            continue
                    else:
                        pass
                print(line[:-1])
        else:
            print("Было введено не ТРЁХЗНАЧНОЕ число")
    start()
print("1. Запись прекращается цифрой \"0\"")
print("2. Чтобы декодировать файл, надо сначала его записать")

start()
