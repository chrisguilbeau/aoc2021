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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    }


def main(lines):
    score = 0
    for line_ in lines:
        line = line_.strip()
        stack = []
        for char in line:
            if char in enders:
                beginner = stack.pop(-1)
                try:
                    assert beginner == e2b[char], f'{beginner} nok {char}'
                except Exception:
                    print(
                        line,
                        '- Expected',
                        b2e[beginner],
                        'but found',
                        char,
                        'instead.',
                        )
                    score += values[char]
                    break
            elif char in beginers:
                stack.append(char)
    print(score)


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
