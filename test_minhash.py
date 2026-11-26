import unittest

from minhash import MinHash


class TestMinHash(unittest.TestCase):
    def test_identical_sets_have_similarity_one(self):
        a = MinHash(num_hashes=64)
        b = MinHash(num_hashes=64)
        items = ["alpha", "beta", "gamma", "delta"]
        a.update(items)
        b.update(items)
        self.assertEqual(a.jaccard(b), 1.0)

    def test_overlapping_sets_estimate_close_to_exact_jaccard(self):
        set_a = {f"w{i}" for i in range(0, 60)}
        set_b = {f"w{i}" for i in range(30, 90)}
        exact = len(set_a & set_b) / len(set_a | set_b)  # 30 / 90 = 0.333...

        mh_a = MinHash(num_hashes=128)
        mh_b = MinHash(num_hashes=128)
        mh_a.update(set_a)
        mh_b.update(set_b)

        est = mh_a.jaccard(mh_b)
        self.assertAlmostEqual(est, exact, delta=0.12)

    def test_mismatched_lengths_raise(self):
        with self.assertRaises(ValueError):
            MinHash(32).jaccard(MinHash(64))


if __name__ == "__main__":
    unittest.main()
