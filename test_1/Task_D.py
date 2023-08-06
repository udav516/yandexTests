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
