import xml.etree.ElementTree as ET
def parce_subtree(root):
    # обрабатываем текующую вершину
    if 'tspan' in root.tag and root.text != None:
        print(root.text)
    for child in root:
        # обрабатываем ее сыновей 
        parce_subtree(child)

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
tree = ET.parse('template.svg')
root = tree.getroot()
parce_subtree(root)

#Отличная справка: https://olegmax.readthedocs.io/ru/latest/represents-2.html