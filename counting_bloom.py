import hashlib


class CountingBloomFilter:
    """Pure-Python Counting Bloom filter supporting deletions."""

    def __init__(self, size=256, num_hashes=4):
        if size <= 0 or num_hashes <= 0:
            raise ValueError("size and num_hashes must be positive")
        self.size = size
        self.num_hashes = num_hashes
        self.counts = [0] * size

    def _indices(self, item):
        raw = str(item).encode("utf-8")
        h1 = int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")
        h2 = int.from_bytes(hashlib.md5(raw).digest()[:8], "big") or 1
        for i in range(self.num_hashes):
            yield (h1 + i * h2) % self.size

    def add(self, item):
        for idx in self._indices(item):
            self.counts[idx] += 1

    def remove(self, item):
        if item not in self:
            return False
        for idx in self._indices(item):
            if self.counts[idx] > 0:
                self.counts[idx] -= 1
        return True

    def __contains__(self, item):
        return all(self.counts[idx] > 0 for idx in self._indices(item))
