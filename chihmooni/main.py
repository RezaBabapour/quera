def main():
    lenght = int(input().strip())
    data = []
    for i in range(0, lenght):
        line = list(map(str, input().strip().split()))

        tmpTime = line[1].split(":")
        time = int(tmpTime[0]) * 60 + int(tmpTime[1])
        item = {"time": time, "stat": line[2]}
        data.append(item)
    mergSort(data, 0, lenght - 1)
    maximum = {"time": 0, "num": 0}
    present = {"time": 0, "num": 0}
    for i in data:
        if i["stat"] == "+":
            present["time"] = i["time"]
            present["num"] += 1
            if present["num"] > maximum["num"]:
                maximum["num"] = present["num"]
                maximum["time"] = present["time"]

        if i["stat"] == "-":
            present["time"] = i["time"]
            present["num"] -= 1

    HH = int(maximum["time"]) // 60
    MM = int(maximum["time"]) % 60
    time = str(HH) + ":" + str(MM)
    print(time)


def mergSort(array, f, r):
    if f < r:
        mid = (f + r) // 2
        mergSort(array, f, mid)
        mergSort(array, mid + 1, r)
        merge(array, f, mid, r)


def merge(array, f, mid, r):
    left = []
    right = []
    for i in range(f, mid + 1):
        left.append(array[i])
    left.append({"time": 4000})
    for j in range(mid + 1, r + 1):
        right.append(array[j])
    right.append({"time": 4000})

    i = j = 0
    for a in range(f, r + 1):
        leftTime = left[i]["time"]
        rightTime = right[j]["time"]
        if leftTime > rightTime:
            array[a] = right[j]
            j += 1
        else:
            array[a] = left[i]
            i += 1


if __name__ == "__main__": main()
