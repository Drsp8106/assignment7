class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        if current_node is None:
            current_node = self.root
            if current_node is None:
                print("Error: Tree is empty. Add a root doctor first.")
                return

        if current_node.name == parent_name:
            if side.lower() == "left":
                if current_node.left is None:
                    current_node.left = DoctorNode(doctor_name)
                else:
                    print(f"Error: LEFT side of {parent_name} is already occupied.")
            elif side.lower() == "right":
                if current_node.right is None:
                    current_node.right = DoctorNode(doctor_name)
                else:
                    print(f"Error: RIGHT side of {parent_name} is already occupied.")
            else:
                print("Error: Side must be 'left' or 'right'.")
            return

        if current_node.left:
            self.insert(parent_name, doctor_name, side, current_node.left)
        if current_node.right:
            self.insert(parent_name, doctor_name, side, current_node.right)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))
