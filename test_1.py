# Task A
def jewels_and_stones(J: str, S: str) -> int:
    jewels = set(J)
    count = 0
    for stone in S:
        if stone in jewels:
            count += 1
    return count


J = input()
S = input()

result = jewels_and_stones(J, S)

print(result)

# Task B
n = int(input())

max_len = 0
cur_len = 0

for _ in range(n):
    num = int(input())
    if num == 1:
        cur_len += 1
    else:
        max_len = max(max_len, cur_len)
        cur_len = 0

max_len = max(max_len, cur_len)

print(max_len)

# Task C
n = int(input())
numbers = []

previous_number = None

for _ in range(n):
    current_number = int(input())

    if current_number != previous_number:
        numbers.append(current_number)
        previous_number = current_number

for number in numbers:
    print(number)


# Task D
def generateParentheses(n, s, open_count, close_count):
    if len(s) == 2 * n:
        parentheses.append(s)
        return

    if open_count < n:
        generateParentheses(n, s + '(', open_count + 1, close_count)

    if close_count < open_count:
        generateParentheses(n, s + ')', open_count, close_count + 1)


n = int(input())
parentheses = []
generateParentheses(n, '', 0, 0)
parentheses.sort()

for p in parentheses:
    print(p)
