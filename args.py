#!/usr/bin/python3
from argparse import ArgumentParser, FileType
import xml_parce as xml
import csv_example as csv
import xml.etree.ElementTree as ET
import csv_example as csv

def line_to_dictionaty():
    parser = ArgumentParser()
    parser.add_argument("--file", dest="filename",
                        help="write report to FILE", metavar="FILE")
    parser.add_argument('inputfile', nargs=1, type=FileType('r'), help = "template file", metavar="template_file")

    return vars(parser.parse_args())

#print(line_to_dictionaty())

import xml_parce as xml
args_dict = line_to_dictionaty()
file_csv = args_dict['filename']
#print (file_csv)
list_dict = csv.csv_to_dictionaries (file_csv)
#print(list_dict)

for i in range (len(list_dict)):
    dictionary = list_dict[i]
    print(dictionary)
    tree = ET.parse('template.svg')
    root = tree.getroot()
    xml.parce_subtree(root, dictionary)
    tree.write('output_write_' + str(i) + '.svg')