from sys import argv


def main(ints):
    counter = 0
    for i in range(0, len(ints) - 3):
        l1 = ints[i:i + 3]
        l2 = ints[i + 1:i + 4]
        if len(l1) == len(l2):
            sum1 = sum(l1)
            sum2 = sum(l2)
            print(l1, sum1)
            print(l2, sum2)
            if sum1 < sum2:
                counter += 1
    print(counter)


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        ints = list(map(int, f.readlines()))
    main(ints)
