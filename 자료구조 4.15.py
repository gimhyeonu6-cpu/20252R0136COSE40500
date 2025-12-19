class BinaryTreeNode :

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    n1 = BinaryTreeNode(93)
    n2 = BinaryTreeNode(15)
    n3 = BinaryTreeNode(19)
    n4 = BinaryTreeNode(36)
    n5 = BinaryTreeNode(44)
    n6 = BinaryTreeNode(72)
    n7 = BinaryTreeNode(83)

    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
    n5.left=n6
    n5.right=n7

        

        
