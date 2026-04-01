"""Binary Search Tree implementation."""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value) -> bool:
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

def inorder(self) -> list:
    """Return inorder traversal."""
    result = []
    self._inorder_recursive(self.root, result)
    return result

def _inorder_recursive(self, node, result):
    if node:
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

def preorder(self) -> list:
    """Return preorder traversal."""
    result = []
    self._preorder_recursive(self.root, result)
    return result

def _preorder_recursive(self, node, result):
    if node:
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

def height(self) -> int:
    """Calculate tree height."""
    return self._height_recursive(self.root)

def _height_recursive(self, node) -> int:
    if not node:
        return -1
    return 1 + max(
        self._height_recursive(node.left),
        self._height_recursive(node.right),
    )
