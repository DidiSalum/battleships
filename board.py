import pygame
from random import randint


class Board:
    def __init__(self, lines: int, columns: int, surface: pygame.Surface, pos: tuple[int, int]):
        self.surface = surface
        self.rect = surface.get_rect()
        self.rect.topleft = pos
        self.lines = lines
        self.columns = columns
        rd_lines = randint(0, self.lines - 1)
        rd_columns = randint(0, self.columns - 1)
        #self.cel_size = cel_size
        self.matrix = [["" for _ in range(columns)] for _ in range(lines)]
        # a linha acima faz a mesma coisa que o codigo abaixo
        # m = []
        # for _ in range(lines):
        #     l = []
        #     for _ in range(columns):
        #         l.append("")
        #     m.append(l)
        self.matrix[rd_columns][rd_lines] = "x"
    
    def __repr__(self) -> str:
        return "abc"
    
    def __len__(self) -> int:
        return self.lines * self.columns
    
    def shoot(self, x, y) -> None:
        w = self.surface.width
        h = self.surface.height
        if not (self.rect.collidepoint((x, y))):
            return
        line = (y - self.rect.top)//(h // self.lines)
        column = (x - self.rect.left)//(w // self.columns)
        if self.matrix[line][column] == "x":
            print("Acertou!")
        elif self.matrix[line][column] == "a":
            print("Ja acertou essa posição")
        else:
            print("Errou!")
            self.matrix[line][column] = "a"
        


    def draw(self, screen: pygame.Surface):
        self.surface.fill('darkblue')
        cel_x = self.surface.width // self.columns
        cel_y = self.surface.height // self.lines
        for i in range(self.lines):
            for j in range(self.columns):
                if self.matrix[i][j] == "a":
                    pygame.draw.rect(self.surface, "Green", (j*cel_x, i*cel_y, cel_x -1, cel_y - 1))
                elif self.matrix[i][j] == "x":
                    pygame.draw.rect(self.surface, "Lightblue", (j*cel_x, i*cel_y, cel_x -1, cel_y - 1))
                else:
                    pygame.draw.rect(self.surface, "Lightblue", (j*cel_x, i*cel_y, cel_x -1, cel_y - 1))
        screen.blit(self.surface, self.rect)
