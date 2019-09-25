import random


def main():
    N = int(input("サイコロの面の数は?: "))
    M = int(input("何回振りますか?: "))
    res = []

    for i in range(M):
        res.append(random.randrange(N) + 1)

    print(res)


if __name__ == '__main__':
    main()
