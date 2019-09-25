def main():
    for i in range(1, 10):
        for j in range(1, 10):
            if j == 9:
                print(f"{'{0:2d}'.format(i)} *{'{0:2d}'.format(j)} ={'{0:3d}'.format(i * j)} |")
            else:
                print(f"{'{0:2d}'.format(i)} *{'{0:2d}'.format(j)} ={'{0:3d}'.format(i * j)} |", end="")


if __name__ == '__main__':
    main()
