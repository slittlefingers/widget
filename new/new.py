# from PySide6.QtWidgets import QApplication, QWidget , QMainWindow ,  QPushButton
# # Only needed for access to command line arguments
# import sys
# from PySide6.QtCore import QSize, Qt
# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([])
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__() 
#         self.setWindowTitle("My App")
#         self.button = QPushButton("Press Me!")
#         self.button_is_checked = True
#         # Set the central widget of the Window.
#         self.setFixedSize(QSize(400, 300))
#         self.button.setCheckable(True)
#         self.button.clicked.connect(self.the_button_was_clicked)
#         self.button.clicked.connect(self.the_button_was_toggled)
#         self.button.released.connect(self.the_button_was_released) 
#         self.button.setCheckable(self.button_is_checked)
#         self.setCentralWidget(self.button) 
    
#     def the_button_was_clicked(self):
#         print("Clicked!")
    
#     def the_button_was_toggled(self, checked):
#         self.button_is_checked=checked
#         print(self.button_is_checked)
    
#     def the_button_was_released(self):
#         self.button_is_checked = self.button.isChecked() 
#         print(self.button_is_checked)

# app = QApplication(sys.argv)
# # Create a Qt widget, which will be our window.
# window = MainWindow()
# window.show() # IMPORTANT!!!!! Windows are hidden by default.
# # Start the event loop.
# app.exec()
# # Your application won't reach here until you exit and the event
# # loop has stopped.

# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys
# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     self.button = QPushButton("Press Me!") 
#     self.button.clicked.connect(self.the_button_was_clicked)
#     # Set the central widget of the Window.
#     self.setCentralWidget(self.button)
#   def the_button_was_clicked(self):
#     self.button.setText("You already clicked me.") 
#     self.button.setEnabled(False) 
#     # Also change the window title.
#     self.setWindowTitle("My Oneshot App")
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys
# from random import choice
# window_titles = [ 
#   'My App',
#   'My App',
#   'Still My App',
#   'Still My App',
#   'What on earth',
#   'What on earth',
#   'This is surprising',
#   'This is surprising',
#   'Something went wrong'
# ]

# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.n_times_clicked = 0
#     self.setWindowTitle("My App")
#     self.button = QPushButton("Press Me!")
#     self.button.clicked.connect(self.the_button_was_clicked)
#     self.windowTitleChanged.connect(self.the_window_title_changed)

#     # Set the central widget of the Window.
#     self.setCentralWidget(self.button)
#   def the_button_was_clicked(self):
#     print("Clicked.")
#     new_window_title = choice(window_titles)
#     print("Setting title: %s" % new_window_title)
#     self.setWindowTitle(new_window_title) 
#   def the_window_title_changed(self, window_title):
#     print("Window title changed: %s" % window_title) 
#     if window_title == 'Something went wrong':
#      self.button.setDisabled(True)
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

# from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QLineEdit, QVBoxLayout, QWidget,QCheckBox
# from PySide6.QtCore import Qt
# import sys
# class MainWindow(QMainWindow):
#   def __init__(self):
#   #   super().__init__()
#   #   self.setWindowTitle("My App")
#   #   self.label = QLabel("hello")
#   #   self.label.setText("w")
#   #   self.input = QLineEdit()
#   #   self.Qcheckbox=QCheckBox()
#   #   self.input.textChanged.connect(self.label.setText) 
#   #   layout = QVBoxLayout() 
#   #   layout.addWidget(self.input)
#   #   layout.addWidget(self.label)
#   #   layout.addWidget(self.Qcheckbox)
#   #   container = QWidget()
#   #   container.setLayout(layout)
#   # # Set the central widget of the Window.
#   #   self.setCentralWidget(container)
#     super().__init__()

#     self.setWindowTitle("My App")
#     widget = QLabel("Hello")
#     font = widget.font() 
#     font.setPointSize(30)
#     widget.setFont(font)
#     widget.setAlignment(Qt.AlignLeft | Qt.AlignRight) 
#     self.setCentralWidget(widget)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

