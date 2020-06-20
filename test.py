import unittest

import texttable_latex


class TexttableLatexTest(unittest.TestCase):

    def test_clean_row(self):
        row = ["Row1\n", "Row2"]
        cleaned = texttable_latex._clean_row(row)
        self.assertEqual(cleaned[0], "Row1")
        self.assertNotIn("\n", cleaned[0])
        self.assertEqual(cleaned[1], "Row2")

    def test_sanitise_drop_columns(self):
        header = ["Col1", "Col2", "Col3"]
        self.assertIsNone(texttable_latex._sanitise_drop_columns(header, ["Col1"]))
        self.assertIsNone(texttable_latex._sanitise_drop_columns(header, ["Col1", "Col2"]))
        self.assertRaises(texttable_latex.DropColumnError, texttable_latex._sanitise_drop_columns, header, ["Col4"])

    def test_drop_columns(self):
        target = ["Row1", "Row2", "Row3"]
        header = ["Col1", "Col2", "Col3"]
        no_drop = texttable_latex._drop_columns(target, header, [])
        one_drop = texttable_latex._drop_columns(target, header, ['Col1'])
        two_drop = texttable_latex._drop_columns(target, header, ['Col1', 'Col3'])
        self.assertEqual(len(no_drop), 3)
        self.assertTrue(target[0] in no_drop)
        self.assertTrue(target[1] in no_drop)
        self.assertTrue(target[2] in no_drop)
        self.assertEqual(len(one_drop), 2)
        self.assertTrue(target[0] not in one_drop)
        self.assertTrue(target[1] in one_drop)
        self.assertTrue(target[2] in one_drop)
        self.assertEqual(len(two_drop), 1)
        self.assertTrue(target[0] not in two_drop)
        self.assertTrue(target[1] in two_drop)
        self.assertTrue(target[2] not in two_drop)

    def test_indent_text(self):
        text = "test"
        no_ident = texttable_latex._indent_text(text, 0)
        one_ident = texttable_latex._indent_text(text, 1)
        two_ident = texttable_latex._indent_text(text, 2)
        self.assertIn(text, no_ident)
        self.assertEqual(len(no_ident), len(text))
        self.assertIn(text, one_ident)
        self.assertEqual(len(one_ident) - 1, len(text))
        self.assertIn(text, two_ident)
        self.assertEqual(len(two_ident) - 2, len(text))


if __name__ == '__main__':
    unittest.main()
