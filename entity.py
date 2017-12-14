import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QAbstractItemModel, QFile, QIODevice, QModelIndex, Qt
from PyQt5.QtQuick import QQuickView
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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
        self.initTable()
        self.initTreeView()

    def browse_folder(self):

        filename = QFileDialog.getOpenFileName(self, 'Open file','./', "XML files (*.xml)")

        if filename:
            self.CIGITaskConfig_path.setText(str(filename[0]))

            data = self.get_xml_entity_data(str(filename[0]))
            self.fill_table(data)

            data = self.get_xml_entity_data(str(filename[0]))
            self.fill_tree_view(data)

            print("point")
        return

    def fill_tree_view(self, data):

        self.treeview.setModel(self.model)
        self.treeview.setColumnWidth(0, 150)
        self.treeview.setAlternatingRowColors(True)

        for en in data:
            #print (en)
            self.get_child(en)

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

    def add_row(self,parent,text='Empty'):

        item = QStandardItem(text)
        parent.appendRow([item, None])

        return

    def initTreeView(self):
        self.model = QStandardItemModel()

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

        self.item_test = self.model.findItems('CIGITaskConfig.xml')

        self.add_row(self.item_test[0])


        return

    def initTable(self):

        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)

        hheader = self.tableWidget.horizontalHeader()

        hheader.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        hheader.setSectionResizeMode(1, QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget.setHorizontalHeaderLabels(['Type', 'Name'])

    def get_xml_entity_data(self,xml_filename):

        xml_tree = ET.parse(xml_filename)
        entity_tree = xml_tree.findall('Entity')
        return entity_tree

    def fill_table(self,data):

        i = 0
        for row in data:
            self.tableWidget.setRowCount(i+1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row.attrib['Type']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(row.attrib['Name']))
            i = i + 1
        return

    def get_child(self, parent):

        #print(parent.tag, parent.attrib)

        #self.prnt = self.model.findItems(parent)
        #self.itemCIGI = QStandardItem(parent.attrib)
        #self.add_row(self.itemCIGI)

        for key in parent.attrib:
            print(key, ' = ', parent.attrib[key])

            self.parent_item = self.model.findItems('CIGITaskConfig.xml')
            print (self.parent_item)
            self.add_row(self.parent_item)

        for i in range(0, len(parent)):
            self.get_child(parent[i])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


