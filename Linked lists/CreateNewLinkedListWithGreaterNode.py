#CreateNewLinkedListWithGreaterNode
'''given two linked lists of the same size, the task is to create a new linked using those linked lists. The
condition is that the greater node among both linked list will be added to the new linked list.'''

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,data):
        self.head=None
    #Function which returns new linked list
    def newList(root1, root2):
        ptr1=root1
        ptr2=root2
        root=None
        while(ptr!= None):
            temp=Node(0)
            temp.next=None
            if(ptr1.data<ptr2.data):
                temp.data=ptr2.data
            else:
                temp.data=ptr1.data
            if(root==None):
                root=temp
            else:
                ptr=root
                while(ptr.next!=None):
                    ptr=ptr.next
                ptr=ptr1.next
                ptr2=ptr2.next

                
