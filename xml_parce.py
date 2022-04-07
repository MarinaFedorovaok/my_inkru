import xml.etree.ElementTree as ET
import csv_example as csv

def replacement (dictionary, str):
    if str in dictionary:
        return (dictionary[str])
    else:
        return str

def parce_subtree(node):
    # обрабатываем текующую вершину
    if 'tspan' in node.tag and node.text != None:
        #print(node.text)
        node.text = replacement(dictionary, node.text)
    for child in node:
        # обрабатываем ее сыновей 
        parce_subtree(child)

file_csv = 'user_file.csv'
list_dict = csv.csv_to_dictionaries (file_csv)
#print(list_dict)
for i in range (len(list_dict)):
    dictionary = list_dict[i]
    print(dictionary)
    tree = ET.parse('template.svg')
    root = tree.getroot()
    parce_subtree(root)
    tree.write('output_write_' + str(i) + '.svg')

#Отличная справка: https://olegmax.readthedocs.io/ru/latest/represents-2.html

def parce_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    #print(root)
    f = open('text.txt', 'w')
    global i
    i = 0
    for child in root:
        #print(child.tag, child.attrib)
        f.write(root[i][0].text)
        i +=1
#parce_xml('beerJournal.xml')