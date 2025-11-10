import sys

def event_check_and_gtavi(e_n: str, year: int, month: int, day: int) -> str:
    event_tuple = (year, month, day)
    gta_release = (2026, 11, 19)

    if event_tuple < gta_release:
        return f"we got {e_n} before gta6"
    else:
        return f"we got gta6 before {e_n}"


def main():
    input_lines = sys.stdin.readlines()
    
    num_cases = int(input_lines[0])
    
    current_line = 1
    answers = []
    
    for i in range(num_cases):
        event = input_lines[current_line].rstrip('\n')
        current_line += 1
        
        y, m, d = map(int, input_lines[current_line].split())
        current_line += 1
        
        result = event_check_and_gtavi(event, y, m, d)
        answers.append(result)
    
    print('\n'.join(answers))


if __name__ == '__main__':
    main()

def read_input_single():
    e_n = sys.stdin.readline().rstrip('\n') 
    year, month, day = map(int, sys.stdin.readline().split())
    return e_n, year, month, day
