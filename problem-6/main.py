import sys

def solve():
    try:
        K = int(sys.stdin.readline())
        N = K - 1
        rem = N % 5
        if rem == 0 or rem == 1:
            print("Oski")
        else:
            print("Big Ben")    
    except (IOError, ValueError):
        pass

def main():
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            solve()
    except (IOError, ValueError):
        pass

if __name__ == '__main__':
    main()

def read_my_input():
  K = int(sys.stdin.readline())
  return K