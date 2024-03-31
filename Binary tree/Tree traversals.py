class Node:
    def __init__(self,key):
        self.leftChild=None
        self.rightChild=None
        self.data=key
    def InorderTraversal(root):
        if root:
            InorderTraversal(root.leftChild)
            print(root.data, end=" ")
            InorderTraversal(root.rightChild)
    def PreorderTraversal(root):
        if root:
            print(root.data, end=" ")
            PreorderTraversal(root.leftChild)
            PreorderTraversal(root.rightChild)
    def PostorderTraversal(root):
        if root:
            PostorderTraversal(root.leftChild)
            PostorderTraversal(root.rightChild)
            print(root.data, end=" ")
    if __name__=="__main__":
        root=Node(1)
        root.leftChild=Node(2)
        root.rightChild=Node(3)
        root.leftChild.leftChild=Node(4)
        root.leftChild.rightChild=Node(5)
        root.rightChild.leftChild=Node(6)
        print("Inorder traversal of binary tree is")
        InorderTraversal(root)
        print("Preorder traversal of binary tree is")
        PreorderTraversal(root)
        print("Postorder traversal of binary tree is")
        PostorderTraversal(root)
