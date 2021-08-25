# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(441, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.horizontalLayout_4.addWidget(self.main_label)
        self.number_of_words = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.number_of_words.setFont(font)
        self.number_of_words.setObjectName("number_of_words")
        self.horizontalLayout_4.addWidget(self.number_of_words, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rand_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rand_label.setFont(font)
        self.rand_label.setObjectName("rand_label")
        self.horizontalLayout_7.addWidget(self.rand_label)
        self.random_w = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.random_w.setFont(font)
        self.random_w.setObjectName("random_w")
        self.horizontalLayout_7.addWidget(self.random_w, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.rand_label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rand_label_2.setFont(font)
        self.rand_label_2.setObjectName("rand_label_2")
        self.horizontalLayout_11.addWidget(self.rand_label_2)
        self.strike_main = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.strike_main.setFont(font)
        self.strike_main.setObjectName("strike_main")
        self.horizontalLayout_11.addWidget(self.strike_main, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.save_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/disk-black.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.save_button.setIcon(icon)
        self.save_button.setFlat(False)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_6.addWidget(self.save_button)
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.reset_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/arrow-circle-045-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon1)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout_6.addWidget(self.reset_button)
        self.pronunciation_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pronunciation_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/speaker-volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pronunciation_button.setIcon(icon2)
        self.pronunciation_button.setIconSize(QtCore.QSize(20, 22))
        self.pronunciation_button.setObjectName("pronunciation_button")
        self.horizontalLayout_6.addWidget(self.pronunciation_button)
        self.pronunciation_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.pronunciation_checkbox.setEnabled(True)
        self.pronunciation_checkbox.setText("")
        self.pronunciation_checkbox.setChecked(False)
        self.pronunciation_checkbox.setObjectName("pronunciation_checkbox")
        self.horizontalLayout_6.addWidget(self.pronunciation_checkbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(True)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.correctly_main = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.correctly_main.setFont(font)
        self.correctly_main.setObjectName("correctly_main")
        self.horizontalLayout_5.addWidget(self.correctly_main, 0, QtCore.Qt.AlignLeft)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.badly_main = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.badly_main.setFont(font)
        self.badly_main.setObjectName("badly_main")
        self.horizontalLayout_5.addWidget(self.badly_main)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.random_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.random_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/arrow-switch-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.random_button.setIcon(icon3)
        self.random_button.setObjectName("random_button")
        self.verticalLayout_2.addWidget(self.random_button)
        self.random_word = QtWidgets.QLabel(self.centralwidget)
        self.random_word.setEnabled(True)
        self.random_word.setMinimumSize(QtCore.QSize(0, 94))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.random_word.setFont(font)
        self.random_word.setWordWrap(False)
        self.random_word.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard)
        self.random_word.setObjectName("random_word")
        self.verticalLayout_2.addWidget(self.random_word, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbutton1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbutton1.setFont(font)
        self.cbutton1.setAutoDefault(False)
        self.cbutton1.setDefault(False)
        self.cbutton1.setFlat(False)
        self.cbutton1.setObjectName("cbutton1")
        self.horizontalLayout.addWidget(self.cbutton1)
        self.cbutton2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbutton2.setFont(font)
        self.cbutton2.setObjectName("cbutton2")
        self.horizontalLayout.addWidget(self.cbutton2)
        self.cbutton3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbutton3.setFont(font)
        self.cbutton3.setObjectName("cbutton3")
        self.horizontalLayout.addWidget(self.cbutton3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_c1 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_c1.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.edit_c1.setFont(font)
        self.edit_c1.setMouseTracking(False)
        self.edit_c1.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_c1.setObjectName("edit_c1")
        self.horizontalLayout_2.addWidget(self.edit_c1)
        self.edit_c2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_c2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.edit_c2.setFont(font)
        self.edit_c2.setMouseTracking(False)
        self.edit_c2.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_c2.setObjectName("edit_c2")
        self.horizontalLayout_2.addWidget(self.edit_c2)
        self.edit_c3 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_c3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.edit_c3.setFont(font)
        self.edit_c3.setMouseTracking(False)
        self.edit_c3.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_c3.setObjectName("edit_c3")
        self.horizontalLayout_2.addWidget(self.edit_c3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.correctly = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.correctly.setFont(font)
        self.correctly.setObjectName("correctly")
        self.horizontalLayout_9.addWidget(self.correctly, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.badly = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.badly.setFont(font)
        self.badly.setObjectName("badly")
        self.horizontalLayout_10.addWidget(self.badly, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.streak_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(True)
        self.streak_name.setFont(font)
        self.streak_name.setObjectName("streak_name")
        self.verticalLayout_5.addWidget(self.streak_name, 0, QtCore.Qt.AlignHCenter)
        self.streak_num = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(True)
        self.streak_num.setFont(font)
        self.streak_num.setObjectName("streak_num")
        self.verticalLayout_5.addWidget(self.streak_num, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.add_new_word = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_new_word.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_new_word.setIcon(icon4)
        self.add_new_word.setObjectName("add_new_word")
        self.horizontalLayout_8.addWidget(self.add_new_word, 0, QtCore.Qt.AlignLeft)
        self.save_word = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_word.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_word.setIcon(icon5)
        self.save_word.setObjectName("save_word")
        self.horizontalLayout_8.addWidget(self.save_word, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random Words"))
        self.main_label.setText(_translate("MainWindow", "Number of words:"))
        self.number_of_words.setText(_translate("MainWindow", "0"))
        self.rand_label.setText(_translate("MainWindow", "Random words:"))
        self.random_w.setText(_translate("MainWindow", "0"))
        self.rand_label_2.setText(_translate("MainWindow", "Win Streak:"))
        self.strike_main.setText(_translate("MainWindow", "0"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.pronunciation_button.setText(_translate("MainWindow", "Pronunciation"))
        self.groupBox.setTitle(_translate("MainWindow", "Summary"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:normal; color:#3ca32c;\">Correctly:</span></p></body></html>"))
        self.correctly_main.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3ca32c;\">0</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:400; font-style:normal; color:#991d1d;\">Badly:</span></p></body></html>"))
        self.badly_main.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#991d1d;\">0</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Summary"))
        self.random_button.setText(_translate("MainWindow", "random a word"))
        self.random_word.setText(_translate("MainWindow", "english random word"))
        self.cbutton1.setText(_translate("MainWindow", "word"))
        self.cbutton2.setText(_translate("MainWindow", "word"))
        self.cbutton3.setText(_translate("MainWindow", "word"))
        self.edit_c1.setText(_translate("MainWindow", "word"))
        self.edit_c2.setText(_translate("MainWindow", "word"))
        self.edit_c3.setText(_translate("MainWindow", "word"))
        self.groupBox_2.setTitle(_translate("MainWindow", "temporary scores"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#3ca32c;\">Correctly</span></p></body></html>"))
        self.correctly.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#991d1d;\">Badly</span></p></body></html>"))
        self.badly.setText(_translate("MainWindow", "0"))
        self.streak_name.setText(_translate("MainWindow", "Streak"))
        self.streak_num.setText(_translate("MainWindow", "0"))
        self.add_new_word.setText(_translate("MainWindow", "Add new word"))
        self.save_word.setText(_translate("MainWindow", "Save new word"))
