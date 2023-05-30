"""Example extension, also used for testing.

See extend.txt for more details on creating an extension.
See config-extension.def for configuring an extension.
"""

from idlelib.config import idleConf
import tkinter as tk
from tkinter import simpledialog
from tkinter import OptionMenu

class SnippetDialog(simpledialog.Dialog):
    def __init__(self, parent, title, snippets):
        self.snippets = snippets
        super().__init__(parent, title)

    def body(self, master):
        self.title("Select a Snippet")
        self.optionVar = tk.StringVar()
        self.optionVar.set(list(self.snippets.keys())[0]) # default choice
        self.dropdown = OptionMenu(master, self.optionVar, *self.snippets.keys())
        self.dropdown.pack()

    def apply(self):
        self.result = self.snippets[self.optionVar.get()]

class AutoCode:
    """Prepend or remove initial text from selected lines."""

    # Extend the format menu.
    menudefs = [
        ('edit', [
            ('Code fill', '<<code-fill>>'),
        ] )
    ]

    def __init__(self, editwin):
        "Initialize the settings for this extension."
        self.editwin = editwin
        self.text = editwin.text
        self.formatter = editwin.fregion

    @classmethod
    def reload(cls):
        "Load class variables from config."
        cls.ztext = idleConf.GetOption('extensions', 'AutoCode', 'z-text')

    def code_fill_event(self, event=None):
            snippets = {
                "For Loop": "for i in range(n):\n    pass\n",
                "While Loop": "while condition:\n    pass\n",
                "Try-Catch Block": "try:\n    pass\nexcept Exception as e:\n    pass\n",
                "Function Definition": "def function_name(parameters):\n    pass\n",
                "Class Definition": "class ClassName:\n    def __init__(self):\n        pass\n",
                "If-Else Structure": "if condition:\n    pass\nelse:\n    pass\n",
            }


            root = tk.Tk()
            root.withdraw()  # Hide the main window
            dialog = SnippetDialog(root, "Select a Snippet", snippets)
            snippet = dialog.result

            if snippet:
                self.text.insert(tk.INSERT, snippet)
                self.text.see(tk.INSERT)

            root.destroy()  # Close the dialog box

AutoCode.reload()


