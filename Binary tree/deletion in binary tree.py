#deletion in binary tree
'''
1)start from root of thr tree
2)if tree is empty, return none
3)if the root node is the node to be deleted
    a)if the root has no children, return None.
    b)if the root has only one child, return the child
    c)if the root has two children
        *Find the deepest node in the right sub tree(or left)
        *copy the data of the deepest node to the root
        *Delete the deepest node
4)otherwise, perform a level order traversal to find the node to be deleted
5)once the node to be deleted is found:
    a)if the node has only no child, delete the node
    b)if the node has only one child, replace the node with its child
    c)if the node has two children:
        *Find the deepest node in the right subtree(or left)
        *copy the data of the deepest node to the root
        *Delete the deepest node
6)Return the root of the modified tree
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
    def delete_deepest(root, d_node):
        q=[root]
        while q:
            temp=q.pop()
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right=None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left=None
                    return
                else:
                    q.append(temp.left)
    def deletion(root,key):
        if root is None:
            return None:
        if root.left is None and root.right is None:
            if root.data==key:
                return None
            else:
                return root
        key_node=None
        q=[root]
        temp=None
        while q:
            temp=q.pop(0)
            if temp.data==key:
                key_node=temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x=temp.data
            delete_deepest(root,temp)
            key_node.data=x
        return root
     if __name__=="__main__":
            root= TreeNode(50)
            root.left= TreeNode(30)
            root.left.left= TreeNode(20)
            root.left.right= TreeNode(40)
            root.right= TreeNode(70)
            root.right.left= TreeNode(60)
            root.right.right=TreeNode(80)
            print("The tree before the deletion:", end=" ")
            inorder(root)
            key=30
            root=deletion(root,key)
            print("\nThe tree after the deletion:", end=" ")
            inorder(root)
    
