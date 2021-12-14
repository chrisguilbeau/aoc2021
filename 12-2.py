from sys import argv


class Room:
    def __init__(self, name):
        self.name = name
        self.isSmall = name.islower()
        self.paths = []
        self.visitCount = 0

    def addPath(self, room):
        if room not in self.paths:
            self.paths.append(room)

from collections import Counter


def visit(room, route=[]):
    route = route[:]
    route.append(room.name)
    counts = []
    for n, count in Counter(route).items():
        if n == 'start' and count > 1:
            return
        if n.islower():
            if count > 2:
                return
            counts.append(count)
    if counts.count(2) > 1:
        return
    if room.name == 'end':
        yield (','.join(route))
    else:
        for path in room.paths:
            yield from visit(path, route)


def main(lines):
    rooms = {}
    for line in lines:
        a, b = line.strip().split('-')
        if a not in rooms:
            rooms[a] = Room(a)
        if b not in rooms:
            rooms[b] = Room(b)
        rooms[a].addPath(rooms[b])
        rooms[b].addPath(rooms[a])
    routes = set(visit(rooms['start']))
    list(map(print, sorted(routes)))
    print(len(routes))

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
