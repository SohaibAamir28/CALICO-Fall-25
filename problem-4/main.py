import sys
from collections import defaultdict

def c_s_r(line_rocks, l_t):
    a = 0
    for i in range(len(line_rocks)):
        p_t, x, y = line_rocks[i]
        c_t_p_a = False
        if l_t == 'horiz' or l_t == 'vert':
            if p_t in ('R', 'Q'):
                c_t_p_a = True
        elif l_t == 'diag':
            if p_t in ('B', 'Q'):
                c_t_p_a = True   
        if c_t_p_a:
            if i > 0:
                a += 1
            if i < len(line_rocks) - 1:
                a += 1
    return a

def solve():
    try:
        N, M = map(int, sys.stdin.readline().split())
        K = int(sys.stdin.readline())
        rocks = []
        for _ in range(K):
            line = sys.stdin.readline().split()
            rocks.append((line[0], int(line[1]), int(line[2]))) 
    except (IOError, ValueError, IndexError):
        return 0
    t_a = 0
    r_b_r = defaultdict(list)
    rocks_by_col = defaultdict(list)
    r_b_d_s = defaultdict(list)
    rocks_by_diag_diff = defaultdict(list)
    for p_t, x, y in rocks:
        r_b_r[y].append((p_t, x, y))
        rocks_by_col[x].append((p_t, x, y))
        r_b_d_s[x + y].append((p_t, x, y))
        rocks_by_diag_diff[x - y].append((p_t, x, y))
    for y in r_b_r:
        if len(r_b_r[y]) > 1:
            row = sorted(r_b_r[y], key=lambda p: p[1])
            t_a += c_s_r(row, 'horiz')
    for x in rocks_by_col:
        if len(rocks_by_col[x]) > 1:
            col = sorted(rocks_by_col[x], key=lambda p: p[2])
            t_a += c_s_r(col, 'vert')
    for diag_sum in r_b_d_s:
        if len(r_b_d_s[diag_sum]) > 1:
            diag = sorted(r_b_d_s[diag_sum], key=lambda p: p[1])
            t_a += c_s_r(diag, 'diag')
    for diag_diff in rocks_by_diag_diff:
        if len(rocks_by_diag_diff[diag_diff]) > 1:
            diag = sorted(rocks_by_diag_diff[diag_diff], key=lambda p: p[1])
            t_a += c_s_r(diag, 'diag')
    return t_a

def main():
    try:
        T = int(sys.stdin.readline())
        results = []
        for _ in range(T):
            results.append(str(solve()))
        print('\n'.join(results))
    except (IOError, ValueError):
        pass

if __name__ == '__main__':
    main()

def read_my_input():
  l1 = sys.stdin.readline().split()
  N, M = int(l1[0]), int(l1[1])
  K = int(sys.stdin.readline())
  rocks = []
  for _ in range(K):
      line = sys.stdin.readline().split()
      rocks.append((line[0], int(line[1]), int(line[2])))
  return N, M, K, rocks