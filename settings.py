class Settings():
	""" Класс для хранения всех настроек игры Alien Invasion."""

	def __init__(self):
		""" Инициализирует статические настройки игры. """
		# Параметры экрана
		self.screen_width = 1200
		self.screen_height = 730
		self.bg_color = (230,230,230)

		# Настройка коробля
		self.ship_speed =5
		self.ship_limit = 3

		# Параметры снаряда
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height =15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3

		# Настройка пришельцев.
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10

		# Темп ускорение игры
		self.speedup_scale = 1.1
		# Темп роста стоимости пришельцев
		self.score_scale = 1.5

		self.initialize_dymanic_settings()

		
	def initialize_dymanic_settings(self):
		""" Инициализирует настройки, изменяющиеся в ходе игры."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3.0
		self.alien_speed_factor = 1.0

		# fleet_dirction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1

		# Подсчет очков
		self.alien_points = 50




	def increase_speed(self):
		""" Увеличивает настройки скоростию и стоимость пришельцев."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
