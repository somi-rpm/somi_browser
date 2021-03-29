from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # ToolBar
        navbar = QToolBar()
        self.addToolBar(navbar)

        bk_btn = QAction("Back", self)
        bk_btn.triggered.connect(self.browser.back)
        navbar.addAction(bk_btn)

        fwd_btn = QAction("Forward", self)
        fwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fwd_btn)

        refresh_btn = QAction("Reload", self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.NavHome)
        navbar.addAction(home_btn)

        self.UrlBar = QLineEdit()
        self.UrlBar.returnPressed.connect(self.NavToUrl)
        navbar.addWidget(self.UrlBar)

        self.browser.urlChanged.connect(self.UpdtUrl)

    def NavHome(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def NavToUrl(self):
        url = self.UrlBar.text()
        self.browser.setUrl(QUrl(url))

    def UpdtUrl(self, q):
        self.UrlBar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Somi browser")
window = MainWindow()
app.exec()