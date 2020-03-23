def main():
    tmp = list(map(int, input().strip().split()))
    n = tmp[0]
    k = tmp[1]
    price = list(map(int, input().strip().split()))

    if k == 1:
        print(max(price))
        exit()

    if k >= 3:
        print(min(price))
        exit()

    first = price[0]
    last = price[n - 1]
    if first <= last:
        print(first)
    else:
        print(last)
    # maxl = 0
    # maxr = 0
    # mini = 6000
    # left = []
    # right = []
    # for cat in range(0, n - 1):
    #     for i in range(0, cat + 1):
    #         left.append(price[i])
    #     for j in range(cat + 1, n):
    #         right.append(price[j])
    #     maxl = max(left)
    #     maxr = max(right)
    #
    #     if maxl < mini:
    #         mini = maxl
    #     if maxr < mini:
    #         mini = maxr
    #     left = []
    #     right = []
    # print(mini)


if __name__ == "__main__": main()
