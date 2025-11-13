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
        # Каждый новый корабль появляется в центре экрана.
        self.rect.center = self.screen_rect.center
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)  # Чтобы значение могло быть не только целым числом.
        self.y = float(self.rect.y)

        # Флаги перемещения.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Ограничение, чтобы корабль не выходил за правый край экрана.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Обновляет атрибут x, не rect.
            self.x += self.settings.rocket_speed
        # Ограничение, чтобы корабль не выходил за левый край экрана.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        # Ограничение, чтобы корабль не выходил за верхнюю границу экрана.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        # Ограничение, чтобы корабль не выходил за нижнюю границу экрана.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
