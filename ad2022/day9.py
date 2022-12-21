import math

directions = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
commands = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}
visited = [[0, 0]]
snake=[]
for i in range(10):
    snake.append([0,0])

f = open("day9.input", "r")
for command in f:
    command = command.split()
    for i in range(int(command[1])):
        for node in range(len(snake)):
            if node == 0:
                snake[node][0] += commands[command[0]][0]
                snake[node][1] += commands[command[0]][1]
            else:
                t_sticks = False
                for dir in directions:
                    if snake[node-1][0] == snake[node][0] + dir[0] and snake[node-1][1] == snake[node][1] + dir[1]:
                        t_sticks = True
                        break
                if t_sticks == False:
                    x = (snake[node-1][0] - snake[node][0]) / 2
                    y = (snake[node-1][1] - snake[node][1]) / 2
                    if x >= 0:
                        x = math.ceil(x)
                    else:
                        x = math.floor(x)
                    if y >= 0:
                        y = math.ceil(y)
                    else:
                        y = math.floor(y)
                    x = int(x)
                    y = int(y)
                    snake[node][0] = snake[node][0] + x
                    snake[node][1] = snake[node][1] + y
            if node==len(snake)-1:
                    if snake[node] not in visited:
                        new_val = []
                        new_val.append(snake[node][0])
                        new_val.append(snake[node][1])
                        visited.append(new_val)
print(len(visited))
