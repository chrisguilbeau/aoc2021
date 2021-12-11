from sys import argv

def main(lines):
    lenLine = len(lines[0].strip())
    def getVal(g=True):
        candidates = lines[:]
        for i in range(lenLine):
            lenLineHalf = len(candidates) / 2.
            numOnes = sum(int(l[i]) for l in candidates)
            print(numOnes)
            if numOnes >= lenLineHalf:
                candidates = [c for c in candidates if c[i] == ('1'
                              if g else '0')]
            else:
                candidates = [c for c in candidates if c[i] == ('0'
                              if g else '1')]
            if len(candidates) == 1:
                print(candidates[0])
                return int(candidates[0].strip(), 2)
    print(getVal(0) * getVal(1))

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
