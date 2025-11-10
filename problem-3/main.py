import sys

def solve(N: int, M: int, g: list) -> int:
    m_d = [0] * M
    for i in range(N):
        for j in range(M):
            char = g[i][j]
            if char.isdigit():
                d = int(char)
                m_d[j] = max(m_d[j], d)
    return sum(m_d)

def main():
    try:
        ls = sys.stdin.readlines()
        T = int(ls[0])
        l_i = 1
        results = []
        for _ in range(T):
            N, M = map(int, ls[l_i].split())
            l_i += 1
            g = []
            for i in range(N):
                g.append(ls[l_i + i])
            l_i += N
            results.append(str(solve(N, M, g)))
        print('\n'.join(results))
    except (IOError, ValueError, IndexError):
        pass

if __name__ == '__main__':
    main()

def my_read_input():
    line = sys.stdin.readline().split()
    N, M = int(line[0]), int(line[1])
    g = []
    for _ in range(N):
        g.append(sys.stdin.readline())
    return N, M, g