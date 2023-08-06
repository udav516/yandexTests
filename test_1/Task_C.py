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
