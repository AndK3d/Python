import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import xml.etree.ElementTree as ET


qtCreatorFile = "entity.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QDialog, Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.browse_folder_bt1.clicked.connect(self.browse_folder)
        self.initTreeView()

    def browse_folder(self):

        filename = QFileDialog.getOpenFileName(self, 'Open file','./', "XML files (*.xml)")

        if filename:
            self.CIGITaskConfig_path.setText(str(filename[0]))

            data = self.get_xml_entity_data(str(filename[0]))
            self.fill_tree_view(data)

        return

    def fill_tree_view(self, data):

        self.treeview.setModel(self.model)
        self.treeview.setColumnWidth(0, 150)
        self.treeview.setAlternatingRowColors(True)

        for entity in data:
            print ('fill_tree_view: entity = ',entity)
            self.get_child(entity)

        value = ["my_item1", "my_item2", "my_item3"]

        #self.item = QStandardItem("my_item1")
        #self.model.setItem(0, 2, self.item)
        '''
        i = 0
        for val in value:
            self.item = QStandardItem(val)
            self.model.setItem(i, 0, item)
            self.item.appendRow([QStandardItem("Child C"), None])
            i = i + 1
        
        self.treeview.setModel(model)
        self.treeview.setColumnWidth(0, 150)
        self.treeview.setAlternatingRowColors(True)
        '''

        return

    def add_row(self,parent,values=['default']):

        items_list = []

        #columns loop
        for val in values:
            item = QStandardItem(str(val))
            items_list.append(item)

        #resize columns count
        if self.model.columnCount() < len(items_list):
            self.model.setColumnCount(len(items_list))

        parent.appendRow(items_list)
        self.treeview.expandAll()
        return item

    def set_item(self,row,column,text='set_item_Default'):
        item = QStandardItem(text)
        self.model.setItem(row,column, item)

        return

    def initTreeView(self):
        self.model = QStandardItemModel(2,2)

        # init data
        self.itemCIGI = QStandardItem("CIGITaskConfig.xml")
        self.model.setItem(0, 0, self.itemCIGI)
        self.itemDB = QStandardItem("DBDefaultConfig.xml")
        self.model.setItem(1, 0, self.itemDB)
        self.itemRHost = QStandardItem("renderHost*.conf")
        self.model.setItem(2, 0, self.itemRHost)


        self.treeview.setModel(self.model)
        self.treeview.setColumnWidth(0, 150)
        self.treeview.setAlternatingRowColors(True)

        self.item_parent = self.model.findItems('CIGITaskConfig.xml')

        #self.add_row(self.item_parent[0],[1,2,3,4,5])



        return


    def get_xml_entity_data(self,xml_filename):

        xml_tree = ET.parse(xml_filename)
        entity_tree = xml_tree.findall('Entity')

        return entity_tree


    def get_child_backup(self, value, parent = None ):

        if not parent:
            root = self.model.findItems('CIGITaskConfig.xml')
            parent = root[0]
            print ('true',' Parent=',parent)
        else:
            print ('false',' Parent=',parent)

        p_item = self.add_row(parent, [value.tag])

        #loop in XML child nodes
        for child in value:
            print ('-child =', child)
            p_item = self.add_row(p_item, [child.tag])
            #loop in XML parameters
            for key in child.attrib:
                print('  *key =', key)
                self.add_row(p_item, [key, child.attrib[key]])



        '''
        for key in value.attrib:

            self.add_row(parent,[key,value.attrib[key]])
        for i in range(0, len(value)):
            self.get_child(value[i],parent)
        '''

    def get_child(self, value, parent = None ):

        if not parent:
            root = self.model.findItems('CIGITaskConfig.xml')
            parent = root[0]
            print ('true',' Parent=',parent)
        else:
            print ('false',' Parent=',parent)

        # add TAG of XML node
        p_item = self.add_row(parent, [value.tag])
         # add parameters of node
        for key in value.attrib:
            print('  *key =', [key, value.attrib[key]])
            c_item = self.add_row(p_item, [key, value.attrib[key]])

        for child in value:
            print('_______________', child.tag)
            self.get_child(child,c_item)

        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


