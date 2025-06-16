# 139335609

from sys import stdin


class Stack:
    """Простой стек на базе списка."""

    def __init__(self):
        self.items = []

    def push(self, item: tuple):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def decode_instructions(message: str) -> str:
    """Основная функция для решения задачи на основе стека."""
    stack: Stack = Stack()
    current_num: int = 0
    current_str: str = ''

    for symbol in message:
        if symbol.isdigit():
            current_num = current_num * 10 + int(symbol)
        elif symbol == '[':
            stack.push((current_str, current_num))
            current_str = ''
            current_num = 0
        elif symbol == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += symbol

    return current_str


def main() -> None:
    message: str = stdin.readline().strip()
    print(decode_instructions(message))


if __name__ == "__main__":
    main()
