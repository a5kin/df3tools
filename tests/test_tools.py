import unittest
import glob
import os

from df3tools import df3split, df3combine


class TestDf3Tools(unittest.TestCase):

    def tearDown(self):
        for filename in glob.glob("*.tga"):
            os.remove(filename)
        for filename in glob.glob("*.df3"):
            os.remove(filename)

    def test_full_cycle(self):
        df3split.df3split('data/clouds.df3')
        self.assertEqual(len(glob.glob("*.tga")), 133)
        df3combine.df3combine('clouds.df3')
