import pygame
import random

# Constants
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
BIRD_WIDTH = 35
BIRD_HEIGHT = 25
PIPE_WIDTH = 70
PIPE_HEIGHT = 600
GAP = 150
GRAVITY = 0.5
FLAP_STRENGTH = -8
BASE_SPEED = 5
SPEED_INCREMENT = 0.5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Use default font and size 36

# Load images
bird_images = {
    'classic': pygame.image.load('bird.png'),
    'acquatic': pygame.image.load('fish.png'),
    'aero war': pygame.image.load('plane.png')
}

pipe_images = {
    'classic': pygame.image.load('pipe.png'),
    'acquatic': pygame.image.load('tube.png'),
    'aero war': pygame.image.load('tower.png')
}

background_images = {
    'classic': pygame.image.load('background.png'),
    'acquatic': pygame.image.load('spongebobBG.png'),
    'aero war': pygame.image.load('smashedCityBG.png')
}

# Scale images
def scale_images(theme):
    global bird_image, pipe_image, background_image
    if theme == 'classic':
        bird_image = pygame.transform.scale(bird_images[theme], (BIRD_WIDTH, BIRD_HEIGHT))
        pipe_image = pygame.transform.scale(pipe_images[theme], (PIPE_WIDTH, PIPE_HEIGHT))
    elif theme == 'acquatic':
        bird_image = pygame.transform.scale(bird_images[theme], (BIRD_WIDTH, BIRD_HEIGHT * 1.5))
        pipe_image = pygame.transform.scale(pipe_images[theme], (PIPE_WIDTH, PIPE_HEIGHT))
    elif theme == 'aero war':
        bird_image = pygame.transform.scale(bird_images[theme], (BIRD_WIDTH * 1.5, BIRD_HEIGHT))
        pipe_image = pygame.transform.scale(pipe_images[theme], (PIPE_WIDTH * 1.5, PIPE_HEIGHT))
    background_image = pygame.transform.scale(background_images[theme], (SCREEN_WIDTH, SCREEN_HEIGHT))

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, bird_image.get_width(), bird_image.get_height())

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = self.y

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, bird_image.get_width(), bird_image.get_height())

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)
        self.top_rect = pygame.Rect(self.x, self.height - GAP - pipe_image.get_height(), pipe_image.get_width(), pipe_image.get_height())
        self.bottom_rect = pygame.Rect(self.x, self.height, pipe_image.get_width(), pipe_image.get_height())
        self.passed = False

    def update(self, speed):
        self.x -= speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        screen.blit(pipe_image, (self.x, self.height))
        screen.blit(pygame.transform.flip(pipe_image, False, True), (self.x, self.height - GAP - pipe_image.get_height()))

    def get_rects(self):
        return self.top_rect, self.bottom_rect

def check_collision(bird, pipes):
    bird_rect = bird.get_rect()
    for pipe in pipes:
        top_rect, bottom_rect = pipe.get_rects()
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
            return True
    if bird.y <= 0 or bird.y >= SCREEN_HEIGHT:
        return True
    return False

def draw_score(score):
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

