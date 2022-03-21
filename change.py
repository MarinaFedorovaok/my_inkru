f = open('text.txt', 'r')
file_out = open("text_result.txt", "w")
# change_what = open('change_what.txt', 'r')
# change_to = open('change_to.txt', 'r')
def change_word (was, will):
    while True:
        # считываем строку
        line = f.readline()
        # what = change_what.readline()
        # print(what)
        # to = change_to.readline()
        # print(to)
        text = line.replace(was, will)
        file_out.write(text)

        # прерываем цикл, если строка пустая
        if not line:
            break
   
# закрываем файлы
f.close
file_out.close
change_word(' is ', ' was ')
# change_to.close
# change_what.close