# import sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow
# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     widget = QCheckBox("This is a checkbox")
#     widget.setCheckState(Qt.Unchecked)
#     # For tristate: widget.setCheckState(Qt.PartiallyChecked)
#     # Or: widget.setTristate(True)
#     widget.stateChanged.connect(self.show_state)
#     self.setCentralWidget(widget)
#   def show_state(self, s):
#     print(s == Qt.Checked)
#     print(s)
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
# import sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow
# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     widget = QComboBox()
#     widget.addItems(["One", "Two", "Three"])
#     widget.setEditable(True)
#     widget.setInsertPolicy(QComboBox.InsertAtTop)
  

#     widget.currentIndexChanged.connect(self.index_changed)
#     widget.currentTextChanged.connect(self.text_changed)
#     self.setCentralWidget(widget)
#   def index_changed(self, i): # i is an int
#     print(i)
#   def text_changed(self, s): # s is a str
#     print(s)
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec() 
# import sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     widget = QSpinBox()
#     # Or: widget = QDoubleSpinBox()
#     widget.setMinimum(-10)
#     widget.setMaximum(3)
#     # Or: widget.setRange(-10,3)
#     widget.setPrefix("$")
#     widget.setSuffix("c")
#     widget.setSingleStep(3) # Or e.g. 0.5 for QDoubleSpinBox
#     widget.valueChanged.connect(self.value_changed)
#     widget.textChanged.connect(self.value_changed_str)
#     self.setCentralWidget(widget)
#   def value_changed(self, i):
#     print(i)
#   def value_changed_str(self, s):
#     print(s)
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
# import sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     widget = QSlider()
#     widget.setMinimum(-10)
#     widget.setMaximum(3)
#     # Or: widget.setRange(-10,3)
#     widget.setSingleStep(3)
#     widget.valueChanged.connect(self.value_changed)
#     widget.sliderMoved.connect(self.slider_position)
#     widget.sliderPressed.connect(self.slider_pressed)
#     widget.sliderReleased.connect(self.slider_released)
#     self.setCentralWidget(widget)
#   def value_changed(self, i):
#     print(i)
#   def slider_position(self, p):
#     print("position", p)
#   def slider_pressed(self):
#     print("Pressed!")
#   def slider_released(self):
#     print("Released")
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

# import sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QDial, QMainWindow
# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     widget = QDial()
#     widget.setRange(-10, 100)
#     widget.setSingleStep(1)
#     widget.valueChanged.connect(self.value_changed)
#     widget.sliderMoved.connect(self.slider_position)
#     widget.sliderPressed.connect(self.slider_pressed)
#     widget.sliderReleased.connect(self.slider_released)
#     self.setCentralWidget(widget)
#   def value_changed(self, i):
#     print(i)
#   def slider_position(self, p):
#     print("position", p)
#   def slider_pressed(self):
#     print("Pressed!")
#   def slider_released(self):
#     print("Released")
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget
class Color(QWidget):
  def __init__(self, color):
    super().__init__()
    self.setAutoFillBackground(True)
    palette = self.palette()
    palette.setColor(QPalette.Window, QColor(color))
    self.setPalette(palette)

# import sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QMainWindow
# # from layout_colorwidget import Color
# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     widget = Color("red")
#     self.setCentralWidget(widget)
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
# import sys
# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import (
#   QApplication,
#   QHBoxLayout,
#   QLabel,
#   QMainWindow,
#   QVBoxLayout,
#   QWidget,
# )

# class MainWindow(QMainWindow):
#   def __init__(self):
#     super().__init__()
#     self.setWindowTitle("My App")
#     # layout1 = QHBoxLayout()
#     # layout2 = QVBoxLayout()
#     # layout3 = QVBoxLayout()
#     # layout1.setContentsMargins(0, 0, 0, 0)
#     # layout1.setSpacing(0)
#     # layout2.addWidget(Color("red"))
#     # layout2.addWidget(Color("yellow"))
#     # layout2.addWidget(Color("purple"))
#     # layout1.addLayout(layout2)
#     # layout1.addWidget(Color("green"))
#     # layout3.addWidget(Color("red"))
#     # layout3.addWidget(Color("purple"))
#     # layout1.addLayout(layout3)
#     widget = QWidget()
#     # widget.setLayout(layout1)
#     # widget.setAttribute(Qt.WA_TranslucentBackground)
#     # widget.setWindowOpacity(0.5)
    
