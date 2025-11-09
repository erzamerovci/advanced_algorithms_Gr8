from collections import Counter
from typing import List, Optional, Deque
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        freq = Counter()

        def postorder(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            s = node.val + postorder(node.left) + postorder(node.right)
            freq[s] += 1
            return s

        postorder(root)
        max_freq = max(freq.values())
        return [s for s, c in freq.items() if c == max_freq]

def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q: Deque[TreeNode] = deque([root])
    for v in it:
        node = q[0]
        if node.left is None:
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
        else:
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
            q.popleft()
    return root

if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([5, 2, -3])
    print("Test 1:", sol.findFrequentTreeSum(root1))
    root2 = build_tree([5, 2, -5])
    print("Test 2:", sol.findFrequentTreeSum(root2))
