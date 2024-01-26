# Implementation of classic arcade game Pong
import math
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400  
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2     
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2,HEIGHT / 2]
INIT_BALL_POS = [WIDTH / 2,HEIGHT / 2]
paddle1_pos = [[0,HALF_HEIGHT-HALF_PAD_HEIGHT],[PAD_WIDTH,HALF_HEIGHT-HALF_PAD_HEIGHT],
               [PAD_WIDTH,HALF_HEIGHT+HALF_PAD_HEIGHT],[0,HALF_HEIGHT+HALF_PAD_HEIGHT]]
paddle1_up = False
paddle1_down = False
paddle2_pos = [[WIDTH-PAD_WIDTH,HALF_HEIGHT-HALF_PAD_HEIGHT],[WIDTH,HALF_HEIGHT-HALF_PAD_HEIGHT],
               [WIDTH,HALF_HEIGHT+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH,HALF_HEIGHT+HALF_PAD_HEIGHT]]
paddle2_up = False
paddle2_down = False
paddle_vel = 10
time = 0
angle = random.random()*360
P1_score = 0
P2_score = 0
ball_dir = [math.cos(angle),math.sin(angle)]
ball_vel = 5
def tick():
    global time
    time = time + 1

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos  # these are numbers  # these are ints
    global P1_score, P2_score, paddle1_pos, paddle2_pos, ball_pos, ball_vel,ball_dir,INIT_BALL_POS
    global paddle1_down,paddle1_up,paddle2_down,paddle2_up,paddle_vel
    ball_pos = [WIDTH / 2,HEIGHT / 2]
    INIT_BALL_POS = [WIDTH / 2,HEIGHT / 2]
    paddle1_pos = [[0,HALF_HEIGHT-HALF_PAD_HEIGHT],[PAD_WIDTH,HALF_HEIGHT-HALF_PAD_HEIGHT],
               [PAD_WIDTH,HALF_HEIGHT+HALF_PAD_HEIGHT],[0,HALF_HEIGHT+HALF_PAD_HEIGHT]]
    paddle1_up = False
    paddle1_down = False
    paddle2_pos = [[WIDTH-PAD_WIDTH,HALF_HEIGHT-HALF_PAD_HEIGHT],[WIDTH,HALF_HEIGHT-HALF_PAD_HEIGHT],
               [WIDTH,HALF_HEIGHT+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH,HALF_HEIGHT+HALF_PAD_HEIGHT]]
    paddle2_up = False
    paddle2_down = False
    paddle_vel = 10
    P1_score = 0
    P2_score = 0

def draw(canvas):
    global P1_score, P2_score, paddle1_pos, paddle2_pos, ball_pos, ball_vel,ball_dir,INIT_BALL_POS
    global paddle1_down,paddle1_up,paddle2_down,paddle2_up,paddle_vel
    global time,angle
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # update ball   
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,5,"white","white")
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_dir[1] = -ball_dir[1]

    ball_pos[0] += ball_dir[0] * ball_vel
    ball_pos[1] += ball_dir[1] * ball_vel

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_up:
        for i in range(4):
            paddle1_pos[i][1] -= paddle_vel
    elif paddle1_down:
        for i in range(4):
            paddle1_pos[i][1] += paddle_vel
    if paddle2_up:
        for i in range(4):
            paddle2_pos[i][1] -= paddle_vel
    elif paddle2_down:
        for i in range(4):
            paddle2_pos[i][1] += paddle_vel
    if paddle1_pos[0][1] <= 0 or paddle1_pos[3][1] >= HEIGHT:
        paddle1_up = False
        paddle1_down = False
    if paddle2_pos[0][1] <= 0 or paddle2_pos[3][1] >= HEIGHT:
        paddle2_up = False
        paddle2_down = False
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 12, 'white', 'white')
    canvas.draw_polygon(paddle2_pos, 12, 'green', 'green')
    
    # determine whether paddle and ball collide    
    if (ball_pos[0] + BALL_RADIUS >= paddle2_pos[0][0]) \
        or  (ball_pos[0] - BALL_RADIUS <= paddle1_pos[1][0] ):
        #if paddle2_pos[1][1]<=ball_pos[1]<=paddle2_pos[2][1]:
            ball_dir[0] = -ball_dir[0]
        #重新思考碰撞條件    
    elif ball_pos[0] <= BALL_RADIUS:
        P2_score += 1
        ball_pos = INIT_BALL_POS
        #angle = random.random()*360
        #ball_dir = [math.cos(angle),math.sin(angle)]
    elif ball_pos[0] + BALL_RADIUS >= WIDTH:
        P1_score += 1
        ball_pos = INIT_BALL_POS

        #angle = random.random()*360
        #ball_dir = [math.cos(angle),math.sin(angle)]


    # if ball_pos[0] == BALL_RADIUS or ball_pos[0] == WIDTH - BALL_RADIUS:
    #     ball_pos = INIT_BALL_POS
    # draw scores
    canvas.draw_text(str(P1_score),[WIDTH/4,HEIGHT/8], 20, "white")
    canvas.draw_text(str(P2_score),[3*WIDTH/4,HEIGHT/8], 20, "white")
                
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_down, paddle2_down,paddle1_up,paddle2_up
    if key == simplegui.KEY_MAP['down'] and (paddle2_pos[3][1] and paddle2_pos[2][1]) < HEIGHT:
        paddle2_down = True        
        # for i in range(4):
        #     paddle2_pos[i][1] += paddle_vel
    elif key == simplegui.KEY_MAP['up'] and (paddle2_pos[0][1] and paddle2_pos[1][1]) > 0:
        paddle2_up = True
        # for i in range(4):
        #     paddle2_pos[i][1] -= paddle_vel 
    if key == simplegui.KEY_MAP['s'] and (paddle1_pos[3][1] and paddle1_pos[2][1]) < HEIGHT:
        paddle1_down = True
        # for i in range(4):
        #     paddle1_pos[i][1] += paddle_vel
    elif key == simplegui.KEY_MAP['w'] and (paddle2_pos[0][1] and paddle2_pos[1][1]) > 0:
        paddle1_up = True
        # for i in range(4):
        #     paddle1_pos[i][1] -= paddle_vel          
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_up, paddle2_up,paddle1_down ,paddle2_down,paddle1_up,paddle2_up
    if key == simplegui.KEY_MAP['down']:
        paddle2_up = False
        paddle2_down = False
    elif key == simplegui.KEY_MAP['up']:
        paddle2_up = False
        paddle2_down = False
    if key == simplegui.KEY_MAP['s']:
        paddle1_up = False
        paddle1_down = False
    elif key == simplegui.KEY_MAP['w']:
        paddle1_up = False
        paddle1_down = False  


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(100, tick)

# start frame
new_game()
frame.start()
timer.start()