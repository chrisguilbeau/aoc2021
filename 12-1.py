from sys import argv


class Room:
    def __init__(self, name):
        self.name = name
        self.isSmall = name.islower()
        self.paths = []
        self.canVisit = True

    def addPath(self, room):
        if room not in self.paths:
            self.paths.append(room)

    def traverse(self, names=[]):
        print('entering', self.name)
        if self.isSmall:
            self.canVisit = False
        for room in self.paths:
            if room.name == 'end':
                print(','.join(names + [room.name]))
            elif room.canVisit:
                room.traverse(names=names + [room.name])


def visit(room, route=[], visited=[]):
    visited = visited[:]
    route = route[:]
    # print('visiting', room.name)
    route.append(room.name)
    if room.name == 'end':
        yield (','.join(route))
    else:
        if room.isSmall:
            visited = visited + [room.name]
        for path in room.paths:
            if path.name not in visited:
                yield from visit(path, route, visited)


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
    # rooms['start'].traverse()
    routes = list(visit(rooms['start']))
    list(map(print, routes))
    print(len(routes))

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
