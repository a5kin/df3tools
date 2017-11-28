"""
Test suite for df3 tools module.

"""

import unittest
import glob
import os

from df3tools import df3split, df3combine


class TestDf3Tools(unittest.TestCase):
    """
    Tests for df3split and df3combine tools.

    """

    def tearDown(self):
        """
        Clean up .tga and .df3 files after test.

        """
        for filename in glob.glob("*.tga"):
            os.remove(filename)
        for filename in glob.glob("*.df3"):
            os.remove(filename)

    def test_full_cycle(self):
        """
        Test that DF3 split and combine produce same file.

        """
        df3split.df3split('data/clouds.df3')
        self.assertEqual(len(glob.glob("*.tga")), 133)
        df3combine.df3combine('clouds.df3')
        with open('data/clouds.df3', "rb") as df3_file:
            orig_content = df3_file.read()
        with open('clouds.df3', "rb") as df3_file:
            combined_content = df3_file.read()
        self.assertEqual(orig_content, combined_content,
                         "Original file differs from combined file.")
