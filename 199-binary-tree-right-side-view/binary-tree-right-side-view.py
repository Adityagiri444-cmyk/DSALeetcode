class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        ans = []

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)

                if i == size - 1:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return ans