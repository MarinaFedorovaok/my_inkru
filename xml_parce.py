import xml.etree.ElementTree as ET
def parce_subtree(node):
    # обрабатываем текующую вершину
    if 'tspan' in node.tag and node.text != None:
        node.text = 'Hello, world'
        print(node.text)
    for child in node:
        # обрабатываем ее сыновей 
        parce_subtree(child)

tree = ET.parse('template.svg')
root = tree.getroot()
parce_subtree(root)
tree.write('output_write.svg')

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