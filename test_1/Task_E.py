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
