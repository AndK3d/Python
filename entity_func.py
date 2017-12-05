import xml.etree.ElementTree as ET

CIGITaskConfig = 'CIGITaskConfig.xml'
DBDefaultConfig = 'DBDefaultConfig.xml'
renderHost = 'renderHost_masterV3_insgraf.conf'

def get_xml_entity_list(file):

    xml_tree = ET.parse(CIGITaskConfig)
    print
    for entity in xml_tree.iter('Entity'):
        print (entity.attrib)




get_xml_entity_list('E:/py_dev/entity_editor/DBDefaultConfig.xml')