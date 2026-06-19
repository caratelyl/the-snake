from random import choice, randint

import pygame

# Test push.
# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """Класс, с помощью которого создаем все обьекты."""

    def __init__(self, body_color):
        self.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.body_color = body_color

    def draw(self):
        pass


class Apple(GameObject):
    """Класс, с помощью которого создаем яблоко."""

    def __init__(self, body_color=APPLE_COLOR):
        super().__init__(body_color)
        self.randomize_position()

    def randomize_position(self):
        """Функция, которая получает случайные координаты для яблока."""

        # Число ячеек на поле.
        max_grid_height = SCREEN_HEIGHT // GRID_SIZE
        max_grid_width = SCREEN_WIDTH // GRID_SIZE

        random_y = randint(0, max_grid_height - 1) * GRID_SIZE
        random_x = randint(0, max_grid_width - 1) * GRID_SIZE
        self.position = (random_x, random_y)

    # Метод draw класса Apple
    def draw(self):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, с помощью которошо создаем змейку."""

    def __init__(self, body_color=SNAKE_COLOR):
        super().__init__(body_color)
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        """Начальная позиция змейки."""
        return self.positions[0]

    # Метод обновления направления после нажатия на кнопку
    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    # # Метод draw класса Snake
    def draw(self):
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    #     # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

    #     # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def move(self):
        """Функция, с помощью которой двигается змейка.
        (создается голова и удаляется хвост)."""

        head_x, head_y = self.get_head_position()
        dx, dy = self.direction

        new_x = (head_x + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT
        new_head = (new_x, new_y)

        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def reset(self):
        """Функция, начинающая игру сначала при проигрыше"""
        self.length = 1
        self.positions = [self.position]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None
        self.last = None


# Функция обработки действий пользователя
def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(SPEED)

        # Тут опишите основную логику игры.
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            screen.fill(BOARD_BACKGROUND_COLOR)

        apple.draw()
        snake.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
