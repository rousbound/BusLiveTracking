from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from GUI import *
from GetBuses import *

class Main():

    def __init__(self):
        self.ui = Ui_MainWindow()
        self.mainWindow = QMainWindow()
        self.ui.setupUi(self.mainWindow)
        self.connect()

    def connect(self):
      self.ui.BusSearchButton.clicked.connect(self.Run)
      pass
  
    def Run(self):
      line = self.ui.BusLineEdit.text()
      buses = get_onibus(int(line))
      self.ui.BusLinesTextBrowser.setPlainText(buses)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.mainWindow.show()
    sys.exit(app.exec_())
