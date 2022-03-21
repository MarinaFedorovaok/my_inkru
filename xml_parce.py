import xml.etree.ElementTree as ET
def parce_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    #print(type(root))
    f = open('text.txt', 'w')
    for child in root:
        #print(child.tag, child.attrib)
        f.write(root[0][0].text)
parce_xml('beerJournal.xml')