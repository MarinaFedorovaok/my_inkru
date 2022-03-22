from logging import root
import xml.etree.ElementTree as ET
f = open('text_result.txt', 'r')
tree = ET.parse('beerJournal.xml')
root = tree.getroot()
for beer in root.iter('Beer'):
   beer.text = "\n" + f.readline()
tree.write('output.xml')

# def write_xml(file_to_parce, file_to_join):
#     tree = ET.parse(file_to_parce)
#     root = tree.getroot()
#     #print(type(root))
#     f = open(file_to_join, 'r')
#     for child in root:
#         #print(child.tag, child.attrib)
#         root[0][0].text = f.readline
#     tree.write('result.xml')
# write_xml('beerJournal.xml', 'text_result.txt')