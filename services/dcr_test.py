from logging import NullHandler, error
import unittest
from services.dcr import get_dominant_colors


class TestDCR(unittest.TestCase):
    # output needs to have an array / list type.
    def test_output_type(self):
        self.assertEqual(type(get_dominant_colors(
            "https://pbs.twimg.com/media/E0EA4j2VUAcFIZQ?format=jpg&name=large")),  list)

    # output should return a list with at least two values.
    def test_output_N(self):
        self.assertGreaterEqual(len(get_dominant_colors(
            "https://pbs.twimg.com/media/E0EA4j2VUAcFIZQ?format=jpg&name=large")), 2)

    # output should return a list with less than/an equal of five values.
    def test_output_less(self):
        self.assertLessEqual(len(get_dominant_colors(
            "https://pbs.twimg.com/media/E0EA4j2VUAcFIZQ?format=jpg&name=large")), 5)


if __name__ == '__main__':
    unittest.main()
