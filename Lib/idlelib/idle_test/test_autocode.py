import unittest
from test.support import requires
from unittest.mock import MagicMock
from idlelib import autocode

class TestAutoCode(unittest.TestCase):
    def setUp(self):
        self.editwin = MagicMock()
        self.editwin.text = MagicMock()
        self.auto_code = autocode.AutoCode(self.editwin)

    def test_init(self):
        self.assertEqual(self.auto_code.editwin, self.editwin)
        self.assertEqual(self.auto_code.text, self.editwin.text)

    def test_add_snippet_event(self):
        snippet_description = "Test snippet"
        snippet_code = "print('Hello, World!')"
        self.auto_code.add_snippet_event_logic(snippet_description, snippet_code)
        self.assertEqual(self.auto_code.snippets[snippet_description], snippet_code)

    def test_delete_snippet_event(self):
        snippet_description = "Test snippet"
        snippet_code = "print('Hello, World!')"
        self.auto_code.add_snippet_event_logic(snippet_description, snippet_code)
        self.auto_code.delete_snippet_event_logic(snippet_description)
        self.assertNotIn(snippet_description, self.auto_code.snippets)

    def test_code_fill_event_logic(self):
        snippet = "print('Hello, World!')"
        self.auto_code.code_fill_event_logic(snippet)
        self.auto_code.text.insert.assert_called_once_with('insert', snippet)
        self.auto_code.text.see.assert_called_once_with('insert')
    
    def test_code_fill_event_logic_after_add_snippet(self):
        # First, add a custom snippet
        snippet_description = "Test snippet"
        snippet_code = "print('Hello, Test Snippet!')"
        self.auto_code.add_snippet_event_logic(snippet_description, snippet_code)

        # Check if the snippet was added correctly
        self.assertEqual(self.auto_code.snippets[snippet_description], snippet_code)

        # Now test code_fill_event_logic with this snippet
        self.auto_code.code_fill_event_logic(snippet_code)
        self.auto_code.text.insert.assert_called_once_with('insert', snippet_code)
        self.auto_code.text.see.assert_called_once_with('insert')
    
if __name__ == "__main__":
    unittest.main()
