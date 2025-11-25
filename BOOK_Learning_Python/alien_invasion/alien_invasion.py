import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        # Создать окно для прорисовки всех графических элементов.
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()  # Группа для хранения всех летящих снарядов
        self.aliens = pygame.sprite.Group()  # Группа для хранения пришельцев

        # Запускает игру в полноэкранном режиме.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()  # Обновление позиции корабля после проверки событий клавиатуры.
            self._update_bullets()  # Обновляет позиции снарядов.
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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # Перемещает корабль вправо пока нажата кнопка.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # Завершает игру при нажатии клавиши Q.
        elif event.key == pygame.K_q:
            sys.exit()
        # Запуск снаряда при нажатии клавиши пробел.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновление позиции снарядов и уничтожает старые снаряды."""
        self.bullets.update()  # Обновляет местоположение снаряда

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Создаёт флот пришельцев."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        alien_width = alien.rect.width  # Определение ширины пришельца по его атрибуту rect.

        # Вычисление доступного пространства для размещения пришельцев.
        aviable_space_x = self.settings.screen_width - (2 * alien_width)

        # Вычисление кол-ва пришельцев, помещающихся в строчку по горизонтали.
        number_aliens_x = aviable_space_x // (2 * alien_width)

        # Создание первого ряда пришельцев.
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width = alien.rect.width

        # Здесь задается координата х для размещения каждого пришельца в ряду.
        alien.x = alien_width + 2 * alien_width * alien_number

        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()  # Отображение последнего прорисованного экрана.


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
