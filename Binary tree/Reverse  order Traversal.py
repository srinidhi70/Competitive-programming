#Reverse level order
from collections import deque
class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
def reverse_level_order(root):
    if not root:
        return[]
    result=[]
    queue=deque([root])
    while queue:
        level_size=len(queue)
        current_level=[]
        for i in range(level_size):
            node=queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.insert(0,current_level)
    return result
root= TreeNode(1)
root.left= TreeNode(2)
root.right= TreeNode(3)
root.left.left= TreeNode(4)
root.left.right= TreeNode(5)
root.right.left= TreeNode(6)
root.right.right= TreeNode(7)
reverse_order=reverse_level_order(root)
print("Reverse level order Traversal:")
for level in reverse_order:
    print(level)
