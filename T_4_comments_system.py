class Comment:
    """Клас для представлення коментаря з ієрархічною структурою."""
    def __init__(self, text, author):
        """
        Ініціалізує коментар.
        :param text: Текст коментаря.
        :param author: Автор коментаря.
        """
        self.text = text  # Текст коментаря
        self.author = author  # Автор коментаря
        self.replies = []  # Список відповідей
        self.is_deleted = False  # Прапорець видаленого коментаря

    def add_reply(self, reply):
        """
        Додає відповідь до коментаря.
        :param reply: Об'єкт класу Comment.
        """
        self.replies.append(reply)

    def remove_reply(self):
        """
        Видаляє коментар. Змінює текст коментаря на "Цей коментар було видалено"
        та встановлює прапорець is_deleted у True.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        """
        Рекурсивно виводить коментар та всі його відповіді.
        :param level: Рівень відступу для відображення ієрархії.
        """
        indent = "    " * level  # Відступ залежно від рівня
        if not self.is_deleted:
            print(f"{indent}{self.author}: {self.text}")
        else:
            print(f"{indent}{self.text}")
        for reply in self.replies:
            reply.display(level + 1)


# Демонстрація роботи
if __name__ == "__main__":
    # Створення кореневого коментаря
    root_comment = Comment("Яка чудова книга!", "Бодя")

    # Створення відповідей
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    # Додавання відповідей до кореневого коментаря
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    # Додавання відповіді до відповіді
    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # Видалення коментаря
    reply1.remove_reply()

    # Виведення всієї структури коментарів
    root_comment.display()
