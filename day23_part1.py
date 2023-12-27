from collections import deque


def start(lines):
    return (0, lines[0].index("."))


def goal(lines):
    return (len(lines) - 1, lines[-1].index("."))


def longest_hike(input):
    matrix = [[i for i in line] for line in input]
    r_start, c_start = start(matrix)
    r_end, c_end = goal(matrix)
    direction_map = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    # edge contraction algorithm
    # we will create new weighted graph/adjacency list which will contain
    # only nodes with mulitple possible neighbors(more than 2) + start and end node
    graph = {}
    graph[(r_start, c_start)] = {}
    graph[(r_end, c_end)] = {}
    visited1 = set()
    queue1 = deque([(r_start, c_start)])
    while queue1:
        r, c = queue1.popleft()
        if (r, c) in visited1:
            continue
        visited1.add((r, c))
        neighbors = 0
        for dr, dc in direction_map.values():
            if 0 <= r + dr < len(matrix) and 0 <= c + dc < len(matrix[0]) and matrix[r + dr][c + dc] != "#":
                neighbors += 1
                if (r + dr, c + dc) not in visited1:
                    queue1.append((r + dr, c + dc))
        if neighbors > 2:
            graph[(r, c)] = {}

    # now we need to fill values in graph with distances
    # so we iterate from each node up to other nodes in new graph
    # here bfs is used
    for node in graph:
        r, c = node
        visited2 = set()
        # stack contains node coordinates and distance
        queue2 = deque([(r, c, 0)])
        while queue2:
            r, c, dist = queue2.popleft()
            if (r, c) in visited2:
                continue
            visited2.add((r, c))

            if dist != 0 and (r, c) in graph:
                graph[node][(r, c)] = dist
                # we don't need to go further from this node
                # but we do not break from loop cause we might reach more new nodes
                continue

            if matrix[r][c] in direction_map:
                directions = [direction_map[matrix[r][c]]]
            elif matrix[r][c] == ".":
                directions = direction_map.values()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] != "#" and (nr, nc) not in visited2:
                    queue2.append((nr, nc, dist + 1))

    # now we brute force throught new graph looking for longest path
    # we use recursive dfs for this
    visited = set()

    def dfs(node):
        if node == (r_end, c_end):
            return 0
        visited.add(node)
        # distance is initialized with -inf
        # cause any valid path should have higher value than invalid one
        distance = float("-inf")
        for neighbor in graph[node]:
            if neighbor not in visited:
                distance = max(distance, graph[node][neighbor] + dfs(neighbor))
        visited.remove(node)
        return distance
    return dfs((r_start, c_start))


# Testing
test1 = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
ans1 = 94
assert longest_hike(test1.splitlines()) == ans1

# Read input
with open("day23.txt") as f:
    input = f.read().splitlines()
    print(longest_hike(input))
