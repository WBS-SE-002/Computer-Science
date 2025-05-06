"""
informations:

2d array - nested lists
2d = [[xxx],
      [xxx], 
      [xxx]]

array - directions

reach endpoint -> Finish
hit walls or go outside -> Dead
no directions anymore -> Lost

0 - safe to walk
1 - Wall
2 - Start Point
3 - Finish Point

directions - array ["N", "E", "N"]

maze - N X N

starting point and end point not given

directions
north - "N" - (-1, 0)
east - "E" - (0, 1)
south - "S" - (1, 0)
west - "W" - (0, -1)

following directions = moves

strategy:

- Find the starting position
- walk through the maze
    - go from start
    - loop over directions
    - check current position - finish, dead

loop ends (no directions)
-> Lost
"""


first_maze = [[1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 3],
              [1, 0, 1, 0, 1, 0, 1],
              [0, 0, 1, 0, 0, 0, 1],
              [1, 0, 1, 0, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 1],
              [1, 2, 1, 0, 1, 0, 1]]


# for y in range(len(maze)):
#     for x in range(len(maze[y])):
#         if maze[y][x] == 2:
#             print((y, x))


mapDir = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}


def find_starting_point(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 2:
                return [y, x]


def walk(maze, directions, position):

    # move
    for dir in directions:
        (move_y, move_x) = mapDir[dir]
        position[0] += move_y
        position[1] += move_x

    # check current coordinates
        coordinate_y = position[0]
        coordinate_x = position[1]

        height = len(maze)
        width = len(maze[0])

        if coordinate_y >= height or coordinate_y < 0:
            return "Dead"

        if coordinate_x >= width or coordinate_x < 0:
            return "Dead"

        currentPosition = maze[coordinate_y][coordinate_x]

        if currentPosition == 3:
            return "Finish"

        if currentPosition == 1:
            return "Dead"

    return "Lost"


def maze_runner(maze, directions):
    position = find_starting_point(maze)
    result = walk(maze, directions, position)
    return result


# Finish
dir_1 = ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]

# Finish
dir_2 = ["N", "N", "N", "N", "N", "E", "E", "S", "S", "E", "E", "N", "N", "E"]

# Dead
dir_3 = ["N", "N", "N", "W", "W"]

# Lost
dir_4 = ["N", "E", "E", "E", "E"]


# print(maze_runner(first_maze, dir_1))
# print(maze_runner(first_maze, dir_2))
# print(maze_runner(first_maze, dir_3))
print(maze_runner(first_maze, dir_4))
