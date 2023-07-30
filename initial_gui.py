import sys
from PyQt6.QtWidgets import (
    QApplication, QLabel, QWidget, QMainWindow,
    QToolBar, QStatusBar, QVBoxLayout, QRadioButton, 
    QHBoxLayout, QPlainTextEdit, QPushButton
)

from PyQt6.QtCore import QRect, QSize, Qt
from PyQt6.QtGui import QMovie
from PyQt6 import QtCore

from commands import win_closing

WINDOW_SIZE: int = 500

class QtFrontWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Turtle AI Funny App Generator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.setCentralWidget(self.centralWidget)
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self._createGif()
        self._createTitleLabels()

        self._createHorizontalLayout()
        self._createRadioButton()
        self._createInputArea()
    
    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        # status.showMessage("I'm the status Bar")
        self.setStatusBar(status)
    
    def _createGif(self):
        self.gif = QLabel(self.centralWidget)
        self.gif.setGeometry(QRect(50, 10, 200, 200))
        self.gif.setMinimumSize(QSize(200, 200))
        self.gif.setMaximumSize(QSize(200, 200))

        self.movie = QMovie("./sprites/happy-turtle-transparent_med.gif")
        self.movie.setCacheMode(QMovie.CacheMode.CacheAll)
        self.gif.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()

    def _createTitleLabels(self):
        title = QLabel("<h1>Turtle AI</h1>", parent=self.centralWidget)
        title.move(180, 65) 
        
        subtitle = QLabel("<h2>Your friendly Turtle ChatGPT Chatbot </h2>", parent=self.centralWidget)
        subtitle.setWordWrap(True)
        subtitle.setGeometry(QRect(180, 105, 200, 50)) 

    def _createHorizontalLayout(self):
        self.hWidget = QWidget(self.centralWidget)
        self.hWidget.setGeometry(QRect(30,190,425,160))
        # self.hWidget.setStyleSheet("background-color: red")
        
        self.hLayout = QHBoxLayout()
        self.hWidget.setLayout(self.hLayout)
    
    def _createRadioButton(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(10)

        title = QLabel("<h4>Which API Model would you like?</h4>")
        title.setWordWrap(True)
        layout.addWidget(title)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        b1 = QRadioButton("GPT3")
        b1.setChecked(True)
        layout.addWidget(b1)
        b2 = QRadioButton("GPT4")
        layout.addWidget(b2)
        b3 = QRadioButton("Stable Diffusion")
        layout.addWidget(b3)

        widget.setLayout(layout)
        self.hLayout.addWidget(widget)

    def _createInputArea(self):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        layout.addWidget(QLabel("<h4>Enter your prompt..."))
        layout.addWidget(QPlainTextEdit())
        self.submitButton = QPushButton("Submit")
        layout.addWidget(self.submitButton)

        widget.setLayout(layout)
        self.hLayout.addWidget(widget)

    def setButtonCommand(self, function):
        self.submitButton.clicked.connect(lambda: function())

