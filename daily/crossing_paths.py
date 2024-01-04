
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        visited = {(0,0)}
        x , y = 0, 0
        for l in path:
            if l == 'N':
                y += 1
            if l == 'E':
                x += 1
            if l == 'W':
                x -= 1
            if l == 'S':
                y -= 1
        
            if (x, y) in visited:
                return True

            visited.add((x, y))
        return False

res = Solution()
print(res.isPathCrossing("ES"))
