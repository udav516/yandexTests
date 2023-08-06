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


# Task E
def checkAnagram(s1, s2):
    charCount = {}
    for char in s1:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    for char in s2:
        if char in charCount:
            charCount[char] -= 1
            if charCount[char] < 0:
                return False
        else:
            return False

    for count in charCount.values():
        if count != 0:
            return False

    return True


s1 = input()
s2 = input()

result = checkAnagram(s1, s2)
if result:
    print(1)
else:
    print(0)

# Task G
from collections import deque

n = int(input())
cities = []
for _ in range(n):
    x, y = map(int, input().split())
    cities.append((x, y))

k = int(input())
start, end = map(int, input().split())


def distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])


def can_reach(city1, city2, max_distance):
    return distance(city1, city2) <= max_distance


def bfs(start, end, max_distance):
    queue = deque()
    queue.append(start)
    distances = [float('inf')] * n
    distances[start] = 0

    while queue:
        current_city = queue.popleft()

        if current_city == end:
            return distances[end]

        for neighbor in range(n):
            if can_reach(cities[current_city], cities[neighbor], max_distance) and distances[neighbor] == float('inf'):
                queue.append(neighbor)
                distances[neighbor] = distances[current_city] + 1

    return -1


result = bfs(start - 1, end - 1, k)
print(result)
