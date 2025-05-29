# 138885766
from sys import stdin


def solution(robots: list[int], limit: int) -> int:
    platforms: int = 0
    left: int = 0
    right: int = len(robots) - 1
    while (left <= right):
        if robots[left] + robots[right] <= limit:
            left += 1
        platforms += 1
        right -= 1
    return platforms


def main() -> None:
    robots: list = sorted(list(map(int, stdin.readline().strip().split())))
    limit: int = int(input())
    print(solution(robots, limit))


if __name__ == '__main__':
    main()
