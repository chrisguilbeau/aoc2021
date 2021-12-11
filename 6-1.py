from sys import argv

class LanternFish:
    def __init__(self, timer=8):
        self.timer = timer
    def getSpawn(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return LanternFish()

def main(lines):
    allFish = []
    for timer in lines[0].split(','):
        allFish.append(LanternFish(int(timer)))
    for i in range(80):
        newFish = []
        for f in allFish:
            newFish.append(f.getSpawn())
        allFish.extend(filter(None, newFish))
    print(len(allFish))

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    main(lines)
