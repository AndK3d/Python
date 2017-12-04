import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog


qtCreatorFile = "entity.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QDialog, Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.browse_folder_bt1.clicked.connect(self.browse_folder)

    def browse_folder(self):
        #print ('booo!!!')

        filename = QFileDialog.getOpenFileName(self, 'Open file',
                                    './', "Image files (*.xml)")

        if filename:
            print (filename)
            self.CIGITaskConfig_path.setText(str(filename))

        return



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


