"""
Test suite for df3 tools module.

"""

import unittest
import glob
import os
import sys

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
        args = sys.argv
        sys.argv = ['df3split.py', 'data/clouds.df3']
        df3split.main()
        self.assertEqual(len(glob.glob("*.tga")), 133)
        sys.argv = ['df3split.py', 'clouds.df3']
        df3combine.main()
        with open('data/clouds.df3', "rb") as df3_file:
            orig_content = df3_file.read()
        with open('clouds.df3', "rb") as df3_file:
            combined_content = df3_file.read()
        self.assertEqual(orig_content, combined_content,
                         "Original file differs from combined file.")
        sys.argv = args

    def test_main(self):
        """
        Test main() functions are callable and raise SystemExit.

        """
        with self.assertRaises(SystemExit):
            df3split.main()
        with self.assertRaises(SystemExit):
            df3combine.main()

    @unittest.skip("Raise FileNotFoundError")
    def test_abscent_file(self):
        """
        Test behavior when DF3 file not found

        """
        args = sys.argv
        sys.argv = ['df3split.py', 'data/nofile.df3']
        df3split.main()
        sys.argv = args

    def test_no_layers(self):
        """
        Test behavior when images not found

        """
        args = sys.argv
        sys.argv = ['df3combine.py', '-p', 'nolayer', 'data/nofile.df3']
        with self.assertRaises(df3combine.Df3Exception):
            df3combine.main()
        sys.argv = args
