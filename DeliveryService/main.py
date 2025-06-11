# 138906562
from sys import stdin


def solution(robots: list[int], limit: int) -> int:
    """Функция для решения задачи.

    Вычисляет минимальное количество транспортных
    платформ для перевозки роботов.
    """
    robots = sorted(robots)
    platforms: int = 0
    lightest: int = 0
    heaviest: int = len(robots) - 1
    while lightest <= heaviest:
        if robots[lightest] + robots[heaviest] <= limit:
            lightest += 1
        platforms += 1
        heaviest -= 1
    return platforms


def main() -> None:
    robots: list = [int(i) for i in stdin.readline().strip().split()]
    limit: int = int(input())
    print(solution(robots, limit))


if __name__ == '__main__':
    main()
