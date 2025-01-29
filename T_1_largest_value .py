class Node:
    """Клас для вузла дерева"""
    def __init__(self, value):
        self.value = value  # Значення вузла
        self.left = None  # Лівий нащадок
        self.right = None  # Правий нащадок


class BinarySearchTree:
    """Клас для двійкового дерева пошуку (BST)"""
    def __init__(self):
        self.root = None  # Корінь дерева

    def insert(self, value):
        """Додає нове значення до дерева"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        """Рекурсивна вставка вузла"""
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def find_max(self):
        """Знаходить найбільше значення в дереві"""
        if self.root is None:
            return None  # Якщо дерево порожнє
        current = self.root
        while current.right:
            current = current.right
        return current.value


if __name__ == "__main__":
    # Створення дерева
    bst = BinarySearchTree()

    # Вставка значень у дерево
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # Знаходження найбільшого значення
    max_value = bst.find_max()
    print(f"Найбільше значення в дереві: {max_value}")
