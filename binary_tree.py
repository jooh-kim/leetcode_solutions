# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#iterative traversal requires a stack
stack = []
def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # Recursive
    # if root != None:
    #     print(root.val)
    #     preorderTraversal(root.left)
    #     preorderTraversal(root.right)
    # else:
    #     return

    # Iterative
    result = []
    if root is None:
        return result
    stack = []
    stack.append(root)
    while len(stack) > 0:
        result.append(stack[-1].val)
        node = stack.pop()
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result

def postorderTraversal(root):
    # recursive 
    # if root:
    #     postorderTraversal(root.left)
    #     postorderTraversal(root.right)
    #     print(root.val)
    if root is None:
        return []
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1) > 0:
        node = stack1.pop()
        stack2.append(node.val)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
    stack2.reverse()
    return stack2
    # print(stack2[::-1])

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # recursive
    # if root:
    #     inorderTraversal(root.left)
    #     print(root.val)
    #     inorderTraversal(root.right)
    result = []
    stack = []
    pointer = root
    while len(stack) > 0 or pointer is not None:
        # stack.append(pointer)
        if pointer is None:
            node = stack.pop()
            result.append(node.val)
            pointer = node.right
        else:
            stack.append(pointer)
            pointer = pointer.left
    return result

""" 
Level-Order Traversal
BFS - Breadth First Search

Queue is used to help the algorithm
"""

        

def main():
    # sol = Solution()
    root = TreeNode(1) 
    root.left      = TreeNode(2) 
    # root.right     = TreeNode(3) 

    root.left.left  = TreeNode(4) 
    # root.left.right  = TreeNode(5) 

    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)


    print(postorderTraversal(root))

if __name__ == "__main__":
    main()