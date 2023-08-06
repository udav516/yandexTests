# Task 1
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
