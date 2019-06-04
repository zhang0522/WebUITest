import unittest
from pageobject.indexpage import IndexPage

class TestIndexPage(unittest.TestCase):

    def test_open_indexpage(self):
        indexpage = IndexPage()
        self.assertEqual(indexpage.open_and_check())

if __name__ == '__main__':
    unittest.main()
