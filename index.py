import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView
import keyboard

myappid = 'handlarz.duskview.browser.291020231608'
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Duskview(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Duskview, self).__init__(*args, **kwargs)

        self.setWindowTitle("Duskview Browser")
        self.setWindowIcon(QIcon("stuff/icon.png"))

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(25)

        self.go_btn = QPushButton("🔎")
        self.go_btn.setMinimumHeight(25)
        self.go_btn.setMaximumWidth(30)

        self.refresh_btn = QPushButton("⟳")
        self.refresh_btn.setMinimumHeight(25)
        self.refresh_btn.setMaximumWidth(30)

        self.next_btn = QPushButton("↻")
        self.next_btn.setMinimumHeight(25)
        self.next_btn.setMaximumWidth(30)

        self.back_btn = QPushButton("↺")
        self.back_btn.setMinimumHeight(25)
        self.back_btn.setMaximumWidth(30)

        self.settings_btn = QPushButton("⚙️")
        self.settings_btn.setMinimumHeight(25)
        self.settings_btn.setMaximumWidth(30)

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.next_btn)
        self.horizontal.addWidget(self.refresh_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        #self.horizontal.addWidget(self.settings_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(self.navigate)
        self.back_btn.clicked.connect(self.browser.back)
        self.next_btn.clicked.connect(self.browser.forward)
        self.refresh_btn.clicked.connect(self.browser.reload)

        self.browser.page().titleChanged.connect(self.update_window)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://searx.be/"))
        
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.url_bar.returnPressed.connect(self.navigate)

    def navigate(self):
        input_url = self.url_bar.text()
        
        if "." in input_url and not " " in input_url:
            if not input_url.startswith("http"):
                input_url = "https://" + input_url
        else:
            input_url = "http://searx.be/search?q=" + input_url + "&categories=general"
        self.browser.setUrl(QUrl(input_url))
        
    def update_window(self, title):
        self.setWindowTitle(f"{title} - Duskview Browser")

app = QApplication(sys.argv)
window = Duskview()
window.show()
sys.exit(app.exec())
