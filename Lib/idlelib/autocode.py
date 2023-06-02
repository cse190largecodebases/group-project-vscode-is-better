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

class SnippetDeleteDialog(simpledialog.Dialog):
    def __init__(self, parent, title, snippets):
        self.snippets = snippets
        super().__init__(parent, title)

    def body(self, master):
        self.title("Delete a Snippet")
        self.optionVar = tk.StringVar()
        self.optionVar.set(list(self.snippets.keys())[0])  # default choice
        self.dropdown = OptionMenu(master, self.optionVar, *self.snippets.keys())
        self.dropdown.pack()

    def apply(self):
        self.result = self.optionVar.get()

class CodeDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.text = ''
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text="Enter the code for the new snippet:").grid(row=0)
        self.text_widget = tk.Text(master)
        self.text_widget.grid(row=1, padx=10)
        self.text_widget.bind("<Return>", self.insert_newline)
        return self.text_widget

    def apply(self):
        self.text = self.text_widget.get("1.0", 'end-1c')
        
    def insert_newline(self, event=None):
        self.text_widget.insert(tk.INSERT, '\n')
        return "break"
    
class AutoCode:
    """Prepend or remove initial text from selected lines."""

    # Extend the format menu.
    menudefs = [
        ('edit', [
            ('Code fill', '<<code-fill>>'),
            ('Add snippet', '<<add-snippet>>'),
            ('Delete snippet', '<<delete-snippet>>')
        ])
    ]
    snippets = {
        "For Loop": "for i in range(n):\n    pass\n",
        "While Loop": "while condition:\n    pass\n",
        "Try-Catch Block": "try:\n    pass\nexcept Exception as e:\n    pass\n",
        "Function Definition": "def function_name(parameters):\n    pass\n",
        "Class Definition": "class ClassName:\n    def __init__(self):\n        pass\n",
        "If-Else Structure": "if condition:\n    pass\nelse:\n    pass\n",
    }

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
        root = tk.Tk()
        root.withdraw()

        dialog = SnippetDialog(root, "Select a Snippet", self.snippets)
        snippet = dialog.result

        if snippet:
            self.code_fill_event_logic(snippet)

        root.destroy()

    def code_fill_event_logic(self, snippet):
        self.text.insert(tk.INSERT, snippet)
        self.text.see(tk.INSERT)
        
    def add_snippet_event(self, event=None):
        root = tk.Tk()
        root.withdraw()

        snippet_description = simpledialog.askstring("New Snippet", "Enter the description of the new snippet:", parent=root)
        if snippet_description:
            snippet_dialog = CodeDialog(root, "New Snippet")
            snippet_code = snippet_dialog.text
            if snippet_code:
                self.add_snippet_event_logic(snippet_description, snippet_code)

        root.destroy()
        return 'break'
    
    def delete_snippet_event(self, event=None):
        root = tk.Tk()
        root.withdraw()

        delete_dialog = SnippetDeleteDialog(root, "Delete Snippet", self.snippets)
        snippet_to_delete = delete_dialog.result

        if snippet_to_delete:
            self.delete_snippet_event_logic(snippet_to_delete)

        root.destroy()
        return 'break'

    def add_snippet_event_logic(self, snippet_description, snippet_code):
        self.snippets[snippet_description] = snippet_code

    def delete_snippet_event_logic(self, snippet_to_delete):
        del self.snippets[snippet_to_delete]

AutoCode.reload()