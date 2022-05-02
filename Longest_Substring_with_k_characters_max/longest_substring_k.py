# Find the longest substring with at most k distinct characters.
import time

def backtrack(string: str, k: int, i: int) -> int:
    """
        Returns the new starting index for counting next substring.
    """
    distinct_chars = set()
    
    while i >= 0:
        distinct_chars.add(string[i])

        if len(distinct_chars) > k:
            return i + 1

        i -= 1


def find_longest_substring(string: str, k: int) -> int:
    
    max_length = 0
    current_length = 0

    distinct_chars = set()
    i = 0

    while i < len(string):
        distinct_chars.add(string[i])

        if len(distinct_chars) > k:
            max_length = current_length if current_length > max_length else max_length
            current_length = 0

            i = backtrack(string, k, i)
            distinct_chars.clear()
            continue

        current_length += 1
        i += 1
    
    max_length = current_length if current_length > max_length else max_length

    return max_length


def main() -> None:
    string = "abbacbadfgaghfgabcdefgcdababadcghi"
    n = find_longest_substring(string, 5)

    print(n)

if __name__ == "__main__":
    tic = time.time()    
    main()
    toc = time.time()

    print(f"Completed in {toc - tic:.4f} seconds")