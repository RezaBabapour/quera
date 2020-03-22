def main():
    length = int(input())
    donbale = list(map(int, input().strip().split()))
    while length > 1:
        for index in range(0, length - 1):
            donbale[index] = donbale[index + 1] - donbale[index]
        length -= 1

    if donbale[0] >= 0:
        print(donbale[0])
    else:
        print(donbale[0] % 1000000007)


if __name__ == "__main__": main()
