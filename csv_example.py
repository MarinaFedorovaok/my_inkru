import csv
from operator import length_hint
import string

def csv_to_dictionaries (file_csv):
    dictionary = {}
    list_of_dictionaries = []
    with open(file_csv, newline='') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=",", quotechar='"'))
        for j in range (1, len(spamreader)):
            for i in range (len(spamreader[0])):
                dictionary[spamreader[0][i]] = spamreader[j][i]
            list_of_dictionaries.append(dictionary.copy())
        #print (list(spamreader))
        for row in spamreader:
            print(', '.join(row))
    return list_of_dictionaries