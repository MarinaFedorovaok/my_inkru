import xml.etree.ElementTree as ET
#tree = ElementTree()
#tree.parse("beerJournal.xml")
tree = ET.parse('beerJournal.xml')
root = tree.getroot()
print(type(root))
for child in root:
    print(child.tag, child.attrib)
    print(root[0][0].text)
