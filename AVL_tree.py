class Node:
    def __init__(self, value):
        self.parent = None
        self.right = None
        self.left = None
        self.height = 0
        self.ballance = 0

        self.key = value



class Avl_Tree:
    def __init__(self):
        self.root = None

    def inTree(self, key):
        node = self.root
        while node != None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return True

        return False

    def getHeights(self, node):
        lheight = -1
        rheight = -1

        # finds heights of children and updates heights as it goes
        if node.left != None:
            # finds height of left sub-tree
            lheight = self.getHeights(node.left)
            node.left.height = lheight
        if node.right != None:
            # finds height of right sub-tree
            rheight = self.getHeights(node.right)
            node.right.height = rheight

        # makes hight equal to height of tallest subtree + 1
        height = 1 + max(lheight, rheight)
        return height

    def fixBals(self, node):
        bal = node.left.height - node.right.height

        if bal > 1:
            self.rotRight(node)
        elif bal < -1:
            self.rotLeft(node)

    def insert(self, node):
        if self.inTree(node.key):
            print(f"{node.key} is already in the tree")
            return -1

        if self.root == None:
            self.root = node
        else:
            targ = self.root

            # gets inserted nodes parent by finding leaf node colsest in value
            while targ != None:
                parent = targ
                if node.key <= targ.key:
                    targ = targ.left
                else:
                    targ = targ.right

            # puts node into tree
            node.parent = parent

            if node.key <= parent.key:
                parent.left = node
            else:
                parent.right = node

            self.root.height = self.getHeights(self.root)

    def delete(self, key):
        pass

    def min(self):
        node = self.root
        while node.left:
            node = node.left

        return node.key

    def max(self):
        node = self.root
        while node.right:
            node = node.right

        return node.key

    def displayASC(self):
        stack = []
        node = self.root
        done = False
        while not done:
            if node:
                stack.append(node)
                node = node.left

            elif stack:
                node = stack.pop()
                print(f"{node.key}  {node.height}")

                node = node.right

            else:
                return None





    def displayDESC(self):
        stack = []
        node = self.root
        while True:
            if node:
                stack.append(node)
                node = node.right

            elif stack:
                node = stack.pop()
                print(f"{node.key}  {node.height}")

                node = node.left

            else:
                return None


tree = Avl_Tree()

tree.insert(Node(10))
tree.insert(Node(1))
tree.insert(Node(5))
tree.insert(Node(7))
tree.insert(Node(5))
tree.insert(Node(10))
tree.insert(Node(50))
tree.insert(Node(-3))
tree.insert(Node(1))

tree.displayASC()
