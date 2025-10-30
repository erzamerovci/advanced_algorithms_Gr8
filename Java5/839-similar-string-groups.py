class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        def isSimilar(a, b):
            diff = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            return len(diff) == 0 or (len(diff) == 2 and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]])

        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(strs[i], strs[j]):
                    union(i, j)

        groups = len({find(i) for i in range(n)})
        return groups


sol = Solution()

print(sol.numSimilarGroups(["tars", "rats", "arts", "star"]))  
print(sol.numSimilarGroups(["omv", "ovm"]))  
print(sol.numSimilarGroups(["abc", "abc", "abc"]))  
print(sol.numSimilarGroups(["abc", "def", "ghi"]))  
print(sol.numSimilarGroups(["abcd", "abdc", "acbd", "acdb"]))  
print(sol.numSimilarGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))  

