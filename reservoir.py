import random


class ReservoirSampler:
    """Algorithm R reservoir sampling for uniform k-item streaming samples."""

    def __init__(self, k, rng=None):
        if k <= 0:
            raise ValueError("k must be positive")
        self.k = k
        self.rng = rng or random.Random()
        self.seen = 0
        self.sample = []

    def add(self, item):
        self.seen += 1
        if len(self.sample) < self.k:
            self.sample.append(item)
            return

        j = self.rng.randrange(self.seen)
        if j < self.k:
            self.sample[j] = item

    def extend(self, items):
        for item in items:
            self.add(item)
