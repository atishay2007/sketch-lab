import hashlib
import math


class BloomFilter:
    """Minimal pure-Python Bloom filter using double hashing."""

    def __init__(self, size=1024, num_hashes=4):
        if size <= 0 or num_hashes <= 0:
            raise ValueError("size and num_hashes must be positive")
        self.size = size
        self.num_hashes = num_hashes
        self.bits = bytearray(math.ceil(size / 8))

    def _hashes(self, item):
        raw = str(item).encode("utf-8")
        h1 = int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")
        h2 = int.from_bytes(hashlib.md5(raw).digest()[:8], "big") or 1
        for i in range(self.num_hashes):
            yield (h1 + i * h2) % self.size

    def _set_bit(self, idx):
        self.bits[idx // 8] |= 1 << (idx % 8)

    def _get_bit(self, idx):
        return bool(self.bits[idx // 8] & (1 << (idx % 8)))

    def add(self, item):
        for idx in self._hashes(item):
            self._set_bit(idx)

    def __contains__(self, item):
        return all(self._get_bit(idx) for idx in self._hashes(item))
