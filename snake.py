import pygame

class Player:
	x = []
	y = []
	speed = 24
	direction = 0
	length = 3
	counter = 0
	countMax = 2

	def __init__(self, length):
		self.length = length
		for i in range(length):
			self.x.append(0)
			self.y.append(0)

	def update(self):
		self.counter += 1
		if self.counter > self.countMax:

			# update previous positions starting at end working fwd
			for i in range(self.length-1, 0, -1):
				self.x[i] = self.x[i-1]
				self.y[i] = self.y[i-1]

			# update head of snek
			if self.direction == 0:
				self.x[0] += self.speed
			if self.direction == 1:
				self.x[0] -= self.speed
			if self.direction == 2:
				self.y[0] -= self.speed
			if self.direction == 3:
				self.y[0] += self.speed

			self.counter = 0

	def moveRight(self):
		self.direction = 0

	def moveLeft(self):
		self.direction = 1

	def moveUp(self):
		self.direction = 2

	def moveDown(self):
		self.direction = 3

	def draw(self, surface, image):
		for i in range(self.length):
			surface.blit(image, (self.x[i], self.y[i]))

class App:
	windowHeight = 400
	windowWidth = 600
	player = None
	clock = pygame.time.Clock()

	def __init__(self):
		self._running = True
		self._screen = None
		self._image = None
		self.player = Player(5)

	def on_init(self):
		pygame.init()
		self._screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
		self._screen.fill((255, 255, 255))
		pygame.display.set_caption("SNEK GAME")
		self._running = True
		self._image = pygame.image.load('snake.png').convert()

	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False

	def on_loop(self):
		self.player.update()

	def on_render(self):
		self._screen.fill((255, 255, 255))
		self.player.draw(self._screen, self._image)
		pygame.display.flip()

	def on_execute(self):
		if self.on_init() == False:
			self._running = False

		while self._running:
			pygame.event.pump()

			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_UP]:
				self.player.moveUp()
			if pressed[pygame.K_DOWN]:
				self.player.moveDown()
			if pressed[pygame.K_LEFT]:
				self.player.moveLeft() 
			if pressed[pygame.K_RIGHT]:
				self.player.moveRight()
			if pressed[pygame.K_ESCAPE]:
				self._running = False

			self.on_render()
			self.on_loop()
			self.clock.tick(30)
		pygame.quit()

if __name__ == "__main__":
	snekGame = App()
	snekGame.on_execute()




