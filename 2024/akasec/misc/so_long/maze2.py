from PIL import Image
from collections import deque
from math import sqrt
START, GOAL = None, None

def detect_walls(image_path):
    global START, GOAL
    image = Image.open(image_path)
    width, height = image.size
    maze_data = []

    px = int(sqrt(count_red_pixels(image_path)))
    for y in range(0, height, px):
        row = []
        for x in range(0, width, px):
            pixel = image.getpixel((x, y))
            if pixel == (0, 0, 0): # wall
                row.append(1)
            elif pixel == (0, 255, 0): # start
                row.append(2)
                START = [y // px, x // px]
            elif pixel == (255, 0, 0): # goal
                row.append(3)
                GOAL = [y // px, x // px]
            else:
                row.append(0)
        maze_data.append(row)

    return maze_data

def count_red_pixels(image_path):
    image = Image.open(image_path)
    width, height = image.size
    count = 0

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 0:
                count += 1

    return count
from pwn import *
def solve(image_path):
    global START, GOAL
    maze = detect_walls(image_path)
    dd = 'up, down, left, right, up-left, up-right, down-left, down-right'.split(', ')
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    cur = START # y, x
    visited = [[[] for i in range(len(maze[0]))] for j in range(len(maze))]
    Q = deque()
    visited[cur[0]][cur[1]] = ['GO']
    Q.append(cur)

    while 1:
        cur = Q.popleft()

        if cur == GOAL:
            break

        for i in range(8):
            nx = cur[1] + dx[i]
            ny = cur[0] + dy[i]

            if nx < 0 or nx >= len(maze[0]) or ny < 0 or ny >= len(maze):
                continue

            if maze[ny][nx] == 1 or visited[ny][nx]:
                continue

            visited[ny][nx] = visited[cur[0]][cur[1]] + [dd[i]]
            Q.append([ny, nx])

    return visited[GOAL[0]][GOAL[1]]
