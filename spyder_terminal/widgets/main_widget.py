# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2020, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Terminal Main Widget.
"""

from spyder.api.translations import get_translation
from qtpy.QtWidgets import QHBoxLayout, QLabel
from spyder.api.widgets import PluginMainWidget

_ = get_translation("spyder_terminal")


class SpyderTerminalActions:
    ExampleAction = "example_action"


class SpyderTerminalToolBarSections:
    ExampleSection = "example_section"


class SpyderTerminalOptionsMenuSections:
    ExampleSection = "example_section"


class SpyderTerminalWidget(PluginMainWidget):
    DEFAULT_OPTIONS = {}

    # Signals

    def __init__(self, name, plugin, parent=None, options=DEFAULT_OPTIONS):
        super().__init__(name, plugin, parent=parent, options=options)

        # Create an example label
        self._example_label = QLabel("Example Label")

        # Add example label to layout
        layout = QHBoxLayout()
        layout.addWidget(self._example_label)
        self.setLayout(layout)

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def get_title(self):
        return _("Terminal")

    def get_focus_widget(self):
        pass

    def setup(self, options=DEFAULT_OPTIONS):
        # Create an example action
        example_action = self.create_action(
            name=SpyderTerminalActions.ExampleAction,
            text="Example action",
            tip="Example hover hint",
            icon=self.create_icon("spyder"),
            icon_text="Example icon text",
            triggered=lambda: print("Example action triggered!"),
        )

        # Add an example action to the plugin options menu
        menu = self.get_options_menu()
        self.add_item_to_menu(
            example_action,
            menu,
            SpyderTerminalOptionsMenuSections.ExampleSection,
        )

        # Add an example action to the plugin toolbar
        toolbar = self.get_main_toolbar()
        self.add_item_to_toolbar(
            example_action,
            toolbar,
            SpyderTerminalOptionsMenuSections.ExampleSection,
        )

    def on_option_update(self, option, value):
        pass

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
