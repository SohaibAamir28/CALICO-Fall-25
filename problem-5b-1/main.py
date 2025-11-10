import sys
MOD = 998244353
MAX_K = 10004
fib = [0] * (MAX_K + 2)
fib[1] = 1
for i in range(2, MAX_K + 2):
    fib[i] = (fib[i-1] + fib[i-2]) % MOD

def get_fib(i):
    if i == -1:
        return 1
    if i < 0:
        return 0
    return fib[i]

def solve():
    try:
        l = sys.stdin.readline().split()
        if not l:
            return False
        S = l[0]
        K = int(l[1])
        t_s = 0
        for c in S:
            L_k, U_k = 0, 0
            v = 0
            
            if c.islower():
                v = ord(c) - ord('a') + 1
                L_k = get_fib(K-1)
                U_k = get_fib(K)
            else:
                v = ord(c) - ord('A') + 1
                L_k = get_fib(K)
                U_k = get_fib(K+1)
            t_1 = (L_k * v) % MOD
            t2_v = (v + 26)
            t_2 = (U_k * t2_v) % MOD
            
            c_s = (t_1 + t_2) % MOD
            t_s = (t_s + c_s) % MOD
            
        print(t_s)
        return True
    except (EOFError, IndexError):
        return False
    except Exception:
        return False

def main():
    try:
        T_l = sys.stdin.readline()
        if not T_l:
            return
        T = int(T_l)
        for _ in range(T):
            if not solve():
                break
    except Exception:
        pass

if __name__ == '__main__':
    main()

def read_my_input():
    l = sys.stdin.readline().split()
    S = l[0]
    K = int(l[1])
    return S, K