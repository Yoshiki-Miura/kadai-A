def main():
    for i in range(1, 10):
        for j in range(1, 10):
            if j == 9:
                print(i * j)
            else:
                print(f"{i * j} ", end="")


if __name__ == '__main__':
    main()
