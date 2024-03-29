class TreeNode:
    
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self, level=0):
        # HELPER METHOD TO PRINT TREE!
        ret = "--->" * level + repr(self.value) + "\n"
        
        for child in self.children:
            ret += child.__repr__(level+1)
        
        return ret

    def add_child(self, child_node):
        self.children.append(child_node) 

    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children 
                        if child is not child_node]

    def traverse(self):
        print("Traversing...")
        nodes_to_visit = [self]

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


### TEST CODE TO PRINT TREE
if __name__ == "__main__":
    company = [
        "Monkey Business CEO", 
        "VP of Bananas", 
        "VP of Lazing Around", 
        "Associate Chimp", 
        "Chief Bonobo", "Produce Manager", "Tire Swing R & D"]
    root = TreeNode(company.pop(0))
    for count in range(2):
        child = TreeNode(company.pop(0))
        root.add_child(child)

    root.children[0].add_child(TreeNode(company.pop(0)))
    root.children[0].add_child(TreeNode(company.pop(0)))
    root.children[1].add_child(TreeNode(company.pop(0)))
    root.children[1].add_child(TreeNode(company.pop(0)))
    print("MONKEY BUSINESS, LLC.")
    print("=====================")
    print(root)
