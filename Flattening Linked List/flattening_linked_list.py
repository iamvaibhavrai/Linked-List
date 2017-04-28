class LinkedList:
    def __init__(self,data=None,right=None,below=None):
        self.data = data
        self.right = right
        self.below = below

def merge(a,b):
    if a == None:
        return b
    if b == None:
        return a
    if a.data < b.data:
        result = a
        result.below = merge(a.below,b)
    else:
        result = b
        result.below = merge(a,b.below)
    return result

def flatten(root):
    if root is None or root.right is None:
        return root
    root.right = flatten(root.right)
    root = merge(root,root.right)
    return root

def print_list(ll):
    temp = ll.head
    while temp is not None:
        print(temp.data,end = " ")
        temp = temp.below

def main():
    ll = LinkedList()
    ll.head = LinkedList(30)
    ll.head = LinkedList(8,None,ll.head)
    ll.head = LinkedList(7,None,ll.head)
    ll.right = LinkedList(20)
    ll.right.right = LinkedList(50)
    ll.right.right = LinkedList(22,None,ll.right.right)
    ll.right.right.right = LinkedList(45)
    ll.right.right.right = LinkedList(40,None,ll.right.right.right)
    ll.right.right.right = LinkedList(35,None,ll.right.right.right)
    ll.right.right.right = LinkedList(45,None,ll.right.right.right)
    ll.right.right = LinkedList(19,ll.right.right.right,ll.right.right)
    ll.right = LinkedList(10,ll.right.right,ll.right)
    ll.head = LinkedList(5,ll.right,ll.head)
    ll.head = flatten(ll.head)
    print_list(ll)

if __name__ == '__main__':
    main()
