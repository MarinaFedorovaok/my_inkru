import xml.etree.ElementTree as ET

def replacement (dictionary, str):
    if str in dictionary:
        return (dictionary[str])
    else:
        return str

def parce_subtree(node, dictionary):
    if 'tspan' in node.tag and node.text != None:
        #print(node.text)
        node.text = replacement(dictionary, node.text)
    for child in node:
        parce_subtree(child, dictionary)

