class Settings():
    """Класс для хранения всех настроек игры Rocket."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1500
        self.screen_height = 770
        self.bg_color = (230, 230, 230)

        # Настройки скорости.
        self.rocket_speed = 0.8

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (90, 90, 90)
        self.bullet_allowed = 5