def main():
    x = int(input().strip())
    n = int(input().strip())

    if n == 0:
        print("20")
        exit()

    if n == 7:
        print(x)
        exit()

    x -= n

    if x <= 0:
        print("0")
    else:
        print(x)



if __name__ == "__main__": main()