#     self.setCentralWidget(widget)
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtCore import Qt

# app = QApplication([])

# widget = QWidget()

# # 让窗口背景半透明
# widget.setStyleSheet("background-color:rgba(0,0,0,127);")

# # 去掉窗口边框
# widget.setWindowFlags(Qt.FramelessWindowHint)

# widget.show()

# app.exec_()
# importing the required libraries
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys
  
  
# class Window(QMainWindow):
  
  
    # def __init__(self):
    #     super().__init__()
  
  
    #     # set the title
    #     self.setWindowTitle("Python")
  
    #     self.setWindowOpacity(0.1)
  
  
    #     # setting  the geometry of window
    #     self.setGeometry(60, 100, 600, 400)
  
    #     # creating a label widget
    #     self.label_1 = QLabel("transparent ", self)
    #     # moving position
    #     self.label_1.move(100, 100)
  
    #     self.label_1.adjustSize()
    #     self.setWindowFlags(Qt.FramelessWindowHint)
  
    #     # show all the widgets
    #     self.show()
  
  
# # create pyqt5 app
# App = QApplication(sys.argv)
  
# # create the instance of our Window
# window = Window()
# window.show()  
# # start the app
# sys.exit(App.exec())
# first we need a window 
# this window is a class which herit the QMainWindow
# super.init() self.setWindowTitle
# we need a app to run this system
# so we create app=QApplication(sys.argv)
# window=MainWindow()
# window.show()
# app.exec()
class Color(QWidget):
  def __init__(self, color):
    super().__init__()
    self.setAutoFillBackground(True)
    palette = self.palette()
    palette.setColor(QPalette.Window, QColor(color))
    self.setPalette(palette)
  # override the qdialog
