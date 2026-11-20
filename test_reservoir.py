import random
import unittest

from reservoir import ReservoirSampler


class TestReservoirSampler(unittest.TestCase):
    def test_stream_shorter_than_k_keeps_all(self):
        sampler = ReservoirSampler(k=5, rng=random.Random(42))
        sampler.extend([10, 20, 30])
        self.assertEqual(sampler.sample, [10, 20, 30])
        self.assertEqual(sampler.seen, 3)

    def test_large_stream_keeps_exact_k_unique_items(self):
        sampler = ReservoirSampler(k=10, rng=random.Random(7))
        sampler.extend(range(1000))
        self.assertEqual(len(sampler.sample), 10)
        self.assertEqual(len(set(sampler.sample)), 10)
        self.assertEqual(sampler.seen, 1000)

    def test_invalid_k_raises(self):
        with self.assertRaises(ValueError):
            ReservoirSampler(k=0)


if __name__ == "__main__":
    unittest.main()
