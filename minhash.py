import hashlib


class MinHash:
    """Pure-Python MinHash for estimating Jaccard similarity between sets."""

    def __init__(self, num_hashes=64):
        if num_hashes <= 0:
            raise ValueError("num_hashes must be positive")
        self.num_hashes = num_hashes
        self.signature = [float("inf")] * num_hashes

    def _hash(self, item, seed):
        raw = f"{seed}:{item}".encode("utf-8")
        return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")

    def update(self, items):
        for item in items:
            for i in range(self.num_hashes):
                h = self._hash(item, i)
                if h < self.signature[i]:
                    self.signature[i] = h

    def jaccard(self, other):
        if self.num_hashes != other.num_hashes:
            raise ValueError("MinHash signatures must have the same length")
        matches = sum(1 for a, b in zip(self.signature, other.signature) if a == b)
        return matches / self.num_hashes
