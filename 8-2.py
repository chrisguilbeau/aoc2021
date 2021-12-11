from sys import argv


def getMap(sigs):
    sigToNum = {}
    numToSig = {}

    def getDiff(sig, num):
        return len(set(sig) - set(numToSig[num]))

    def update(sig, num):
        assert sig not in sigToNum, (sig, num)
        assert num not in numToSig, (sig, num, numToSig)
        sigToNum[sig] = num
        numToSig[num] = sig
    # pass 1
    for sig in sigs:
        lenSig = len(sig)
        if lenSig == 2:
            update(sig, 1)
        elif lenSig == 4:
            update(sig, 4)
        elif lenSig == 3:
            update(sig, 7)
        elif lenSig == 7:
            update(sig, 8)
    # pass 2 known (1,4,7,8)
    for sig in sigs:
        if sig not in sigToNum:
            lenSig = len(sig)
            if lenSig == 6 and getDiff(sig, 7) == 4:
                update(sig, 6)
            elif lenSig == 5 and getDiff(sig, 7) == 2:
                update(sig, 3)
            elif lenSig == 6 and getDiff(sig, 4) == 2:
                update(sig, 9)
    # pass 3 known (1,3,4,6,7,8,9)
    for sig in sigs:
        if sig not in sigToNum:
            lenSig = len(sig)
            if lenSig == 6:
                update(sig, 0)
            if lenSig == 5 and getDiff(sig, 9) == 0:
                update(sig, 5)
            if lenSig == 5 and getDiff(sig, 9) == 1:
                update(sig, 2)
    assert len(sigToNum) == 10
    # known (0,1,2,3,4,5,6,7,8,9)
    return sigToNum


def main(lines):
    result = 0
    for i, line in enumerate(lines):
        sigs, outs = list(map(lambda l: l.split(), line.split('|')))
        sigs = [''.join(sorted(sig)) for sig in sigs]
        outs = [''.join(sorted(out)) for out in outs]
        m = getMap(sigs)
        result += int(''.join(map(str, map(m.get, outs))))
    print(result)

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
