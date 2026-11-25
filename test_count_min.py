import unittest

from count_min import CountMinSketch


class TestCountMinSketch(unittest.TestCase):
    def test_estimate_never_underestimates(self):
        cms = CountMinSketch(width=128, depth=4)
        counts = {"apple": 5, "banana": 12, "cherry": 1}
        for key, n in counts.items():
            cms.add(key, n)

        for key, n in counts.items():
            self.assertGreaterEqual(cms.estimate(key), n)

    def test_heavy_hitter_remains_accurate(self):
        cms = CountMinSketch(width=512, depth=4)
        for i in range(100):
            cms.add(f"noise:{i}", 1)
        cms.add("hot_key", 500)

        est = cms.estimate("hot_key")
        self.assertGreaterEqual(est, 500)
        self.assertLessEqual(est, 510)

    def test_invalid_params_raise(self):
        with self.assertRaises(ValueError):
            CountMinSketch(width=0, depth=4)


if __name__ == "__main__":
    unittest.main()
