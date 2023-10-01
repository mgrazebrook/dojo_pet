import pygame
from pet import Pet
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


class TextModel:

    def __init__(self):
        pass

    def draw(self, surface, pet):
        font = pygame.font.Font(None, 64)
        text = font.render(f"Food: {pet.food}", True, (255, 0, 255))
        textpos = text.get_rect(centerx=surface.get_width() - 100, y=50)
        surface.blit(text, textpos)
        text = font.render(f"Waste: {pet.waste}", True, (255, 0, 255))
        textpos = text.get_rect(centerx=surface.get_width() - 100, y=95)
        surface.blit(text, textpos)

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
        self.info = TextModel()
        self.pet = Pet()


    def draw(self):
        #self.screen.blit(self.screen, (0,0))
        self.screen.fill((0,0,0))
        self.model.draw(self.screen)
        self.info.draw(self.screen, self.pet)
        pygame.display.update()

    def run(self):
        running = True
        i = 0
        while running:
            self.clock.tick(600)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if (event.type == pygame.KEYDOWN) and (event.key == ord("f")):
                    self.pet.feed()
                if (event.type == pygame.KEYDOWN) and (event.key == ord("s")):
                    self.pet.shovel()
                if (event.type == pygame.KEYDOWN) and (event.key == ord("t")):
                    self.pet.tick()
            time = self.clock.get_time() - self.start
            self.model.update(time)
            self.draw()
            self.clock.tick(self.fps)
            if i % 250 == 0:
                self.pet.tick()
            i += 1


def main():
    pet = DojoPet()
    pet.run()



if __name__ == "__main__":
    main()
