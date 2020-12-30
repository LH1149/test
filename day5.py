# 对话框：对话框或对话窗口是现代GUI程序不可或缺的一部分。对话的定义是两个或多个人之间的交谈。
# 在计算机程序中对话是与程序进行“交谈”的窗体。对话框用于输入数据、修改数据、更改程序设置等。

# # 1、QInputDialog提供了从用户取得一个输入的简便对话框。输入的值可以是字符串、数字或列表中的一项。
# # 这个例子中有一个按钮和一个LineEdit控件。按钮用于显示对话框以取得用户输入。输入的文本会显示在LineEdit控件中。
# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.btn = QPushButton("Dialog", self)
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog)

#         self.le = QLineEdit(self)
#         self.le.move(130, 22)

#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle("Input dialog")
#         self.show()

#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
#         # # 这行代码用于显示QInputDialog对话框。第一个字符串参数是对话框的标题，第二个是对话框中的消息。
#         # QInputDialog.getText方法会返回用户输入的文本和一个布尔值。当点击OK按钮时，这个布尔值为true。
#         if ok:
#             self.le.setText(str(text))
#         # 从对话框中取得的文本会显示在LineEdit控件上。


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())





# # QColorDialog提供了一个用于选择颜色值的对话框。
# # 示例展示了一个按钮和一个QFrame。QFrame控件的背景设置为黑色。使用QColorDialog我们可以改变它的背景色。
# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
# from PyQt5.QtGui import QColor


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         col = QColor(0, 255, 0) 
#         # 这是QtGui.QFrame的初始背景颜色。 三个参数分别为red,green,blue数值为0~255

#         self.btn = QPushButton("Dialog", self)
#         self.btn.move(20, 20)
        

#         self.btn.clicked.connect(self.showDialog)

#         self.frm = QFrame(self)
#         self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
#         self.frm.setGeometry(130, 22, 100, 100)

#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle("Color dialog")
#         self.show()

#     def showDialog(self):
#         col = QColorDialog.getColor()
#         # 这行代码会弹出QColorDialog对话框。
#         if col.isValid():
#             self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
#             # 我们要先检查col的值。如果点击的是Cancel按钮，返回的颜色值是无效的。当颜色值有效时，我们通过样式表(style sheet)来改变背景颜色。


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())





# # QFontDialog是一个用于选择字体的对话框控件。
# # 在这个例子中，我们创建了一个按钮和一个标签(Label)，并通过QFontDialog来改变标签的字体。
# import sys
# from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
#                              QSizePolicy, QLabel, QFontDialog, QApplication)


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         vbox = QVBoxLayout()

#         btn = QPushButton("Dialog", self)
#         btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         btn.move(20, 20)

#         vbox.addWidget(btn)

#         btn.clicked.connect(self.showDialog)

#         self.lb1 = QLabel("Studying makes me happy？扯淡呢", self)
#         self.lb1.move(130,20)

#         vbox.addWidget(self.lb1)
#         self.setLayout(vbox)

#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle("Font dialog")
#         self.show()

#     def showDialog(self):
#         font, ok = QFontDialog.getFont()
#         # 这段代码会弹出字体选择对话框。getFont()方法会返回选定的字体名称和一个ok参数。当点击了OK按钮时ok的值为True，否则为False。
#         if ok:
#             self.lb1.setFont(font)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())






# QFileDialog是一个让用户选择文件或目录的对话框。可用于选择打开或保存文件。
# 这个例子展示了一个菜单栏，中部TextEdit控件和一个状态栏。
# 菜单项Open会显示用于选择文件的QtGui.QFileDialog对话框。选定文件的内容会加载到TextEdit控件中。
import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    # 示例窗体继承自QMainWindow，因为我们要将TextEdit控件置于窗体中央。

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon("D:/CSR/wallpaper/1.jpg"), "Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open new File")
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("File dialog")
        self.setWindowIcon(QIcon("D:/CSR/wallpaper/2.jpg"))
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open file", "/home")
        # 这时会弹出QFileDialog对话框。第一个字符串参数是对话框的标题。第二个指定对话框的工作目录。默认情况下文件筛选器会匹配所有类型的文件(*)
        if fname[0]:
            f = open(fname[0], "r")

            with f:
                data = f.read()
                self.textEdit.setText(data)
                # 读取了选择的文件名称并将文件内容加载到了TextEdit控件。


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())