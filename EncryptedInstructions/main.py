# 139338251

from sys import stdin
from string import digits

DIGITS: set = set(digits)


def decode_instructions(message: str) -> str:
    """Основная функция для решения задачи."""
    stack: list = []
    current_num_str: str = ''
    current_str: str = ''

    for symbol in message:
        if symbol == '[':
            num: int = int(current_num_str)
            stack.append((current_str, num))
            current_str = ''
            current_num_str = ''
        elif symbol == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        elif symbol in DIGITS:
            current_num_str += symbol
        else:
            current_str += symbol

    return current_str


def main() -> None:
    message: str = stdin.readline().strip()
    print(decode_instructions(message))


if __name__ == "__main__":
    main()
