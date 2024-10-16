import pygame
from board import Board
from text_sprite import TextSprite
WIDTH = 1000
HEIGHT = 600

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.Clock()
        self.board_p1 = Board(5, 5, pygame.Surface((WIDTH//5 * 3, HEIGHT//2)),(WIDTH//5 * 2 + 1, 1))
        self.board_p2 = Board(5, 5, pygame.Surface((WIDTH//5 * 3, HEIGHT//2)),(WIDTH//5 * 2 + 1, HEIGHT//2 + 1))
        self.text = TextSprite("Rodrigo", "Arial", 20, "White", (10,10))

    def process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f"atirou na posição {pos}")
                self.board_p1.shoot(*pos)
                self.board_p2.shoot(*pos)
            
    def draw(self):
        self.board_p1.draw(self.screen)
        self.board_p2.draw(self.screen)
        self.text.draw(self.screen)

    def run(self) -> None:
        self.running = True
        while self.running:
            dt = self.clock.tick()
            self.process_events()
            self.draw()
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()