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