import xml.etree.ElementTree as ET

CIGITaskConfig = 'CIGITaskConfig.xml'
DBDefaultConfig = 'DBDefaultConfig.xml'
renderHost = 'renderHost_masterV3_insgraf.conf'

result_list = []

def get_xml_entity_data(xml_filename):
    xml_tree = ET.parse(xml_filename)
    entity_tree = xml_tree.findall('Entity')

    return entity_tree

def get_child(tree, depth=0):
    for child in tree:
        if depth == 0:
            line = child.tag + '\n'
            #to console
            print(line)
            #to list
            result_list.append(line)
        else:
            #to console
            line = ' '*depth + child.tag + '\n'
            print(line)
            # to list
            result_list.append(line)

        #parameters
        for param in child.attrib:
            # to console
            line = ' '*(depth+4)+param + '\t' + child.attrib[param] + '\n'
            print(line)
            # to list
            result_list.append(line)
        get_child(child, depth+4)

    return True

entity_xml_tree = get_xml_entity_data(CIGITaskConfig)

get_child(entity_xml_tree)

with open('default.txt', 'wt') as f:
    for line in result_list:
        f.write(line)