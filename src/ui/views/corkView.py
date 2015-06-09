#!/usr/bin/env python
#--!-- coding: utf8 --!--
 



from qt import *
from enums import *
from functions import *
from ui.views.corkDelegate import *
from ui.views.dndView import *
from ui.views.outlineBasics import *

class corkView(QListView, dndView, outlineBasics):
    
    def __init__(self, parent=None):
        QListView.__init__(self, parent)
        dndView.__init__(self, parent)
        outlineBasics.__init__(self, parent)
        
        self.setResizeMode(QListView.Adjust)
        self.setWrapping(True)
        self.setItemDelegate(corkDelegate())
        self.setSpacing(5)
        self.setStyleSheet("""QListView {
            background:#926239;
            }""")
        self.setVerticalScrollMode(self.ScrollPerPixel)
        self.setFlow(self.LeftToRight)
        self.setSelectionBehavior(self.SelectRows)
        
    def dragMoveEvent(self, event):
        dndView.dragMoveEvent(self, event)
        QListView.dragMoveEvent(self, event)
        
    def mouseReleaseEvent(self, event):
        QListView.mouseReleaseEvent(self, event)
        outlineBasics.mouseReleaseEvent(self, event)