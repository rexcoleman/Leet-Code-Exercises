from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # If there are no elements to construct the tree
            if left > right:
                return None

            # Select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            # Build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # Build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)

def tree_to_list(root):
    output = []
    if not root:
        return None
    # Use a deque to keep track of the tree nodes (BFS)
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current:
            output.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            output.append(None)
    # Remove trailing None values
    while output and output[-1] == None:
        output.pop()
    return output


if __name__ == '__main__':

    # Inputs
    preorder_1 = [3, 9, 20, 15, 7]
    inorder_1 = [9, 3, 15, 20, 7]
    # Output_1 = [3,9,20,null,null,15,7]
    preorder_2 = [-1]
    inorder_2 = [-1]
    # Output_2 = [-1]

    solution_1 = Solution()
    solution_2 = Solution()

    test_1 = solution_1.buildTree(preorder_1, inorder_1)
    test_2 = solution_1.buildTree(preorder_2, inorder_2)

    output_1 = tree_to_list(test_1)
    output_2 = tree_to_list(test_2)

    print(f"\nOutput 1: {output_1}: \nExpected Output: [3,9,20,None,None,15,7]")
    print(f"\nOutput 2: {output_2}: \nExpected Output: [-1]")




