#!/usr/bin/env python3
# coding=utf8

""" Module for unittests """

import unittest
from latex import Latex
class Testcase(unittest.TestCase):
    """
    My test class
    """

    def test_punk(self):
        """
        testing punkt fucntion, after "." we need to make a newline
        """
        la = Latex()
        text = "this is my test file.\nnewline after a punkt\n"
        self.assertEqual( la.readFromFile("testFile/testpunk.tex", "replace_punkt"), text)

    def test_comma(self):
        """
        testing commma fucntion, after "," we need to make a newline
        """
        la = Latex()
        text = "this is my test file,\nnewline after a comma\n"

        self.assertEqual( la.readFromFile("testFile/testcomma.tex", "replace_comma"), text)

    def test_proc(self):
        """
        testing proc fucntion, after a comment (%) we need to add space
        """
        la = Latex()
        text = "% space after a comment\n"
        self.assertEqual( la.readFromFile("testFile/testproc.tex", "replace_proc"), text)

if __name__ == '__main__':
    unittest.main(verbosity=3)
