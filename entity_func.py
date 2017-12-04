import xml.etree.ElementTree as ET

CIGITaskConfig = 'CIGITaskConfig.xml'
DBDefaultConfig = 'DBDefaultConfig.xml'
renderHost = 'renderHost_masterV3_insgraf.conf'

CIGITaskConfig_tree = ET.parse(CIGITaskConfig)

for entity in CIGITaskConfig_tree.iter('Entity'):
    print (entity.attrib)
