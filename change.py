f = open('text.txt', 'r')
file_out = open("text_result.txt", "w")
while True:
    # считываем строку
    line = f.readline()
    text = line.replace(" is ", " was ")
    file_out.write(text)

    # прерываем цикл, если строка пустая
    if not line:
        break
   

# закрываем файл
f.close
file_out.close