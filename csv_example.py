import csv
from operator import length_hint
import string
dictionary = {}
list_of_dictionaries = []
with open('user_file.csv', newline='') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter=",", quotechar='"'))
    for j in range (len(spamreader)):
        for i in range (len(spamreader[0])):
            dictionary[spamreader[0][i]] = spamreader[j][i]
        list_of_dictionaries.append(dictionary)
    #print (list(spamreader))
    for row in spamreader:
        print(', '.join(row))
print(list_of_dictionaries)
