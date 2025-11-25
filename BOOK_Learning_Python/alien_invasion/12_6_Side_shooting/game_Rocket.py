import sys
import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet


class GameRocket:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        pygame.init()
        # Создать окно для прорисовки всех графических элементов.
        self.settings = Settings()

        # Запускает игру в режиме окна.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Side shooting")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.rocket.update()  # Обновление позиции корабля после проверки событий клавиатуры.
            self._update_bullets()
            self._update_screen()  # Обновление экрана.

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():  # Возвращ. список событий с момента последнего вызова функции.
            if event.type == pygame.QUIT:
                sys.exit()  # Метод для выхода из игры.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        # Завершает игру при нажатии клавиши Q.
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:  # Метод для выпуска снарядов.
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()  # Обновление позиции снаряда.

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1500:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()  # Отображение последнего прорисованного экрана.


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = GameRocket()
    ai.run_game()