def draw_game_over(score):
    game_over_surface = font.render(f'Game Over! Score: {score}', True, (255, 255, 255))
    play_again_surface = font.render('Press any key to play again', True, (255, 255, 255))
    menu_surface = font.render('Press ESC to return to menu', True, (255, 255, 255))
    screen.blit(game_over_surface, (SCREEN_WIDTH//2 - game_over_surface.get_width()//2, SCREEN_HEIGHT//2 - 160))
    screen.blit(play_again_surface, (SCREEN_WIDTH//2 - play_again_surface.get_width()//2, SCREEN_HEIGHT//2 - 110))
    screen.blit(menu_surface, (SCREEN_WIDTH//2 - menu_surface.get_width()//2, SCREEN_HEIGHT//2 - 60))

def draw_menu():
    screen.blit(background_image, (0, 0))
    title_surface = font.render('Flappy Bird', True, (255, 255, 255))
    easy_surface = font.render('Press E for Easy', True, (255, 255, 255))
    medium_surface = font.render('Press M for Medium', True, (255, 255, 255))
    hard_surface = font.render('Press H for Hard', True, (255, 255, 255))
    exit_surface = font.render('Press ESC to Return to Theme Menu', True, (255, 255, 255))
    screen.blit(title_surface, (SCREEN_WIDTH//2 - title_surface.get_width()//2, SCREEN_HEIGHT//4 - 50))
    screen.blit(easy_surface, (SCREEN_WIDTH//2 - easy_surface.get_width()//2, SCREEN_HEIGHT//2 - 150))
    screen.blit(medium_surface, (SCREEN_WIDTH//2 - medium_surface.get_width()//2, SCREEN_HEIGHT//2 - 120))
    screen.blit(hard_surface, (SCREEN_WIDTH//2 - hard_surface.get_width()//2, SCREEN_HEIGHT//2 - 90))
    screen.blit(exit_surface, (SCREEN_WIDTH//2 - exit_surface.get_width()//2, SCREEN_HEIGHT//2 - 60))
    pygame.display.update()

def draw_theme_menu():
    background_classic = pygame.transform.scale(background_images['classic'], (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background_classic, (0, 0))
    title_surface = font.render('Select Theme', True, (255, 255, 255))
    classic_surface = font.render('Press C for Classic', True, (255, 255, 255))
    acquatic_surface = font.render('Press A for Acquatic', True, (255, 255, 255))
    aero_surface = font.render('Press W for Aero War', True, (255, 255, 255))
    exit_surface = font.render('Press ESC to Exit', True, (255, 255, 255))
    screen.blit(title_surface, (SCREEN_WIDTH//2 - title_surface.get_width()//2, SCREEN_HEIGHT//4 - 50))
    screen.blit(classic_surface, (SCREEN_WIDTH//2 - classic_surface.get_width()//2, SCREEN_HEIGHT//2 - 150))
    screen.blit(acquatic_surface, (SCREEN_WIDTH//2 - acquatic_surface.get_width()//2, SCREEN_HEIGHT//2 - 120))
    screen.blit(aero_surface, (SCREEN_WIDTH//2 - aero_surface.get_width()//2, SCREEN_HEIGHT//2 - 90))
    screen.blit(exit_surface, (SCREEN_WIDTH//2 - exit_surface.get_width()//2, SCREEN_HEIGHT//2 - 60))
    pygame.display.update()

def game(difficulty):
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    speed = BASE_SPEED
    pipes_passed = 0
    running = True
    game_over = False

    while running:
        screen.blit(background_image, (0, 0))

        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap()
                    elif event.key == pygame.K_ESCAPE:
                        return 'menu'

            bird.update()
            bird.draw()

            if len(pipes) == 0 or pipes[-1].x < SCREEN_WIDTH - 200:
                pipes.append(Pipe())

            for pipe in pipes:
                pipe.update(speed)
                pipe.draw()
                if pipe.x + pipe_image.get_width() < 0:
                    pipes.remove(pipe)
                if not pipe.passed and pipe.x + pipe_image.get_width() < bird.x:
                    score += 1
                    pipe.passed = True
                    pipes_passed += 1
                    if difficulty == 'medium' and pipes_passed % 5 == 0:
                        speed += SPEED_INCREMENT
                    elif difficulty == 'hard' and pipes_passed % 3 == 0:
                        speed += SPEED_INCREMENT

            if check_collision(bird, pipes):
                game_over = True

            draw_score(score)
        else:
            draw_game_over(score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'menu'
                    else:
                        return difficulty

        pygame.display.update()
        clock.tick(30)

def main():
    theme = 'classic'
    difficulty = 'menu'
    selecting_theme = True

    while selecting_theme:
        draw_theme_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    theme = 'classic'
                    selecting_theme = False
                elif event.key == pygame.K_a:
                    theme = 'acquatic'
                    selecting_theme = False
                elif event.key == pygame.K_w:
                    theme = 'aero war'
                    selecting_theme = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

    scale_images(theme)

    while True:
        if difficulty == 'menu':
            selecting_difficulty = True
            while selecting_difficulty:
                draw_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            difficulty = 'easy'
                            selecting_difficulty = False
                        elif event.key == pygame.K_m:
                            difficulty = 'medium'
                            selecting_difficulty = False
                        elif event.key == pygame.K_h:
                            difficulty = 'hard'
                            selecting_difficulty = False
                        elif event.key == pygame.K_ESCAPE:
                            selecting_difficulty = False
                            selecting_theme = True

        if selecting_theme:
            while selecting_theme:
                draw_theme_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            theme = 'classic'
                            selecting_theme = False
                        elif event.key == pygame.K_a:
                            theme = 'acquatic'
                            selecting_theme = False
                        elif event.key == pygame.K_w:
                            theme = 'aero war'
                            selecting_theme = False
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            return

            scale_images(theme)

        difficulty = game(difficulty)
        if difficulty == 'menu':
            selecting_theme = True

if __name__ == '__main__':
    main()
