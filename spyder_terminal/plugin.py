# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2020, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Terminal Plugin.
"""

from qtpy.QtGui import QIcon
from spyder.api.plugins import Plugins
from spyder.api.plugins import SpyderDockablePlugin
from spyder.api.translations import get_translation

# from spyder_terminal.confpage import SpyderTerminalConfPage
from spyder_terminal.widgets import SpyderTerminalWidget

_ = get_translation("spyder_terminal")


class SpyderTerminal(SpyderDockablePlugin):
    """
    Spyder Terminal plugin.
    """

    NAME = "spyder_terminal"
    REQUIRES = []
    OPTIONAL = []
    WIDGET_CLASS = SpyderTerminalWidget
    CONF_SECTION = NAME
    # CONF_WIDGET_CLASS = SpyderTerminalConfPage
    CONF_FROM_OPTIONS = {
        
    }

    # --- Signals

    # --- SpyderPlugin API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("Spyder Terminal")

    def get_description(self):
        return _("Display OS independent virtual terminals inside the main "
                 "Spyder window.")

    def get_icon(self):
        return self.create_icon("DollarFileIcon")

    def register(self):
        widget = self.get_widget()

    def check_compatibility(self):
        valid = True
        message = ""  # Note: Remember to use _("") to localize the string
        return valid, message

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------
    # def get_terms(self):
    #     """Return terminal list."""
    #     return [cl for cl in self.terms if isinstance(cl, TerminalWidget)]

    # def get_focus_term(self):
    #     """Return current terminal with focus, if any."""
    #     widget = QApplication.focusWidget()
    #     for term in self.get_terms():
    #         if widget is term:
    #             return term

    # def get_current_term(self):
    #     """Return the currently selected terminal."""
    #     try:
    #         terminal = self.tabwidget.currentWidget()
    #     except AttributeError:
    #         terminal = None
    #     if terminal is not None:
    #         return terminal

    # def create_new_term(self, name=None, give_focus=True, path=None):
    #     """Add a new terminal tab."""
    #     if path is None:
    #         path = self.current_cwd
    #     path = path.replace('\\', '/')
    #     font = self.get_font()
    #     term = TerminalWidget(self, self.port, path=path, font=font.family(),
    #                           theme=self.theme, color_scheme=self.color_scheme)
    #     self.register_widget_shortcuts(term)
    #     self.register_widget_shortcuts(self.find_widget)
    #     self.add_tab(term)
    #     term.terminal_closed.connect(lambda: self.close_term(term=term))

    # def close_term(self, index=None, term=None):
    #     """Close a terminal tab."""
    #     if not self.tabwidget.count():
    #         return
    #     if term is not None:
    #         index = self.tabwidget.indexOf(term)
    #     if index is None and term is None:
    #         index = self.tabwidget.currentIndex()
    #     if index is not None:
    #         term = self.tabwidget.widget(index)

    #     term.close()
    #     self.tabwidget.removeTab(self.tabwidget.indexOf(term))
    #     self.terms.remove(term)
    #     if self.tabwidget.count() == 0:
    #         self.create_new_term()

    # def set_project_path(self, path):
    #     """Refresh current project path."""
    #     self.project_path = path
    #     self.new_terminal_project.setEnabled(True)

    # def set_current_opened_file(self, path):
    #     """Get path of current opened file in editor."""
    #     self.current_file_path = osp.dirname(path)

    # def unset_project_path(self):
    #     """Refresh current project path."""
    #     self.project_path = None
    #     self.new_terminal_project.setEnabled(False)

    # @Slot(str)
    # def set_current_cwd(self, cwd):
    #     """Update current working directory."""
    #     self.current_cwd = cwd

    # def server_is_ready(self):
    #     """Return server status."""
    #     return self.server_ready

    # def search_next(self, text, case=False, regex=False, word=False):
    #     """Search in the current terminal for the given regex."""
    #     term = self.get_current_term()
    #     if term:
    #         term.search_next(text, case=case, regex=regex, word=word)

    # def search_previous(self, text, case=False, regex=False, word=False):
    #     """Search in the current terminal for the given regex."""
    #     term = self.get_current_term()
    #     if term:
    #         term.search_previous(text, case=case, regex=regex, word=word)

    # # ------ Public API (for tabs) ---------------------------
    # def add_tab(self, widget):
    #     """Add tab."""
    #     self.terms.append(widget)
    #     num_term = self.tabwidget.count() + 1
    #     index = self.tabwidget.addTab(widget, "Terminal {0}".format(num_term))
    #     self.tabwidget.setCurrentIndex(index)
    #     self.tabwidget.setTabToolTip(index, "Terminal {0}".format(num_term))
    #     if self.dockwidget and not self._ismaximized:
    #         self.dockwidget.setVisible(True)
    #     self.activateWindow()
    #     widget.view.setFocus()

    # def move_tab(self, index_from, index_to):
    #     """
    #     Move tab (tabs themselves have already been moved by the tabwidget).

    #     Allows to change order of tabs.
    #     """
    #     term = self.terms.pop(index_from)
    #     self.terms.insert(index_to, term)

    # def tab_name_editor(self):
    #     """Trigger the tab name editor."""
    #     index = self.tabwidget.currentIndex()
    #     self.tabwidget.tabBar().tab_name_editor.edit_tab(index)
