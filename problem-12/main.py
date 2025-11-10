import sys

def binary_XOR(s1: str, s2: str, N: int) -> str:
    """
    Performs a bitwise XOR on two binary strings using fast
    large-integer arithmetic, which is much faster than
    a character-by-character loop for large N.
    """
    # Convert binary strings to integers
    int1 = int(s1, 2)
    int2 = int(s2, 2)
    
    # Perform integer XOR
    xor_int = int1 ^ int2
    
    # Convert result back to binary string, remove '0b' prefix
    xor_bin_str = bin(xor_int)[2:]
    
    # Pad with leading zeros to match length N
    return xor_bin_str.zfill(N)

def is_a_valid_bracketing(bin_str: str) -> bool:
    """
    Checks if a binary string represents a valid Bear Bracket in one pass.
    It verifies both the balance (never dropping < 0) and the
    total count of '0's and '1's simultaneously.
    """
    balancing_temp = 0
    one_count = 0
    n = len(bin_str)
    
    for char in bin_str:
        if char == '0':
            balancing_temp += 1
        else:
            balancing_temp -= 1
            one_count += 1
        
        # If balance ever drops below 0, it's invalid
        if balancing_temp < 0:
            return False
            
    # Final check: must have N/2 '1's (which implies balance is 0)
    return one_count == n // 2

def binary_to_brackets(bin_str: str) -> str:
    """
    Converts a binary string to a bracket sequence.
    """
    # This is a fast, C-backed operation.
    return bin_str.replace('0', '(').replace('1', ')')