class CustomDialog(QDialog):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("HELLO!")
    # it is the same as the hello
    # QDialogButton.OK there is two button in here
    # buttonbox connect to correct signal
    buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    self.buttonBox = QDialogButtonBox(buttons)
    self.buttonBox.accepted.connect(self.accept)
    self.buttonBox.rejected.connect(self.reject)
    self.layout = QVBoxLayout()
    message = QLabel("Something happened, is that OK?")
    self.layout.addWidget(message)
    self.layout.addWidget(self.buttonBox)
    self.setLayout(self.layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # if we want change the window attribute itself it will change the attribute
    self.setWindowTitle("super")
    # layout=QVBoxLayout()
    # layouts1=QHBoxLayout()
    # you can also change to v
    # but Qgrid is more effective
    # if you want to let the widget overlap each other
    # layout = QStackedLayout()
    # layout.addWidget(Color("red"))
    # layout.addWidget(Color("green"))
    # layout.addWidget(Color("blue"))
    # layout.addWidget(Color("yellow"))
    # layout.setCurrentIndex(3)

    # # layout = QGridLayout()
    # # layout.addWidget(Color("red"), 0, 0)
    # # layout.addWidget(Color("green"), 1, 0)
    # # layout.addWidget(Color("blue"), 1, 1)
    # # layout.addWidget(Color("purple"), 2, 1)
    # # layout.addWidget(Color("red"))
    # # layout.addWidget(Color("green"))
    # # layout.addWidget(Color("blue"))
    # # if you want to add more complex layout, you can add layout on the orignal layout
    # # widget is a part of the window
    # # first we can make it a instance
    # # in the layout, there also have a lot of attributes, 
    # layout.setContentsMargins(0,0,0,0)
    # layout.setSpacing(0)
    # # layout.addLayout(layouts1)
    # # layouts1.addWidget(Color("purple"))
    # # layouts1.addWidget(Color("red"))
    # widget1=QWidget()
    # widget1.setLayout(layout)
    # # if you want to change the attribute
    # # you need use the set function some times there are some class inside the class
    # self.setCentralWidget(widget1)
    # if you want add more than one widget, you should add layout on the widget
    # layout is kind of like a net it will seperate the widget to diffenent part
  #   pagelayout = QVBoxLayout()
  #   button_layout = QHBoxLayout()
  #   self.stacklayout = QStackedLayout()
  #   pagelayout.addLayout(button_layout)
  #   pagelayout.addLayout(self.stacklayout)
  #   btn = QPushButton("red")
  #   btn.pressed.connect(self.activate_tab_1)
  #   button_layout.addWidget(btn)
  #   self.stacklayout.addWidget(Color("red"))
  #   btn = QPushButton("green")
  #   btn.pressed.connect(self.activate_tab_2)
  #   button_layout.addWidget(btn)
  #   self.stacklayout.addWidget(Color("green"))
  #   btn = QPushButton("yellow")
  #   btn.pressed.connect(self.activate_tab_3)
  #   button_layout.addWidget(btn)
  #   self.stacklayout.addWidget(Color("yellow"))
  #   widget = QWidget()
  #   widget.setLayout(pagelayout)
  #   self.setCentralWidget(widget)
  # def activate_tab_1(self):
  #   self.stacklayout.setCurrentIndex(0)
  # def activate_tab_2(self):
  #   self.stacklayout.setCurrentIndex(1)
  # def activate_tab_3(self):
  # this is through setcurrentindex to fix the problem
  # Qt have assemble this function to a new type of widget
    # tabs = QTabWidget()
    # tabs.setTabPosition(QTabWidget.West)
    # tabs.setMovable(True)
    # for n, color in enumerate(["red", "green", "blue", "yellow"]):
    #   tabs.addTab(Color(color), color)
    # self.setCentralWidget(tabs)

  #   label = QLabel("Hello!")
  #   label.setAlignment(Qt.AlignCenter)
  #   self.setCentralWidget(label)
  #   # create toolbar instance
  #   toolbar = QToolBar("My main toolbar")
  #   # add toolbar to the window
  #   self.addToolBar(toolbar)
  #   # add an action called button set checkable and status
  #   button_action = QAction(QIcon("acorn.png"), "&Your button", self)
  #   toolbar.setIconSize(QSize(16, 16))
  #   button_action.setCheckable(True)
  #   button_action.setStatusTip("This is your button")
  #   button_action.setShortcut(QKeySequence("Ctrl+p"))
  #   # add triggered connect the function
  #   button_action.triggered.connect(self.onMyToolBarButtonClick)
  #   # add action to tool bar
  #   toolbar.addAction(button_action)
  #   # toolbar.addSeparator()
  #   button_action2 = QAction(QIcon("android.png"), "&Your button2",self)
  #   button_action2.setStatusTip("This is your button2")
  #   button_action2.triggered.connect(self.onMyToolBarButtonClick)
  #   button_action2.setCheckable(True)
  #   # toolbar.addAction(button_action2)
  #   # toolbar.addWidget(QLabel("Hello"))
  #   # toolbar.addWidget(QCheckBox())
  #   # add statusBar
  #   self.setStatusBar(QStatusBar(self))
  #   menu = self.menuBar()
  #   file_menu = menu.addMenu("&File")
  #   # we can add menu here it is like layout and widget toolbar
  #   file_menu.addAction(button_action)
  #   file_menu.addSeparator()
  #   file_menu.addAction(button_action2)

  # def onMyToolBarButtonClick(self, s):
  #   print("click", s)

  # dialog
    button = QPushButton("Press me for a dialog!")
    button.clicked.connect(self.button_clicked)
    self.setCentralWidget(button)
  def button_clicked(self, s):
    # dlg = QDialog(self)
    # dlg.setWindowTitle("?")
    # dlg.exec()
    # print("click", s)
    # dlg = CustomDialog()
    # if dlg.exec():
    #   print("Success!")
    # else:
    #   print("Cancel!")
    # use another component Qmessage box title text button Qessage box itself contain a lot of  state like warning quesion infromation
    dlg = QMessageBox(self)
    dlg.setWindowTitle("I have a question!")
    dlg.setText("This is a question dialog")
    # QMessageBox has two button yes and no
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setIcon(QMessageBox.Question)
    button = dlg.exec()
    if button == QMessageBox.Yes:
      print("Yes!")
    else:e
      print("No!")


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()

