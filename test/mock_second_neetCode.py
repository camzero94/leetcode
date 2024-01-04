
# Design Class

# 1 Inserting a value (no duplicates) O(1)
# 2. Removing a value O(1)
# 3. GetRandom a value that is already inserted (with equal prob)

# If array --> Inserting O(1) append, removing O(n) and GetRandom O(1)? dups 
# If Set --> Inserting O(1), removing O(1) and GetRandom Not possible? no dups

# Allow Duplicates
import random


class Solution:
    def __init__(self):
        self.data = []
        self.indices = {}
        self.idx = 0

    def insert(self, val: int):
        # idx represents slice index and skip dups
        # Append is  O(1)
        self.data.append(val)
        self.indices[val].append(self.idx)
        self.idx += 1
        return f"Value inserted is: {val}"

    def remove(self, val: int):
        if val not in self.indices:
            return "Not found"

        # Get index of item to be removed 
        idx_remove = self.indices.get(val)
        
        if not isinstance(idx_remove, int):
            # Get pointee of item to be remove O(1)
            removed = self.data[idx_remove[-1]]
            print(f"Item to be remove{removed}")

            # Copy last item in slice into position of item that going to be removed O(1)
            self.data[idx_remove[-1]] = self.data[-1]

            #Inside Dictionary modify index of last item for removed index O(1)
            self.indices[self.data[-1]] = idx_remove[-1]
        else:
            # Get pointee of item to be remove O(1)
            removed = self.data[idx_remove]
            print(f"Item to be remove{removed}")

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
print(res.insert(2))
print(res.insert(2))
print(res.insert(2))
print(res.insert(3))
print(res.data, res.indices)

# print(res.remove(2))
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
#
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
#
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
# print(res.get_random())
#
#
#
