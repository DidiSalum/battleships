import pygame

class TextSprite:
    def __init__(self, text: str,font_name: str, size: int, color: str, pos: tuple[int, int]) -> None:
        self.font = pygame.font.SysFont(font_name, size)
        self.img = self.font.render(text, True, color)
        self.rect = self.img.get_rect()
        self.rect.topleft = pos

    def draw(self, surface: pygame.Surface):
        surface.blit(self.img, self.rect)
