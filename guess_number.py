def main():
    length = input()
    if length == '':
        exit()
    else:
        length = int(length)
    divs = list(map(int, input().strip().split()))
    accept = []
    for num in range(1, 1001):
        limit = 0
        for div in range(0, length):
            if num % divs[div] == 0:
                limit += 1
        if limit == length:
            accept.append(num)
    print(len(accept))


if __name__ == "__main__": main()
