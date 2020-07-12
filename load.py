"""
Experimental example plugin that updates the main UI every time we get a journal event
"""
import tkinter
from EDMCPlugin.ui import EDMCUIDisplayRow, EDMCUIPluginBase


class ExampleJournalPlugin(EDMCUIPluginBase, EDMCUIDisplayRow):
    """
    A plugin that prints the time and journal item name each time one is seen.
    """

    # the TK panel widget we will update
    display = None

    def plugin_name(self):
        return "Example Journal Plugin"

    def plugin_version(self):
        return "0.0.1"

    def create_row(self, parent):
        label = tkinter.Label(parent, text="Journal:", justify=tkinter.LEFT)
        self.display = tkinter.Label(parent, text=self.plugin_name(), justify=tkinter.CENTER)
        return label, self.display

    def plugin_start(self):
        print("started {}".format(self.plugin_name()))

    def journal_event(self, cmdr, entry):
        self.display.after(1,
                           self.display.config,
                           {
                               "text": entry["entry"]["event"]
                           })


__plugin__ = ExampleJournalPlugin()
