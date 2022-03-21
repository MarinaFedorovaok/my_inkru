from xml.etree.ElementTree import ElementTree
tree = ElementTree()
tree.parse("beerJournal.xml")
p = tree.find('verb')
for i in p:
    print (p[i].text)
