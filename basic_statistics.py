def sum2(mylist):
    res = 0
    for i in range(len(mylist)):
        res += mylist[i]

    return res


def max2(mylist):
    temp = mylist[0]
    for i in range(1, len(mylist)):
        if temp < mylist[i]:
            temp = mylist[i]

    return temp


def min2(mylist):
    temp = mylist[0]
    for i in range(1, len(mylist)):
        if temp > mylist[i]:
            temp = mylist[i]

    return temp


def ave(mylist):
    return sum2(mylist) / len(mylist)


def main():
    mylist = input("データを入力してください（スペース区切り）> ").split()
    for i in range(len(mylist)):
        mylist[i] = int(mylist[i])

    print("合計値: " + str(sum2(mylist)))
    print("最大値: " + str(max2(mylist)))
    print("最小値: " + str(min2(mylist)))
    print("平均値: " + str(ave(mylist)))


if __name__ == '__main__':
    main()
