import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        backButton = QAction('<', self)
        backButton.triggered.connect(self.browser.back)
        navbar.addAction(backButton)
        forwardButton = QAction('>', self)
        forwardButton.triggered.connect(self.browser.forward)
        navbar.addAction(forwardButton)
        reloadButton = QAction('↻', self)
        reloadButton.triggered.connect(self.browser.reload)
        navbar.addAction(reloadButton)

        homeButton = QAction('⌂', self)
        homeButton.triggered.connect(self.navigateHome)
        navbar.addAction(homeButton)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigateToUrl)
        navbar.addWidget(self.urlBar)

        self.browser.urlChanged.connect(self.updateUrl)

    def navigateHome(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navigateToUrl(self):
        url = self.urlBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, url):
        self.urlBar.setText(url.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("mayb-rowser")
window = MainWindow()
app.exec_()