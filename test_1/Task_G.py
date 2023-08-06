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
