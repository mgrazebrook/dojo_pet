import pygame


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

class DojoPet():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Dojo Pet')
        self.screen = pygame.display.set_mode((1200, 960))

        self.clock = pygame.time.Clock()
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
                self.draw()



def main():
    pet = DojoPet()
    pet.run()



if __name__ == "__main__":
    main()
