import sys
from collections import defaultdict

def c_s_r(l_p, l_t):
    a = 0
    for i in range(len(l_p)):
        p_type, x, y = l_p[i]
        c_t_p_a = False
        if l_t == 'horiz' or l_t == 'vert':
            if p_type in ('R', 'Q'):
                c_t_p_a = True
        elif l_t == 'diag':
            if p_type in ('B', 'Q'):
                c_t_p_a = True
        if c_t_p_a:
            if i > 0:
                a += 1
            if i < len(l_p) - 1:
                a += 1
    return a

def solve():
    try:
        N, M = map(int, sys.stdin.readline().split())
        K = int(sys.stdin.readline())
        p = []
        for _ in range(K):
            line = sys.stdin.readline().split()
            p.append((line[0], int(line[1]), int(line[2]))) 
    except (IOError, ValueError, IndexError):
        return 0
    t_a = 0
    p_b_r = defaultdict(list)
    p_b_c = defaultdict(list)
    p_b_d_s = defaultdict(list)
    p_b_d_dif = defaultdict(list)
    for p_type, x, y in p:
        p_b_r[y].append((p_type, x, y))
        p_b_c[x].append((p_type, x, y))
        p_b_d_s[x + y].append((p_type, x, y))
        p_b_d_dif[x - y].append((p_type, x, y))
    for y in p_b_r:
        if len(p_b_r[y]) > 1:
            row = sorted(p_b_r[y], key=lambda p: p[1]) # sort by x
            t_a += c_s_r(row, 'horiz')
    for x in p_b_c:
        if len(p_b_c[x]) > 1:
            col = sorted(p_b_c[x], key=lambda p: p[2]) # sort by y
            t_a += c_s_r(col, 'vert')
    for diag_sum in p_b_d_s:
        if len(p_b_d_s[diag_sum]) > 1:
            diag = sorted(p_b_d_s[diag_sum], key=lambda p: p[1]) # sort by x
            t_a += c_s_r(diag, 'diag')
    for diag_diff in p_b_d_dif:
        if len(p_b_d_dif[diag_diff]) > 1:
            diag = sorted(p_b_d_dif[diag_diff], key=lambda p: p[1]) # sort by x
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
        pass # End of file

if __name__ == '__main__':
    main()

def read_my_input():
  line1 = sys.stdin.readline().split()
  N, M = int(line1[0]), int(line1[1])
  K = int(sys.stdin.readline())
  p = []
  for _ in range(K):
      line = sys.stdin.readline().split()
      p.append((line[0], int(line[1]), int(line[2])))
  return N, M, K, p