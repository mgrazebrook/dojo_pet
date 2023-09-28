import pygame

def main():
    pygame.init()
    pygame.display.set_caption('Dojo Pet')

    screen = pygame.display.set_mode((1200, 960))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
