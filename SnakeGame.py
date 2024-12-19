import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (62, 181, 58)  # Set a solid background color
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("snake\\resources\\apple.jpg").convert()
        self.x = random.randint(1, (SCREEN_WIDTH // SIZE) - 1) * SIZE
        self.y = random.randint(1, (SCREEN_HEIGHT // SIZE) - 1) * SIZE

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, (SCREEN_WIDTH // SIZE) - 1) * SIZE
        self.y = random.randint(1, (SCREEN_HEIGHT // SIZE) - 1) * SIZE

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("snake\\resources\\block.jpg").convert()
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        # Constrain snake to the screen dimensions
        self.x[0] = self.x[0] % SCREEN_WIDTH
        self.y[0] = self.y[0] % SCREEN_HEIGHT

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake And Apple Game")

        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def render_background(self):
        # Set a solid background color
        self.surface.fill(BACKGROUND_COLOR)

    def play(self):
        self.render_background()  # Fill the background with color
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))  # White color for score
        self.surface.blit(score, (SCREEN_WIDTH - 200, 10))  # Draw the score at the fixed position

    def show_game_over(self):
        self.render_background()  # Use the background color
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.25)

if __name__ == '__main__':
    game = Game()
    game.run()
