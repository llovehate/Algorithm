import sys
from collections import deque

N = int(sys.stdin.readline().strip())
commands = sys.stdin.read().splitlines()
q = deque()

for command in commands:
    command_split = command.split()
    if len(command_split) > 1 and command_split[1].isdigit():
        q.append(command_split[1])
    elif command == "pop":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif command == "back":
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)