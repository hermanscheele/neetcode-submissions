# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        start = root
        prev = root

        while root:
            prev = root
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left



        if val < prev.val:
            prev.left = TreeNode(val)

        if val > prev.val:
            prev.right = TreeNode(val)


        return start