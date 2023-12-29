# Design Class

# 1 Inserting a value (no duplicates) O(1)
# 2. Removing a value O(1)
# 3. GetRandom a value that is already inserted (with equal prob)

# If array --> Inserting O(1) append, removing O(n) and GetRandom O(1)? dups 
# If Set --> Inserting O(1), removing O(1) and GetRandom Not possible? no dups

# Try slice of dicts
import random


class Solution:
    def __init__(self):
        self.data = []
        self.indices = {}
        self.idx = 0

    def insert(self, val: int):
        # idx represents slice index and skip dups
        if val not in self.indices:
            # Append is  O(1)
            self.data.append(val)
            self.indices[val] = self.idx
            self.idx += 1
            return f"Value inserted is: {val}"
        else:
            return f"Dup Val {val}"

    def remove(self, val: int):
        if val not in self.indices:
            return "Not found"

        # Get index of item to be removed 
        idx_remove = self.indices.get(val)

        # Get pointee of item to be remove O(1)
        removed = self.data[idx_remove]
        print(removed)

        # Copy last item in slice into position of item that going to be removed O(1)
        self.data[idx_remove] = self.data[-1]

        #Inside Dictionary modify index of last item for removed index O(1)
        self.indices[self.data[-1]] = idx_remove

        # Pop duplicate item in slice O(1) the last item
        self.data.pop()

        # Del from dictionary  O(1)
        del self.indices[removed]
        return f"Value removed is: {removed}"

    def get_random(self):
        return f"Value random is: {random.choice(self.data)}"


res = Solution()
print(res.insert(1))
print(res.insert(1))
print(res.insert(2))
print(res.insert(3))
print(res.remove(2))
print(res.get_random())
print(res.get_random())
print(res.get_random())
print(res.get_random())
print(res.get_random())

print(res.get_random())
print(res.get_random())
print(res.get_random())
print(res.get_random())
print(res.get_random())

print(res.get_random())
print(res.get_random())
print(res.get_random())
print(res.get_random())
print(res.get_random())



