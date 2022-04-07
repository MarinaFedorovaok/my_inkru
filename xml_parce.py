import xml.etree.ElementTree as ET

def replacement (dictionary, str):
    if str in dictionary:
        return (dictionary[str])
    else:
        return str

def parce_subtree(node, dictionary):
    # обрабатываем текующую вершину
    if 'tspan' in node.tag and node.text != None:
        #print(node.text)
        node.text = replacement(dictionary, node.text)
    for child in node:
        # обрабатываем ее сыновей 
        parce_subtree(child, dictionary)

#Отличная справка: https://olegmax.readthedocs.io/ru/latest/represents-2.html
