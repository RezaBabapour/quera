def mergeSort(input, f, r):
    if f < r:
        mid = (f + r) // 2
        mergeSort(input, f, mid)
        mergeSort(input, mid + 1, r)
        merge(input, f, mid, r)


def merge(array, f, mid, r):
    left = []
    right = []
    for i in range(f, mid + 1):
        left.append(array[i])
    left.append(100000)

    for j in range(mid + 1, r + 1):
        right.append(array[j])
    right.append(100000)
    i = j = 0
    for a in range(f, r + 1):
        if left[i] > right[j]:
            array[a] = right[j]
            j += 1
        else:
            array[a] = left[i]
            i += 1


def main():
    array = []
    f = open("numbers.txt", "r")
    for i in range(0, 100000):
        number = int(f.readline())
        array.append(number)
    print(array, "\n")
    mergeSort(array, 0, len(array) - 1)
    print("sort array : ", "\n")
    print(array)


if __name__ == "__main__": main()
