import pygame


class Rocket():
    """Класс для управления ракетой."""
    def __init__(self, ai_game):
        # Инициализирует корабль и задает его начальную позицию.
        self.screen = ai_game.screen
        self.settings = ai_game.settings  # Задает начальные параметры корабля.
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('ship2.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется по центру левого края экрана.
        self.rect.midleft = self.screen_rect.midleft
        # Сохранение вещественной координаты центра корабля.
        self.y = float(self.rect.y)  # Чтобы значение могло быть не только целым числом.

        # Флаги перемещения.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Ограничение, чтобы корабль не выходил за верхнюю границу экрана.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        # Ограничение, чтобы корабль не выходил за нижнюю границу экрана.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.y = self.y  # Обновление атрибута rect на основании self.y.

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
