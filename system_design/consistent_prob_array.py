class NumStore:
    def __init__(self):
        self._arr = []
        self._set = set()
        self._map = {}

    def add(self, val):
        if val in self._set:
            try:
                raise AttributeError("Element already present")
            except AttributeError:
                print("The Structure cannot have duplicates")
        self._set.add(val)
        self._arr.append(val)
        self._map[val] = len(self._arr) - 1

    
    def remove(self, val):
        