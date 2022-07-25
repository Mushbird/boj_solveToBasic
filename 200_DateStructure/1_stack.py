# https://www.acmicpc.net/problem/10828

import sys
n = int(sys.stdin.readline())

stackBox=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stackBox.append(command[1])
    elif command[0] == 'pop':
        if len(stackBox) == 0:
            print(-1)
        else:
            print(stackBox.pop())
    elif command[0] == 'size':
        print(len(stackBox))
    elif command[0] == 'empty':
        if len(stackBox) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stackBox) == 0:
            print(-1)
        else:        
            print(stackBox[-1])