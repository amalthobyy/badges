class TreeNode:
    def __init__(self, value):
        self.value = value  
        self.children = []  

    def add_child(self, child):
        self.children.append(child)

    
    def display(self, level=0):
        print(" " * level * 4 + str(self.value))  
        for child in self.children:
            child.display(level + 1) 


if __name__ == "__main__":
    
    root = TreeNode("Root")


    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    root.add_child(child1)
    root.add_child(child2)

   
    child1.add_child(TreeNode("Grandchild 1"))
    child1.add_child(TreeNode("Grandchild 2"))
    child2.add_child(TreeNode("Grandchild 3"))

    
    print("Tree structure:")
    root.display()
