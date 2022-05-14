

class AVLTree():
    
    class Node():
        def __init__(self, key, value) -> None:
            self.key    = key
            self.value  = value
            self.left   = None
            self.right  = None
            self.height = 1

    def __init__(self) -> None:
        self.root = None

    def get_height(self, node: Node) -> int:
        return node.height if node else 0

    def get_max(self, a: int, b: int) -> int:
        return a if a > b else b

    def get_balance(self, node: Node) -> int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, x: Node):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = self.get_max(self.get_height(x.left), self.get_height(x.right))
        y.height = self.get_max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y: Node):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = self.get_max(self.get_height(y.left), self.get_height(y.right))
        x.height = self.get_max(self.get_height(x.left), self.get_height(x.right))

        return x

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: Node, key, value) -> Node:
        new_node = self.Node(key, value)
        
        if not node:    
            return new_node
        elif new_node.key < node.key:
            node.left = self._insert(node.left, key, value)
        elif new_node.key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            return node

        node.height = 1 + self.get_max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        elif balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        elif balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node) 

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node, key):
        if not node:
            return None
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_right_node = node.right.min()

                node.key   = min_right_node.key
                node.value = min_right_node.value
                
                node.right = self._delete(node.right, node.key)

        if not node:
            return node

        node.height = 1 + self.get_max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        elif balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        elif balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node) 

        return node
    
    def print_in_order_traversal(self):
        print('')
        self.in_order_traversal(self.root)

    def in_order_traversal(self, node: Node):
        if node:
            self.in_order_traversal(node.left)
            print(node.key)
            self.in_order_traversal(node.right)