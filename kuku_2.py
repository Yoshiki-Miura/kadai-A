def main():
    line = int(input("行を入力してください: "))
    row = int(input("列を入力してください: "))
    for i in range(1,line+1):
        for j in range(1,row+1):
            if j == row:
                print(i*j)
            else:
                print(f"{i*j} ",end="")


if __name__ == '__main__':
    main()