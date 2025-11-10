import sys

def solve(E: str, Y: int, M: int, D: int) -> str:
    event_date = (Y, M, D)
    gta_date = (2026, 11, 19)
    if event_date < gta_date:
        return f"we got {E} before gta6"
    else:
        return f"we got gta6 before {E}"


def main():
    T = int(input())
    for _ in range(T):
        E = input().strip()
        Y, M, D = map(int, input().split())
        print(solve(E, Y, M, D))


if __name__ == '__main__':
    main()

def read_my_input():
  e = input().strip()
  y, m, d = map(int, input().split())
  return e, y, m, d
