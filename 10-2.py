from sys import argv

beginers = '([{<'
enders = ')]}>'
b2e = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    }
e2b = {v: k for k, v in b2e.items()}


values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    }


def main(lines):
    scores = []
    for line_ in lines:
        line = line_.strip()
        stack = []
        for char in line:
            if char in enders:
                beginner = stack.pop(-1)
                try:
                    assert beginner == e2b[char], f'{beginner} nok {char}'
                except Exception:
                    # print(
                    #     line,
                    #     '- Expected',
                    #     b2e[beginner],
                    #     'but found',
                    #     char,
                    #     'instead.',
                    #     )
                    stack = []
                    break
            elif char in beginers:
                stack.append(char)
        iscore = 0
        while stack:
            s = stack.pop()
            e = b2e[s]
            iscore = (5 * iscore) + values[e]
            print(e, end='')
        if iscore:
            scores.append(iscore)
        print(iscore)
    scores.sort()
    score = scores[len(scores) // 2]
    print(scores)
    print(score)


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
