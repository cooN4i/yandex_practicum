# 139247977
from sys import stdin


def solve_task(message: str) -> str:
    """Основная функция для решения задачи.

    Функция, начиная с конца сообщения, ищет пары открывающих и закрывающих
    скобок. Затем, если такие в сообщении имеются, она считывает число, стоящее
    перед открывающей скобкой, умножает его на команды, заключенные в скобках,
    и вставляет полученный фрагмент обратно в сообщение."""
    closing_bracket_index: int = 0
    opening_bracket_index: int = 0
    while '[' in message:
        index: int = len(message) - 1
        while message[index] != '[':
            if message[index] == ']':
                closing_bracket_index = index
            index -= 1
        opening_bracket_index = index
        commands_for_multiplication: str = message[opening_bracket_index +
                                                   1:closing_bracket_index]
        multiplier: str = ''
        index -= 1
        while message[index].isdigit():
            multiplier = message[index] + multiplier
            index -= 1
        commands_for_multiplication *= int(multiplier)
        message = message[:index + 1] + commands_for_multiplication + \
            message[closing_bracket_index + 1:]
    return message


def main() -> None:
    message: str = stdin.readline().strip()
    print(solve_task(message))


if __name__ == '__main__':
    main()
