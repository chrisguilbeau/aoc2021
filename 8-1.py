from sys import argv


def main(lines):
    okSegLengths = {2, 4, 3, 7}
    result = 0
    for _line in lines:
        line = _line.split('|')[-1]
        for seg in line.split():
            print(seg)
            if len(seg) in okSegLengths:
                print('is ok!')
                result += 1
            else:
                print('not ok')
    print(result)



if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
