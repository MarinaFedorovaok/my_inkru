f = open('text.txt', 'r')
while True:
    # считываем строку
    line = f.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    print(line.strip())

# закрываем файл
f.close