def solve():
    """
    Reads one test case, solves it, and returns the result
    as a list of strings for buffered output.
    """
    try:
        N_str = sys.stdin.readline()
        if not N_str:
            return None # End of file
        N = int(N_str)
        X = sys.stdin.readline().strip()
        
        popcount = X.count('1')
        
        # --- 1. Impossibility Check ---
        if (N % 4 == 0) and (popcount % 2 != 0):
            return ["No"]

        # --- 2. Try k=1 ---
        k1_parity_ok = ((N // 2) % 2 == popcount % 2)
        if k1_parity_ok and is_a_valid_bracketing(X):
            return ["Yes", "1", binary_to_brackets(X)]

        # --- 3. Try k=2 ---
        k2_parity_ok = (popcount % 2 == 0)
        
        # Basis string 1: ()()...
        s_simple_bin = "01" * (N // 2)
        s_simple_brackets = "()" * (N // 2)

        if k2_parity_ok:
            f_S2_bin = binary_XOR(X, s_simple_bin, N)
            if is_a_valid_bracketing(f_S2_bin):
                return ["Yes", "2", s_simple_brackets, binary_to_brackets(f_S2_bin)]

        # --- 4. Try k=3 ---
        k3_parity_ok = k1_parity_ok
        
        # Basis string 2: ((...))
        s_nested_bin = "0" * (N // 2) + "1" * (N // 2)
        s_nested_brackets = "(" * (N // 2) + ")" * (N // 2)

        if k3_parity_ok:
            f_S1_XOR_f_S2 = binary_XOR(s_simple_bin, s_nested_bin, N)
            f_S3_bin = binary_XOR(X, f_S1_XOR_f_S2, N)
            
            if is_a_valid_bracketing(f_S3_bin):
                return ["Yes", "3", s_simple_brackets, s_nested_brackets, binary_to_brackets(f_S3_bin)]

        # --- 5. All attempts failed ---
        return ["No"]
        
    except (IOError, ValueError, IndexError):
        return None

def main():
    """
    Reads all test cases, collects all output lines,
    and prints them all at once at the end for fast I/O.
    """
    try:
        T_str = sys.stdin.readline()
        if not T_str:
            return
        T = int(T_str)
        
        all_results = []
        for _ in range(T):
            result_lines = solve()
            if result_lines:
                all_results.extend(result_lines)
            else:
                break # End of input
        
        # Print all lines at once
        print('\n'.join(all_results))

    except (IOError, ValueError):
        pass

if __name__ == '__main__':
    main()

def read_my_input():
    N = int(sys.stdin.readline())
    X = sys.stdin.readline().strip()
    return N, X

# import sys

# def binary_XOR(s1, s2):
#     """
#     Performs a bitwise XOR on two binary strings.
#     """
#     n = len(s1)
#     res = []
#     for i in range(n):
#         bit1 = int(s1[i])
#         bit2 = int(s2[i])
#         xor_bit = bit1 ^ bit2
#         res.append(str(xor_bit))
#     return "".join(res)

# def is_a_valid_bracketing(bin_str):
#     """
#     Checks if a binary string represents a valid Bear Bracket.
#     """
#     n = len(bin_str)
#     # 1. Check for equal number of 0s and 1s
#     if bin_str.count('1') != n // 2:
#         return False
    
#     # 2. Check for balance
#     balancing_temp = 0
#     for char in bin_str:
#         if char == '0':
#             balancing_temp += 1
#         else:
#             balancing_temp -= 1
        
#         # If balance ever drops below 0, it's invalid
#         if balancing_temp < 0:
#             return False
            
#     # Final balance must be 0 (guaranteed by popcount check)
#     return balancing_temp == 0

# def binary_to_brackets(bin_str):
#     """
#     Converts a binary string to a bracket sequence.
#     """
#     return bin_str.replace('0', '(').replace('1', ')')

# def solve():
#     """
#     Reads one test case, solves it, and prints the result.
#     """
#     try:
#         N = int(sys.stdin.readline())
#         X = sys.stdin.readline().strip()
        
#         popcount = X.count('1')
        
#         # --- 1. Impossibility Check ---
#         # If N is a multiple of 4 (N/2 is even) and popcount is odd, impossible.
#         if (N % 4 == 0) and (popcount % 2 != 0):
#             print("No")
#             return

#         # --- 2. Try k=1 ---
#         # Parity check: (k * (N/2)) % 2 == popcount % 2
#         # k=1: (N/2) % 2 == popcount % 2
#         k1_parity_ok = ( (N // 2) % 2 == popcount % 2 )
        
#         if k1_parity_ok and is_a_valid_bracketing(X):
#             print("Yes")
#             print(1)
#             print(binary_to_brackets(X))
#             return

#         # --- 3. Try k=2 ---
#         # Parity check: k=2
#         # (2 * (N/2)) % 2 == popcount % 2
#         # (N) % 2 == popcount % 2 (N is always even, so 0)
#         # 0 == popcount % 2  (popcount must be even)
#         k2_parity_ok = (popcount % 2 == 0)
        
#         # Basis string 1: ()()...
#         s_simple = "01" * (N // 2)
#         s_simple_brackets = "()" * (N // 2)

#         if k2_parity_ok:
#             f_S2 = binary_XOR(X, s_simple)
#             if is_a_valid_bracketing(f_S2):
#                 print("Yes")
#                 print(2)
#                 print(s_simple_brackets)
#                 print(binary_to_brackets(f_S2))
#                 return

#         # --- 4. Try k=3 ---
#         # Parity check: k=3 (same as k=1)
#         k3_parity_ok = k1_parity_ok
        
#         # Basis string 2: ((...))
#         s_nested = "0" * (N // 2) + "1" * (N // 2)
#         s_nested_brackets = "(" * (N // 2) + ")" * (N // 2)

#         if k3_parity_ok:
#             # Try S1 = simple, S2 = nested
#             # f_S3 = X ^ f(S1) ^ f(S2)
#             f_S3 = binary_XOR(X, binary_XOR(s_simple, s_nested))
#             if is_a_valid_bracketing(f_S3):
#                 print("Yes")
#                 print(3)
#                 print(s_simple_brackets)
#                 print(s_nested_brackets)
#                 print(binary_to_brackets(f_S3))
#                 return

#         # --- 5. All attempts failed ---
#         print("No")
        
#     except (IOError, ValueError, IndexError):
#         pass

# def main():
#     try:
#         T = int(sys.stdin.readline())
#         for _ in range(T):
#             solve()
#     except (IOError, ValueError):
#         pass

# if __name__ == '__main__':
#     main()

# def read_my_input():
#     N = int(sys.stdin.readline())
#     X = sys.stdin.readline().strip()
#     return N, X