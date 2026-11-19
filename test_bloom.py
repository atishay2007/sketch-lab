import unittest

from bloom_filter import BloomFilter


class TestBloomFilter(unittest.TestCase):
    def test_added_items_are_always_found(self):
        bf = BloomFilter(size=512, num_hashes=4)
        words = ["hash", "sketch", "stream", "bloom", "index"]
        for w in words:
            bf.add(w)
        for w in words:
            self.assertIn(w, bf)

    def test_false_positive_rate_stays_low(self):
        bf = BloomFilter(size=2048, num_hashes=5)
        for i in range(100):
            bf.add(f"item:{i}")

        false_positives = sum(1 for i in range(100, 300) if f"item:{i}" in bf)
        self.assertLess(false_positives, 15)

    def test_invalid_params_raise(self):
        with self.assertRaises(ValueError):
            BloomFilter(size=0, num_hashes=3)


if __name__ == "__main__":
    unittest.main()
