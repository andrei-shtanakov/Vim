# -*- coding: UTF-8 -*-

from ninja_ide.core import plugin


class Vim(plugin.Plugin):
    def initialize(self):
        # Init your plugin
        self.editor_s = self.locator.get_service('editor')
        self.toolbar_s = self.locator.get_service('toolbar')
        self.menuApp_s = self.locator.get_service('menuApp')
        self.misc_s = self.locator.get_service('misc')
        self.explorer_s = self.locator.get_service('explorer')

    def finish(self):
        # Shutdown your plugin
        pass

    def get_preferences_widget(self):
        # Return a widget for customize your plugin
        pass
