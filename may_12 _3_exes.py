from collections import Counter

def find_password(s: str, required: str, k: int) -> str:
    required_set = set(required)
    window_count = Counter()

    n = len(s)
    best_substr = ""
    best_pos = -1

    left = 0
    total_unique = 0

    for right in range(n):
        c = s[right]
        window_count[c] += 1

        if c in required_set and window_count[c] == 1:
            total_unique += 1

        while right - left + 1 > k:
            left_char = s[left]
            if left_char in required_set and window_count[left_char] == 1:
                total_unique -= 1
            window_count[left_char] -= 1
            left += 1

        if total_unique == len(required_set):
            current_substr = s[left:right+1]
            if (best_pos < left) or (best_pos == left and len(current_substr) > len(best_substr)):
                best_substr = current_substr
                best_pos = left

    return best_substr if best_substr else "-1"


# Версия с input()
if __name__ == "__main__":
    s = input().strip()
    required = input().strip()
    k = int(input())
    print(find_password(s, required, k))
