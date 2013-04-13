# -*- coding: UTF-8 -*-

from ninja_ide.core import plugin
from PyQt4.QtCore import SIGNAL
#from PyQt4.QtCore import QEvent
from .parser import Parser


p = Parser()


class Vim(plugin.Plugin):
    def initialize(self):
        # Init your plugin
        self.editor_s = self.locator.get_service('editor')
        #self.editor_s.blockSignals(True)
        #self.editor_s.editorKeyPressEvent.disconnect(self.editor_s,
        self.editor_s.editorKeyPressEvent.connect(self.echoEvent)
        #print self.editor_s.get_text()

    def echoEvent(self, event):
        print((event.key()), (self.editor_s.get_lines_count()))
        #self.editor_s.cursorPositionChange(1, 1)
        #p.cursorMovement(event)
        #self.editor_s.cursorPositionChange(p._line, p._column)

    def finish(self):
        # Shutdown your plugin
        pass

    def get_preferences_widget(self):
        # Return a widget for customize your plugin
        pass

