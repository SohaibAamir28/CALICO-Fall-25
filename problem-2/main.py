import sys

def solve(word_1: str, word_2: str) -> str:
    n = -1
    if word_2.isdigit():
        n = int(word_2)
    elif word_1.isdigit():
        n = int(word_1) + 1
    else:
        return "crap"
    n_next = n + 1
    if n_next % 15 == 0:
        return "bizzfuzz"
    elif n_next % 3 == 0:
        return "bizz"
    elif n_next % 5 == 0:
        return "fuzz"
    else:
        return str(n_next)


def main():
    try:
        lines = sys.stdin.readlines()
        T = int(lines[0])
        line_index = 1
        results_to_print = []
        for _ in range(T):
            word_1 = lines[line_index].strip()
            line_index += 1
            word_2 = lines[line_index].strip()
            line_index += 1
            results_to_print.append(solve(word_1, word_2))
        print('\n'.join(results_to_print))
    except EOFError:
        pass
    except IndexError:
        pass

if __name__ == '__main__':
    main()
def read_input():
  word_1 = sys.stdin.readline().strip() 
  word_2 = sys.stdin.readline().strip()
  return word_1, word_2