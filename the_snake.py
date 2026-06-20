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

# Цвет плохой еды
BAD_APPLE_COLOR = (150, 75, 0)

# Цвет камня
ROCK_COLOR = (128, 128, 128)

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

    def __init__(self, body_color=None):
        self.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.body_color = body_color

    def draw(self):
        """Функция, отрисовки обьектов"""


class Apple(GameObject):
    """Класс, с помощью которого создаем яблоко."""

    def __init__(self, occupied=None, body_color=APPLE_COLOR):
        super().__init__(body_color)
        self.randomize_position(occupied)

    def randomize_position(self, occupied=None):
        """Функция, которая получает случайные координаты для яблока."""
        # Число ячеек на поле.
        if occupied is None:
            occupied = []

        max_grid_height = SCREEN_HEIGHT // GRID_SIZE
        max_grid_width = SCREEN_WIDTH // GRID_SIZE

        while True:
            random_y = randint(0, max_grid_height - 1) * GRID_SIZE
            random_x = randint(0, max_grid_width - 1) * GRID_SIZE
            new_position = (random_x, random_y)
            if new_position not in occupied:
                self.position = new_position
                break

    # Метод draw класса Apple
    def draw(self):
        """Функция, отрисовки обьектов"""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class BadApple(GameObject):
    """Класс, с помощью которого создаем плохое яблоко."""

    def __init__(self, occupied=None, body_color=BAD_APPLE_COLOR):
        super().__init__(body_color)
        self.randomize_position(occupied)

    def randomize_position(self, occupied=None):
        """Функция, которая получает случайные координаты для яблока."""
        # Число ячеек на поле.
        if occupied is None:
            occupied = []

        max_grid_height = SCREEN_HEIGHT // GRID_SIZE
        max_grid_width = SCREEN_WIDTH // GRID_SIZE

        while True:
            random_y = randint(0, max_grid_height - 1) * GRID_SIZE
            random_x = randint(0, max_grid_width - 1) * GRID_SIZE
            new_position = (random_x, random_y)
            if new_position not in occupied:
                self.position = new_position
                break

    # Метод draw класса Apple
    def draw(self):
        """Функция, отрисовки обьектов"""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Rock(GameObject):
    """Класс, с помощью которого создаем камень."""

    def __init__(self, occupied=None, body_color=ROCK_COLOR):
        super().__init__(body_color)
        self.randomize_position(occupied)

    def randomize_position(self, occupied=None):
        """Функция, которая получает случайные координаты для яблока."""
        # Число ячеек на поле.
        if occupied is None:
            occupied = []

        max_grid_height = SCREEN_HEIGHT // GRID_SIZE
        max_grid_width = SCREEN_WIDTH // GRID_SIZE

        while True:
            random_y = randint(0, max_grid_height - 1) * GRID_SIZE
            random_x = randint(0, max_grid_width - 1) * GRID_SIZE
            new_position = (random_x, random_y)
            if new_position not in occupied:
                self.position = new_position
                break

    # Метод draw класса Apple
    def draw(self):
        """Функция, отрисовки обьектов"""
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

    def update_direction(self):
        """Метод обновления направления после нажатия на кнопку"""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    # # Метод draw класса Snake
    def draw(self):
        """Функция, отрисовки обьектов"""
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    #     # Отрисовка головы змейки
        head_rect = pygame.Rect(
            self.get_head_position(), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

    #     # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def move(self):
        """Функция, с помощью которой двигается змейка.
        (создается голова и удаляется хвост).
        """
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


def handle_keys(game_object):
    """Функция обработки действий пользователя"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основная функция, с помощью которой игра работает"""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake()
    apple = Apple(occupied=snake.positions)
    bad_apple = BadApple(occupied=snake.positions + [apple.position])
    rock = Rock(occupied=snake.positions
                + [apple.position, bad_apple.position]
                )

    while True:
        clock.tick(SPEED)

        # Тут опишите основную логику игры.
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        occupied = (snake.positions + [bad_apple.position, rock.position])

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(occupied)

        elif snake.get_head_position() == bad_apple.position:
            if snake.length > 1:
                snake.length -= 1
                last_segment = snake.positions.pop()
                last_rect = pygame.Rect(last_segment, (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)
                bad_apple.randomize_position(
                    snake.positions + [apple.position, rock.position]
                )

        elif snake.get_head_position() == rock.position:
            snake.reset()
            rock.randomize_position(
                snake.positions + [apple.position, bad_apple.position]
            )
            rock.draw()
            screen.fill(BOARD_BACKGROUND_COLOR)

        elif snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            screen.fill(BOARD_BACKGROUND_COLOR)

        apple.draw()
        snake.draw()
        bad_apple.draw()
        rock.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
