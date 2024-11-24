import pgzrun
from pgzhelper import * 
import random
#screen
WIDTH =800
HEIGHT = 600

#runner
runner = Actor('player')
runner.x=100
runner.y = 400
velocity_y = 0
gravity = 2

#obstacles
obstacles = []
obstacles_timeout = 0

#game variables
score = 0
gameOver= False

#restart
# restart_button= Rect(310, 390, 180, 50)
restart_button = Actor('restart')
restart_button.pos = (400, 420)

game_over_image = Actor('gameover')
game_over_image.pos = (400, 250)

def reset_game():
    global score, gameOver, obstacles, runner, velocity_y
    score=0;
    gameOver = False
    obstacles=[]
    runner.x = 100
    runner.y=400
    velocity_y=0

def get_random_spawn_rate():
    return random.randint(40, 80)
def update():
    global obstacles_timeout, velocity_y,score, gameOver, jumping

    #random spawn rate
    spawnRate= get_random_spawn_rate()


    if keyboard.up:
        velocity_y = -8
        jumping = True

    runner.y += velocity_y
    velocity_y+= gravity

    #prevents off screen
    if runner.y>400:
        velocity_y=0
        runner.y=400
    if runner.y <= 0:
        runner.y=0

    #creates obstacles
    obstacles_timeout += 1

    if obstacles_timeout > spawnRate:
        obstacle = Actor('plane')
        obstacle.x = 850
        obstacle.y = random.randint(0, 400)
        obstacles.append(obstacle)
        obstacles_timeout = 0

    for obstacle in obstacles:
        obstacle.x -= score+4
        if obstacle.x < -50:
            obstacles.remove(obstacle)
            score += 1

    
    
    #collision
    if runner.collidelist(obstacles) != -1:
        gameOver=True

def draw():
    background_image = images.load('background.png')
    resize_background = pygame.transform.scale(background_image, (WIDTH, HEIGHT-200))
    screen.blit(resize_background, (0, 0))    
    
    grass_img = images.load('grass.png')
    resized_grass = pygame.transform.scale(grass_img, (WIDTH, HEIGHT-(HEIGHT-200)))
    screen.blit(resized_grass, (0, HEIGHT-200))    

    # screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))
    if gameOver:
        for obstacle in obstacles:
            obstacle.x = 0
        restart_button.draw()
        # screen.draw.filled_rect(restart_button, 'purple')
        game_over_image.draw()  # Draw the Game Over image
        screen.draw.text('Score: '+str(score), centerx=400, centery=500, color=(255, 0, 127), fontsize=60)
    else:
        runner.draw()
        screen.draw.text('Score: '+str(score), (15, 10), color=(255, 0, 127), fontsize=30)
        for obstacle in obstacles:
            obstacle.draw()
def on_mouse_down(pos, button):
    if  restart_button.collidepoint(pos):  # Check if the mouse click is within the button
        reset_game()
        gameOver=False
pgzrun.go()