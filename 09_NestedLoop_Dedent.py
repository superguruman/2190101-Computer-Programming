for i in range(int(input())):
    line = input()
    for j in range(len(line)):
        if line[j] != '.':
            break
    print('.'*(j//2)+line[j:])