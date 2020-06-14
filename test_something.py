import unittest

from something import ping_google


class TestSomething(unittest.TestCase):
    def test_ping_google_fail(self):
        self.assertEqual(300, ping_google())


if __name__ == "__main__":
    unittest.main()
