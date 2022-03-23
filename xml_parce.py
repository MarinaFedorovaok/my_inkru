import xml.etree.ElementTree as ET
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
parce_xml('beerJournal.xml')