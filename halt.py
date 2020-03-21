def main():
    length = int(input())
    commands = []
    for i in range(0, length):
        command = [False]
        command.append(input().strip().split())
        commands.append(command)
    print(commands)
    flag = False
    index = 0
    a = 0
    output = []
    while True:
        command = commands[index]
        if command[0]:
            output = {"-1"}
            break
        else:
            command[0] = True

        if command[1][0] == 'assign':
            if index == length - 1:
                break
            a += int(command[1][3]) + int(command[1][5])
            index += 1

        if command[1][0] == 'cout':
            output.append(command[1][1])
            if index == length - 1:
                break
            index += 1

        if command[1][0] == 'goto':
            index = int(command[1][1]) - 1

    print(output)

if __name__ == "__main__": main()
