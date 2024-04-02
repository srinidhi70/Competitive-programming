from collections import deque
class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
def diagonal_traversal(root):
    if not root:
        return[]
    result=[]
    queue=deque([(root,0)])
    while queue:
        node,level=queue.popleft()
        if level==len(result):
            result.append([])
        result[level].append(node.val)
        if node.left:
            queue.append((node.left,level+1))
        if node.right:
           queue.append((node.right,level)) 
    return result
root=TreeNode(8)
root.left=TreeNode(3)
root.right=TreeNode(10)
root.left.left=TreeNode(1)
root.left.right=TreeNode(6)
root.right.right=TreeNode(14)
root.right.right.left=TreeNode(13)
root.left.right.left=TreeNode(4)
root.left.right.right=TreeNode(7)
diagonal_order=diagonal_traversal(root)
print("diagonal order")
for level in diagonal_order:
    print(level)
