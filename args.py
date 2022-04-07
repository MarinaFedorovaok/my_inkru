#!/usr/bin/python3
import csv
from argparse import ArgumentParser, FileType
import xml_parce as xml
import xml.etree.ElementTree as ET


def csv_to_dictionaries (file_name):
    dictionary = {}
    list_of_dictionaries = []
    with open(file_name, newline='') as csvfile:
        csv_table = list(csv.reader(csvfile, delimiter=",", quotechar='"'))
        for j in range(1, len(csv_table)):
            for i in range(len(csv_table[0])):
                dictionary[csv_table[0][i]] = csv_table[j][i]
            list_of_dictionaries.append(dictionary.copy())
    return list_of_dictionaries

parser = ArgumentParser()
parser.add_argument("--file", dest="filename", help="write report to FILE", metavar="FILE")
parser.add_argument('input_file', nargs=1, help = "template file", metavar="template_file")
args_dict = vars(parser.parse_args())

file_name  = args_dict['filename']
list_dict = csv_to_dictionaries(file_name)

for i in range (len(list_dict)):
    dictionary = list_dict[i]
    tree = ET.parse(args_dict['input_file'][0])
    root = tree.getroot()
    print("Processing " + str(i) + '-th file...')
    print("Replacments: ", dictionary)
    xml.parce_subtree(root, dictionary)
    tree.write('output_write_' + str(i) + '.svg')