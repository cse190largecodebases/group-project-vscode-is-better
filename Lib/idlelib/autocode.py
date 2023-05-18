"""Example extension, also used for testing.

See extend.txt for more details on creating an extension.
See config-extension.def for configuring an extension.
"""

from idlelib.config import idleConf
from functools import wraps
from idlelib.config import idleConf
from idlelib.editor import EditorWindow
from idlelib.format import FormatRegion
from idlelib.undo import UndoDelegator
from idlelib.percolator import Percolator
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


def format_selection(format_line):
    "Apply a formatting function to all of the selected lines."

    @wraps(format_line)
    def apply(self, event=None):
        head, tail, chars, lines = self.formatter.get_region()
        for pos in range(len(lines) - 1):
            line = lines[pos]
            lines[pos] = format_line(self, line)
        self.formatter.set_region(head, tail, chars, lines)
        return 'break'

    return apply


class AutoCode:
    """Prepend or remove initial text from selected lines."""

    # Extend the format menu.
    menudefs = [
        ('edit', [
            ('Code fill', '<<code-fill>>'),
        ] )
    ]



    code_snippets = {
        'For Loop': 'for item in sequence:\n    # Do something',
        'While Loop': 'while condition:\n    # Do something',
        'Try-Except': 'try:\n    # Code that might raise an exception\nexcept Exception as e:\n    # Handle the exception',
    }

    def __init__(self, editwin):
        "Initialize the settings for this extension."
        self.editwin = editwin
        self.text = editwin.text
        self.formatter = editwin.fregion



    @classmethod
    def reload(cls):
        "Load class variables from config."
        cls.ztext = idleConf.GetOption('extensions', 'ZzDummy', 'z-text')

   

    def code_fill_event(self, event=None):
        snippets = [
            "for i in range (1,10):\n",
            "print('this code only partially works')",
            "import sys",
            "from tkinter import Tk, Button",
            "def my_function():",
            "    print('Hello, world!')"
        ]

        root = tk.Tk()
        root.withdraw()  # Hide the main window

        selected_snippet = messagebox.askquestion("Autocode Snippets",
                                                "Do you want to insert a code snippet?")
        

        if selected_snippet == "yes":
            snippet = simpledialog.askstring("Select a Snippet", "Select a code snippet:", 
                                            parent=root, initialvalue=snippets[0])
                                            # listboxheight=len(snippets), 
                                            # dropdown=sorted(snippets))

            if snippet:
                # Insert the selected snippet at the current cursor position
                    if (self.editwin.flist.pyshell == None):
                        self.editwin.flist.open_shell()
                        
                    #print to the python shell
                    self.editwin.flist.pyshell.write(snippets[0])
                    #self.editwin.flist.pyshell.text.event_generate("<<newline>>")
                    self.editwin.flist.pyshell.interp.runsource(snippets[0])


                    out_msg = self.editwin.text
                    first, last = self.editwin.get_selection_indices()
                    if first and last:
                        head = out_msg.index(first + " linestart")
                        tail = out_msg.index(last + "-1c lineend +1c")
                    else:
                        head = out_msg.index("insert linestart")
                        tail = out_msg.index("insert lineend +1c")
                    chars = out_msg.get(head, tail)
                    lines = chars.split("\n")
                    for pos in range(len(lines) - 1):
                            line = lines[pos]
                            lines[pos] = snippets[0] + line

                    newchars = "\n".join(lines)
                    out_msg.tag_remove("sel", "1.0", "end")
                    out_msg.mark_set("insert", head)
                    out_msg.undo_block_start()
                    out_msg.delete(head, tail)
                    out_msg.insert(head, newchars)
                    out_msg.undo_block_stop()
                    out_msg.tag_add("sel", head, "insert")

                    return "break"
                    
                    #add a newline
                    #self.editwin.flist.pyshell.write("\n")

                    #add the python prompt to indicate that the python shell can now be used as normal
                    #self.editwin.flist.pyshell.showprompt()

        root.destroy()  # Close the dialog box


    def insert_snippet(self, snippet):
        # Implement the logic to insert the snippet at the current cursor position
        
        pass




    @format_selection
    def z_out_event(self, line):
        """Remove specific text from the beginning of each selected line.

        This is bound to the <<z-out>> virtual event when the extensions
        are loaded.
        """
        zlength = 0 if not line.startswith(self.ztext) else len(self.ztext)
        return line[zlength:]


AutoCode.reload()


# if __name__ == "__main__":
#     import unittest
#     unittest.main('idlelib.idle_test.test_zzdummy', verbosity=2, exit=False)
