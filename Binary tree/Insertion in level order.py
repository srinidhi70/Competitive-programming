#Insertion in a binary tree level order
'''
Algorithm:
*start
1)create a queue and enqueue the root node
2)while the queue is not empty, do the following
    a)Dequeue a node from the frout of the queue.
    b)If the left child of the dequeued node is empty,insert the new node as the left child. Otherwise,
    enqueue the left child
    c)if the right child of the dequeued node is empt, insert the new node
3)Repeat step 2 until the new node is inserted into the binary tree.
*end
'''
from collections import deque
class TreeNode:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.key, end=" ")
            inorder_traversal(root.right)
    def insert(root,key):
        if not root:
            return TreeNode(key)
        queue=deque([root])
        while queue:
            node= queue.popleft()
            if not node.left:
                node.left=TreeNode(key)
                break
            else:
                queue.append(node.left)
            if not node.right:
                node.right= TreeNode(key)
                break
            else:
                queue.append(node.right)
        if __name__=="__main__":
            root= TreeNode(50)
            root.left= TreeNode(30)
            root.left.left= TreeNode(20)
            root.left.right= TreeNode(40)
            root.right= TreeNode(70)
            root.right.right= TreeNode(80)
            print("Inorder traversal before insertion:", end=" ")
            inorder_traversal(root)
            key=60
            insert(root, key)
            print("\nInored traversal after insertion:", end=" ")
            inorder_traversal(root)
    
