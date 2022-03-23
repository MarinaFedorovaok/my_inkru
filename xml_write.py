
from logging import root
import xml.etree.ElementTree as ET
f = open('text_result.txt', 'r')
tree = ET.parse('beerJournal.xml')
root = tree.getroot()

# for beer in root:
#    lines = f.readlines()
#    root[i][0].text = "\n" + lines[i+1]
#    print(lines[i+1])
#    i +=1
lines = f.readlines()
j = 1
for beer in root.iter('Beer'):
  
   # #print(len(lines))
   # for i in range(1, len(lines)):
   print (len(lines))
   beer.text= '\n' + lines[j]
   print(lines[j])
   j+=2
   
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