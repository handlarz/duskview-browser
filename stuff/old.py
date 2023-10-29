from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class duskview(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(duskview, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("Duskview Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(25)

        self.go_btn = QPushButton("🔎")
        self.go_btn.setMinimumHeight(25)

        self.refresh_btn = QPushButton("⟳")
        self.refresh_btn.setMinimumHeight(25)

        self.next_btn = QPushButton("↻")
        self.next_btn.setMinimumHeight(25)

        self.back_btn = QPushButton("↺")
        self.back_btn.setMinimumHeight(25)

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.next_btn)
        self.horizontal.addWidget(self.refresh_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)

        durl = self.url_bar.toPlainText()

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: navigate(durl))
        self.back_btn.clicked.connect(self.browser.back)
        self.next_btn.clicked.connect(self.browser.forward)

        self.browser.page().titleChanged.connect(self.updateWindowTitle)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://searx.be/search?q=&categories=general"))
        
        self.window.setLayout(self.layout)
        self.window.show()

        def navigate(self, durl):
            if not durl.startswith("http"):
                durl = "https://"+durl
                self.browser.setUrl(QUrl(durl))

        def updateWindowTitle(self, title):
            self.setWindowTitle(f"{title} - Duskview")
            

app = QApplication([])
window = duskview()
app.exec_()