

class BinarySearchTree():
    
    class Node():
        def __init__(self, key, value) -> None:
            self.key   = key
            self.value = value
            self.right = None
            self.left  = None

        def min(self):
            if not self.left:
                return self
            else:
                return self.left.min()

        def print(self):
            print(f'key: {self.key}, value: {self.value}, left: {self.left.key if self.left else None}, right: {self.right.key if self.right else None}')

    def __init__(self) -> None:
        self.root = None

    def find_min_key(self):
        return self._find_min_key(self.root).key

    def _find_min_key(self, node: Node):
        return node.min()

    def no_rec_find_min_key(self):
        current = self.root

        while current and current.left:
            current = current.left

        return current.key

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: Node, key, value):
        
        new_node = self.Node(key, value)

        if not node:
            return new_node
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        return node

    def find(self, key):
        found_node = self._find(self.root, key)

        return found_node.value if found_node else None

    def find_node(self, key):
        found_node = self._find(self.root, key)

        return found_node

    def _find(self, node: Node, key):
        if not node or node.key == key:
            return node
        elif key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)

        return None

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

        return node

    def check_bst(self, node: Node):

        if not node:
            raise Exception("The node is null")

        left_ok = False

        if node.left:
            if node.left.key < node.key:
                left_ok = True
        else:
            left_ok = True

        right_ok = False

        if node.right:
            if node.right.key > node.key:
                right_ok = True
        else:
            right_ok = True

        return left_ok and right_ok


    def no_rec_insert(self, key, value):
        new_node = self.Node(key, value)

        if not self.root:
            self.root = new_node
            return
        
        current = self.root

        while current:
            if key < current.key:
                if not current.left:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return
                else:
                    current = current.right
        
    def no_rec_find(self, key):

        current = self.root

        while current:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right

        return None

    def pretty_print(self):

        root_left_key = self.root.left.key if self.root.left else 0 
        root_right_key = self.root.right.key if self.root.right else 0

        root_left_left_key = 0
        root_left_right_key = 0

        if self.root.left:
            root_left_left_key = self.root.left.left.key if self.root.left.left else 0
            root_left_right_key = self.root.left.right.key if self.root.left.right else 0

        root_right_left_key = 0
        root_right_right_key = 0

        if self.root.right:
            root_right_left_key = self.root.right.left.key if self.root.right.left else 0
            root_right_right_key = self.root.right.right.key if self.root.right.right else 0

        print('')
        print(f'    {self.root.key}')
        print("   /  \\")
        print(f'  {root_left_key}    {root_right_key}')
        print(f' / \\  / \\')
        print(f'{root_left_left_key}  {root_left_right_key} {root_right_left_key}   {root_right_right_key}')

    def print(self):

        print(f'ROOT key: {self.root.key}, value: {self.root.value}, left: {self.root.left.key if self.root.left else None}, right: {self.root.right.key if self.root.right else None}')

        current = self.root.left

        while current:
            print(f'LEFT key: {current.key}, value: {current.value}, left: {current.left.key if current.left else None}, right: {current.right.key if current.right else None}')
            current = current.left

        current = self.root.right

        while current:
            print(f'RIGHT key: {current.key}, value: {current.value}, left: {current.left.key if current.left else None}, right: {current.right.key if current.right else None}')
            current = current.right