import pygame

from pet import Pet


class PetModel():
    """
    """
    def __init__(self):
        self.model = [
            # Array of pairs of points representing our pet
            ((100, 100), (200, 400)),
            ((100, 100), (50, 50)),
            ((100, 100), (50, 150))
        ]

    def draw(self, surface):
        for p1, p2 in self.model:
            pygame.draw.line(surface, "green", p1, p2)


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

        self.clock = pygame.time.Clock()
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
            self.draw()
            if i % 250 == 0:
                self.pet.tick()
            i += 1


def main():
    pet = DojoPet()
    pet.run()



if __name__ == "__main__":
    main()
