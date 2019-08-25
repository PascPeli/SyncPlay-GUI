#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:56:09 2019

@author: pascpeli
"""
from PyQt5.QtWidgets import QMessageBox, QLineEdit

class FileEdit(QLineEdit):
    def __init__(self, parent, extensions):
        super(FileEdit, self).__init__(parent)

        self.extensions = extensions
        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            # any file type here
            if filepath[-4:].lower() in self.extensions:
                self.setText(filepath)
            else:
                dialog = QMessageBox()
                dialog.setWindowTitle("Error: Invalid File")
                dialog.setText("Only {} files are accepted".format(', '.join(self.extensions)))
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()