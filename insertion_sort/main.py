def insertionSort(array):
    for x in range(1, len(array)):
        key = array[x]
        for j in range(x, -1, -1):
            if key < array[j]:
                array[j + 1] = array[j]
                array[j] = key
    print(array)


def main():
    array = []
    f = open("numbers.txt", "r")
    for i in range (0, 100000):
        number = int(f.readline())
        array.append(number)
    print(array)
    insertionSort(array)



if __name__ == "__main__": main()
