#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:56:09 2019

@author: pascpeli
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

#!/usr/bin/env python3

import os
import sys
import subprocess
#from threading import Thread
from FileEditClass import FileEdit
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import QTimer
#from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import icons_rc
#import twisted



class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 636)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/syncplay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.syncplay_version_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.syncplay_version_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.syncplay_version_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.syncplay_version_label_2.setText("")
        self.syncplay_version_label_2.setPixmap(QtGui.QPixmap(":/icons/syncplay.png"))
        self.syncplay_version_label_2.setObjectName("syncplay_version_label_2")
        self.horizontalLayout_1.addWidget(self.syncplay_version_label_2)
        self.syncplay_version_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.syncplay_version_label.setFont(font)
        self.syncplay_version_label.setObjectName("syncplay_version_label")
        self.horizontalLayout_1.addWidget(self.syncplay_version_label)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setMaximumSize(QtCore.QSize(50, 50))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.horizontalLayout_1.addWidget(self.commandLinkButton)
        self.verticalLayout_1.addLayout(self.horizontalLayout_1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem)
        self.serverSettings_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.serverSettings_groupBox.setObjectName("serverSettings_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.serverSettings_groupBox)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.server_label = QtWidgets.QLabel(self.serverSettings_groupBox)
        self.server_label.setMinimumSize(QtCore.QSize(110, 22))
        self.server_label.setMaximumSize(QtCore.QSize(110, 30))
        self.server_label.setAlignment(QtCore.Qt.AlignCenter)
        self.server_label.setObjectName("server_label")
        self.horizontalLayout_7.addWidget(self.server_label)
        self.server_comboBox = QtWidgets.QComboBox(self.serverSettings_groupBox)
        self.server_comboBox.setMinimumSize(QtCore.QSize(120, 30))
        self.server_comboBox.setObjectName("server_comboBox")
        self.server_comboBox.addItem("")
        self.server_comboBox.addItem("")
        self.server_comboBox.addItem("")
        self.server_comboBox.addItem("")
        self.server_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.server_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.password_label = QtWidgets.QLabel(self.serverSettings_groupBox)
        self.password_label.setMinimumSize(QtCore.QSize(110, 22))
        self.password_label.setMaximumSize(QtCore.QSize(110, 30))
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_8.addWidget(self.password_label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.serverSettings_groupBox)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_8.addWidget(self.password_lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.username_label = QtWidgets.QLabel(self.serverSettings_groupBox)
        self.username_label.setMinimumSize(QtCore.QSize(110, 22))
        self.username_label.setMaximumSize(QtCore.QSize(110, 30))
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.horizontalLayout_9.addWidget(self.username_label)
        self.username_lineEdit = QtWidgets.QLineEdit(self.serverSettings_groupBox)
        self.username_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.username_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout_9.addWidget(self.username_lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.room_name_label = QtWidgets.QLabel(self.serverSettings_groupBox)
        self.room_name_label.setMinimumSize(QtCore.QSize(110, 22))
        self.room_name_label.setMaximumSize(QtCore.QSize(110, 30))
        self.room_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.room_name_label.setObjectName("room_name_label")
        self.horizontalLayout_16.addWidget(self.room_name_label)
        self.room_name_lineEdit = QtWidgets.QLineEdit(self.serverSettings_groupBox)
        self.room_name_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.room_name_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.room_name_lineEdit.setObjectName("room_name_lineEdit")
        self.horizontalLayout_16.addWidget(self.room_name_lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.verticalLayout_1.addWidget(self.serverSettings_groupBox)
        self.playerSettings_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.playerSettings_groupBox.setObjectName("playerSettings_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.playerSettings_groupBox)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.file_path_label = QtWidgets.QLabel(self.playerSettings_groupBox)
        self.file_path_label.setMinimumSize(QtCore.QSize(110, 22))
        self.file_path_label.setMaximumSize(QtCore.QSize(110, 30))
        self.file_path_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_path_label.setObjectName("file_path_label")
        self.horizontalLayout_6.addWidget(self.file_path_label)
        self.file_path_toolButton = QtWidgets.QToolButton(self.playerSettings_groupBox)
        self.file_path_toolButton.setMinimumSize(QtCore.QSize(25, 25))
        self.file_path_toolButton.setMaximumSize(QtCore.QSize(25, 25))
        self.file_path_toolButton.setObjectName("file_path_toolButton")
        self.horizontalLayout_6.addWidget(self.file_path_toolButton)
        self.file_path_lineEdit = FileEdit(self.playerSettings_groupBox,('.mp4','.mkv','.avi','.flv'))
        self.file_path_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.file_path_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.file_path_lineEdit.setObjectName("file_path_lineEdit")
        self.horizontalLayout_6.addWidget(self.file_path_lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.player_path_label = QtWidgets.QLabel(self.playerSettings_groupBox)
        self.player_path_label.setMinimumSize(QtCore.QSize(110, 22))
        self.player_path_label.setMaximumSize(QtCore.QSize(110, 30))
        self.player_path_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_path_label.setObjectName("player_path_label")
        self.horizontalLayout_5.addWidget(self.player_path_label)
        self.player_comboBox = QtWidgets.QComboBox(self.playerSettings_groupBox)
        self.player_comboBox.setMinimumSize(QtCore.QSize(120, 30))
        self.player_comboBox.setMaxVisibleItems(13)
        self.player_comboBox.setObjectName("player_comboBox")
        self.player_comboBox.addItem("")
        self.player_comboBox.addItem("")
        self.player_comboBox.addItem("")
        self.player_comboBox.addItem("")
        self.player_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.player_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_1.addWidget(self.playerSettings_groupBox)
        self.otherSettings_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.otherSettings_groupBox.setObjectName("otherSettings_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.otherSettings_groupBox)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.voicecall_app_label = QtWidgets.QLabel(self.otherSettings_groupBox)
        self.voicecall_app_label.setMinimumSize(QtCore.QSize(110, 22))
        self.voicecall_app_label.setMaximumSize(QtCore.QSize(110, 30))
        self.voicecall_app_label.setAlignment(QtCore.Qt.AlignCenter)
        self.voicecall_app_label.setObjectName("voicecall_app_label")
        self.horizontalLayout_4.addWidget(self.voicecall_app_label)
        self.voicecall_app_which_toolButton = QtWidgets.QToolButton(self.otherSettings_groupBox)
        self.voicecall_app_which_toolButton.setMinimumSize(QtCore.QSize(25, 25))
        self.voicecall_app_which_toolButton.setMaximumSize(QtCore.QSize(25, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/index.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.voicecall_app_which_toolButton.setIcon(icon1)
        self.voicecall_app_which_toolButton.setObjectName("voicecall_app_which_toolButton")
        self.horizontalLayout_4.addWidget(self.voicecall_app_which_toolButton)
        self.voicecall_app_lineEdit = QtWidgets.QLineEdit(self.otherSettings_groupBox)
        self.voicecall_app_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.voicecall_app_lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.voicecall_app_lineEdit.setObjectName("voicecall_app_lineEdit")
        self.horizontalLayout_4.addWidget(self.voicecall_app_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.voicecall_app_checkBox = QtWidgets.QCheckBox(self.otherSettings_groupBox)
        self.voicecall_app_checkBox.setObjectName("voicecall_app_checkBox")
        self.verticalLayout_2.addWidget(self.voicecall_app_checkBox)
        self.verticalLayout_1.addWidget(self.otherSettings_groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout_2.addWidget(self.start_pushButton)
        self.close_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout_2.addWidget(self.close_pushButton)
        self.verticalLayout_1.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.syncplay_version_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.syncplay_version_label_5.setMinimumSize(QtCore.QSize(110, 20))
        self.syncplay_version_label_5.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.syncplay_version_label_5.setFont(font)
        self.syncplay_version_label_5.setObjectName("syncplay_version_label_5")
        self.horizontalLayout_3.addWidget(self.syncplay_version_label_5)
        self.syncplay_version_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.syncplay_version_label_4.setMinimumSize(QtCore.QSize(20, 20))
        self.syncplay_version_label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.syncplay_version_label_4.setText("")
        self.syncplay_version_label_4.setPixmap(QtGui.QPixmap(":/icons/PP_trans.ico"))
        self.syncplay_version_label_4.setObjectName("syncplay_version_label_4")
        self.horizontalLayout_3.addWidget(self.syncplay_version_label_4)
        self.verticalLayout_1.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 28))
        self.menubar.setObjectName("menubar")
        self.menuUpdate = QtWidgets.QMenu(self.menubar)
        self.menuUpdate.setObjectName("menuUpdate")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_Configuration = QtWidgets.QAction(MainWindow)
        self.actionSave_Configuration.setObjectName("actionSave_Configuration")
        self.actionLoad_Configuration = QtWidgets.QAction(MainWindow)
        self.actionLoad_Configuration.setObjectName("actionLoad_Configuration")
        self.menuUpdate.addAction(self.actionSave_Configuration)
        self.menuUpdate.addAction(self.actionLoad_Configuration)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuUpdate.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.start_pushButton.clicked.connect(self.startButton_func)
        self.close_pushButton.clicked.connect(self.closeButton_func)
        self.file_path_toolButton.clicked.connect(self.file_path_Button_func)
        self.actionSave_Configuration.triggered.connect(self.save_config)
        self.actionLoad_Configuration.triggered.connect(self.load_config)
        self.actionAbout.triggered.connect(self.aboutdialog_show)

        self.retranslateUi(MainWindow)

        self.init_values()
        self.outputTimer = QtCore.QTimer(self)
        self.outputTimer.setInterval(500) #.5 seconds
        self.outputTimer.timeout.connect(self.update_output)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        self.version = subprocess.Popen( ['syncplay','-v'], stdout=subprocess.PIPE ).communicate()[0]
        self.version = self.version.decode('ascii').strip()

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SyncPlay GUI"))
        self.syncplay_version_label.setText(_translate("MainWindow", "SyncPlay "+self.version[30:35]))
        self.serverSettings_groupBox.setTitle(_translate("MainWindow", "Server Settings"))
        self.server_label.setText(_translate("MainWindow", "Server Adrress"))
        self.server_comboBox.setItemText(0, _translate("MainWindow", "syncplay.pl:8995"))
        self.server_comboBox.setItemText(1, _translate("MainWindow", "syncplay.pl:8996"))
        self.server_comboBox.setItemText(2, _translate("MainWindow", "syncplay.pl:8997"))
        self.server_comboBox.setItemText(3, _translate("MainWindow", "syncplay.pl:8998"))
        self.server_comboBox.setItemText(4, _translate("MainWindow", "syncplay.pl:8999"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.username_label.setText(_translate("MainWindow", "UserName"))
        self.room_name_label.setText(_translate("MainWindow", "Room Name"))
        self.playerSettings_groupBox.setTitle(_translate("MainWindow", "Player Settings"))
        self.file_path_label.setText(_translate("MainWindow", "File path"))
        self.file_path_toolButton.setText(_translate("MainWindow", "..."))
        self.player_path_label.setText(_translate("MainWindow", "Player Path"))
        self.player_comboBox.setItemText(0, _translate("MainWindow", "vlc"))
        self.player_comboBox.setItemText(1, _translate("MainWindow", "mpv"))
        self.player_comboBox.setItemText(2, _translate("MainWindow", "mpc-hc"))
        self.player_comboBox.setItemText(3, _translate("MainWindow", "mpc-be"))
        self.player_comboBox.setItemText(4, _translate("MainWindow", "mplayer2"))
        self.otherSettings_groupBox.setTitle(_translate("MainWindow", "Other Settings"))
        self.voicecall_app_label.setText(_translate("MainWindow", "VoiceCall App"))
        self.voicecall_app_which_toolButton.setText(_translate("MainWindow", "..."))
        self.voicecall_app_checkBox.setText(_translate("MainWindow", "Start VoiceCall App"))
        self.start_pushButton.setText(_translate("MainWindow", "Start"))
        self.close_pushButton.setText(_translate("MainWindow", "Close"))
        self.syncplay_version_label_5.setText(_translate("MainWindow", "Created By: PascPeli "))
        self.menuUpdate.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave_Configuration.setText(_translate("MainWindow", "Save Configuration"))
        self.actionLoad_Configuration.setText(_translate("MainWindow", "Load Configuration"))




    def init_values(self):
        conf_list=[]
        line_prefix=''
        self.configFile_path = os.getenv('XDG_CONFIG_HOME', os.path.expanduser('~/.config'))
        for name in [".syncplay", "syncplay.ini"]:
            config_file = os.path.join(self.configFile_path,name)
            if os.path.isfile(config_file):
                with open(config_file, 'r') as file:
                    while line_prefix!='playerpath':
                        try:
                            line = file.readline()
                            line = line.split('=')
                            line_prefix = line[0].strip()
                            conf_list.append(line[1].strip())
                        except:pass
                break
        try:
            self.server_address = conf_list[0]+':'+conf_list[1]
            self.password = conf_list[2]
            self.user_name = conf_list[3]
            self.room_name = conf_list[4]
            self.file_path = ''
            self.player_path = conf_list[5]

            self.set_values()
        except IndexError:
            pass

    def get_values(self):
        self.server_address = str(self.server_comboBox.currentText())
        self.room_name = self.room_name_lineEdit.text()
        self.password = self.password_lineEdit.text()
        self.user_name = self.username_lineEdit.text()
        self.file_path = self.file_path_lineEdit.text()

        player = str(self.player_comboBox.currentText())
        self.player_path = subprocess.Popen( ['which', player], stdout=subprocess.PIPE ).communicate()[0]
        self.player_path = self.player_path.decode('ascii').strip()

        call_app = self.voicecall_app_lineEdit.text()
        self.voiceCall_app = subprocess.Popen( ['which', call_app], stdout=subprocess.PIPE ).communicate()[0]
        self.voiceCall_app = self.voiceCall_app.decode('ascii').strip()


    def set_values(self):
        self.server_comboBox.setCurrentIndex(self.server_comboBox.findText(self.server_address))
        self.room_name_lineEdit.setText(self.room_name)
        self.password_lineEdit.setText(self.password)
        self.username_lineEdit.setText(self.user_name)
        self.file_path_lineEdit.setText(self.file_path)
        self.player_comboBox.setCurrentIndex(self.player_comboBox.findText(self.player_path))
        self.voiceCall_app = self.voicecall_app_lineEdit.text()

    def clear_values(self):
        self.server_comboBox.selectedIndex = 0
        self.room_name = ''
        self.password = ''
        self.user_name = ''
        self.file_path = ''
        self.player_comboBox.selectedIndex = 0
        self.voiceCall_app = ''
        self.set_values()

    def file_path_Button_func(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.file_path_lineEdit.setText(fileName)

    def startButton_func(self):

        self.get_values()
        self.command = []
        self.command.append('syncplay')
        self.command.append('"{}"'.format(self.file_path))
        self.command.append('--no-gui')
        self.command.append('-a ' + self.server_address)
        self.command.append('-p ' + self.password)
        self.command.append('-n ' + self.user_name)
        self.command.append('-r ' + self.room_name)
        self.command.append('--player-path')
        self.command.append(self.player_path)

        self.proc=subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.outputTimer.start()


    def closeButton_func(self):
        self.close()
        sys.exit(0)
        #QtCore.QCoreApplication.instance().quit()

    def save_config(self):
        self.get_values()
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.server_address + os.linesep)
                file.write(self.room_name + os.linesep)
                file.write(self.password + os.linesep)
                file.write(self.user_name + os.linesep)
                file.write(self.file_path + os.linesep)
                file.write(self.player_path + os.linesep)
                file.write(self.voiceCall_app + os.linesep)
            #print(fileName)

    def load_config(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.server_address = file.readline()
                self.room_name = file.readline()
                self.password = file.readline()
                self.user_name = file.readline()
                self.file_path = file.readline()
                self.player_path = file.readline()
                self.voiceCall_app = file.readline()
            print(fileName)

    def aboutdialog_show(self):
        pass

    def run_terminal_command(self):
        a=subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(a.communicate()[0])
        print(a.args)
        #subprocess.run(self.command, shell=True)
        #subprocess.run(["ls", "-l"])
        #syncplay --no-gui -a syncplay.pl:8998 -n BornReady -r κακαουρετες  --player-path \vlc

    def update_output(self):
        output = self.proc.stdout.readline()
        try:
            if output.decode('ascii').strip() != '':
                print(output.decode('ascii').strip())
        except:pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

