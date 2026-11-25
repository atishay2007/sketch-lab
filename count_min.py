import hashlib


class CountMinSketch:
    """Pure-Python Count-Min Sketch for approximate frequency counting."""

    def __init__(self, width=256, depth=4):
        if width <= 0 or depth <= 0:
            raise ValueError("width and depth must be positive")
        self.width = width
        self.depth = depth
        self.table = [[0] * width for _ in range(depth)]

    def _indices(self, item):
        raw = str(item).encode("utf-8")
        for row in range(self.depth):
            digest = hashlib.sha256(f"{row}:".encode("utf-8") + raw).digest()
            yield int.from_bytes(digest[:8], "big") % self.width

    def add(self, item, count=1):
        if count < 0:
            raise ValueError("count must be non-negative")
        for row, col in enumerate(self._indices(item)):
            self.table[row][col] += count

    def estimate(self, item):
        return min(self.table[row][col] for row, col in enumerate(self._indices(item)))
