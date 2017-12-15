import xml.etree.ElementTree as ET

CIGITaskConfig = 'CIGITaskConfig.xml'
DBDefaultConfig = 'DBDefaultConfig.xml'
renderHost = 'renderHost_masterV3_insgraf.conf'


def get_child(parent):
    print (parent.tag, parent.attrib)

    for key in parent.attrib:
        print(key, ' = ', parent.attrib[key])
    for i in range(0, len(parent)):
        get_child(parent[i])


def get_xml_entity_list(file):
    xml_tree = ET.parse(file)
    xml = xml_tree.findall('Entity')
    for entity in xml:
        get_child(entity)

def add_row(values=[]):

    #item = [QStandardItem(text),QStandardItem(text),QStandardItem(text)]

    items_list = []
    for text in values:
        item = QStandardItem(text)
        items_list.append(item)

    print (items_list)
    return

#get_xml_entity_list(CIGITaskConfig)
add_row([1,2,3])