import unittest

from counting_bloom import CountingBloomFilter


class TestCountingBloomFilter(unittest.TestCase):
    def test_add_and_remove(self):
        cbf = CountingBloomFilter(size=256, num_hashes=4)
        cbf.add("alpha")
        cbf.add("beta")
        self.assertIn("alpha", cbf)
        self.assertIn("beta", cbf)

        self.assertTrue(cbf.remove("alpha"))
        self.assertNotIn("alpha", cbf)
        self.assertIn("beta", cbf)

    def test_remove_missing_returns_false(self):
        cbf = CountingBloomFilter(size=128, num_hashes=3)
        self.assertFalse(cbf.remove("not-added"))

    def test_duplicate_adds_require_matching_removals(self):
        cbf = CountingBloomFilter(size=256, num_hashes=4)
        cbf.add("dup")
        cbf.add("dup")
        self.assertTrue(cbf.remove("dup"))
        self.assertIn("dup", cbf)
        self.assertTrue(cbf.remove("dup"))
        self.assertNotIn("dup", cbf)


if __name__ == "__main__":
    unittest.main()
