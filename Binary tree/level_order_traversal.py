class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def level_order_traversal(root):
        if root is None:
            return
        queue=[root]
        while queue:
            current_level=[]
            level_size=len(queue)
            for i in range(level_size):
                node=queue.pop(0)
                current_level.append(node.key)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(*current_level, sep=" ", end=" ")
    if __name__=="__main__":
        root= TreeNode(1)
        root.left= TreeNode(2)
        root.right= TreeNode(3)
        root.left.left= TreeNode(4)
        root.left.right= TreeNode(5)
        root.right.left= TreeNode(6)
        root.right.right= TreeNode(7)
        print("Level order Traversal:")
        level_order_traversal(root)
        
