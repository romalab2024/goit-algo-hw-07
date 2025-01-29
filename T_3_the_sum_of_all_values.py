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

    def calculate_sum(self):
        """Обчислює суму всіх значень у дереві"""
        return self._calculate_sum(self.root)

    def _calculate_sum(self, current_node):
        """Рекурсивна функція для обчислення суми"""
        if current_node is None:
            return 0
        left_sum = self._calculate_sum(current_node.left)
        right_sum = self._calculate_sum(current_node.right)
        return current_node.value + left_sum + right_sum


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

    # Обчислення суми значень
    total_sum = bst.calculate_sum()
    print(f"Сума всіх значень у дереві: {total_sum}")
