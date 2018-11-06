class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = 0

        def dfs(root):
            # Edge/Condition
            if not root:
                return 0

            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.right)

        dfs(root)
        return self.res