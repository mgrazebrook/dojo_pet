class Pet:
    def __init__(self, scale=1):
        self.scale = scale
        self.food = 5
        self.waste = 0

    def tick(self):
        if self.dead:
            return
        self.food -= self.scale
        self.waste += self.scale

    @property
    def dead(self):
        if self.food <= 0:
            return True
        if self.waste >= 10:
            return True
        return False

    @property
    def happiness(self):
        return (self.food * (10 - self.waste)) / 100

    def feed(self):
        if self.dead:
            return
        self.food += self.scale

    def shovel(self):
        self.waste = 0
