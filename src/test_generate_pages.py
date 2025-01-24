import unittest

from generate_pages import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello World"), "Hello World")
        self.assertEqual(extract_title("# Hello World\n\nThis is a test"), "Hello World")
        self.assertEqual(extract_title("# Hello World\n\nThis is a test\n\n# Another Title"), "Hello World")
        self.assertEqual(extract_title("# Hello World\n\nThis is a test\n\n# Another Title\n\n# Third Title"), "Hello World")
        with self.assertRaises(ValueError):
            extract_title("#\n\nThis is a test\n\n#Another Title\n\n#Third Title")
        with self.assertRaises(ValueError):
            extract_title("#\n\nThis is a test\n\nAnother Title\n\n#Third Title\n\n#")