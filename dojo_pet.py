import pygame
import math

class PetModel():
    """
    """
    def __init__(self):
        self.model = [
            # Array of pairs of points representing our pet
            ((200, 700), (500, 700)),
            ((500, 700), (600, 500)),
            ((600, 500), (700, 640)),
            ((600, 500), (650, 680)),
        ]

    def update(self, seconds):
        # Mouth length: 120
        # Initial angle: 30 & 45 degrees down
        # Top jaw stationary
        # "head" is the point where the jaw lines meet
        # 2 seconds?
        seconds %= 2000
        if seconds < 1000:
            t = seconds
        else:
            t = seconds - 1000
        dx = 120 * math.sin(seconds * 2 * math.pi / 1000)
        dy = 120 * math.cos(seconds * 2 * math.pi / 1000)
        self.model[-1] = ((600, 500), (600 + dx, 500 + dy))

    def draw(self, surface):
        for p1, p2 in self.model:
            pygame.draw.line(surface, "green", p1, p2, width=4)

class DojoPet():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Dojo Pet')
        self.screen = pygame.display.set_mode((1200, 960))

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.start = self.clock.get_time()

        self.reset()


    def reset(self):
        self.model = PetModel()


    def draw(self):
        self.model.draw(self.screen)
        pygame.display.update()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                time = self.clock.get_time() - self.start
                self.model.update(time)
                self.draw()
                self.clock.tick(self.fps)



def main():
    pet = DojoPet()
    pet.run()



if __name__ == "__main__":
    main()
