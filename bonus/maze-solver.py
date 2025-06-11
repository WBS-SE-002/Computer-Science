first_maze = ["xxxxxxxxxxx",
              "xx      xxx",
              "x xx xxxxxx",
              "x xx xxx xx",
              "         xx",
              "xxxxxxxxxxx",
              "xxxxxxx xxx",
              "xx        x"]


start_first = {"x": 7, "y": 1}
end_first = {"x": 9, "y": 7}

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def maze_solver(maze, start, end, wall):
    seen = []

    for i in maze:
        seen.append([0 for x in maze[0]])

    path = []

    walk(maze, start, end, seen, path, wall)

    return path


def walk(maze, position, end, seen, path, wall):
    length_y = len(maze)
    lenght_x = len(maze[0])

    if position["x"] >= lenght_x:
        return False

    if position["y"] >= length_y:
        return False

    if position["y"] < 0 or position["x"] < 0:
        return False

    if position == end:
        path.append({"x": position["x"], "y": position["y"]})
        return True

    x = position["x"]
    y = position["y"]

    if seen[y][x]:
        return False

    if maze[y][x] == wall:
        return False

    path.append({"x": x, "y": y})
    seen[y][x] = True

    for i in directions:
        new_x = i[0]
        new_y = i[1]
        if walk(maze, {"x": x + new_x, "y": y + new_y}, end, seen, path, wall):
            return True

    path.pop(-1)


print(maze_solver(first_maze, start_first, end_first, wall="x"))
