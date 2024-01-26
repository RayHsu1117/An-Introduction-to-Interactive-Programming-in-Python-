# implementation of card game - Memory

import simplegui
import random

number = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
show = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
click = -1
# helper function to initialize globals
def new_game():
    global number
    random.shuffle(number)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global click
    for i in range(0,800,50):
        if i < pos[0] < i+50:
            click = i//50
            return
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global click,number,show
    for i in range(0,800,50):
        if show[click]:
            canvas.draw_polygon([[click*50, 0], [click*50+50, 0], [click*50+50, 100], [click*50, 100]], 10, 'Green', 'Green')
            canvas.draw_text(str(number[click]), [17.5+click*50,60], 30, 'white')
        else:
            canvas.draw_polygon([[i, 0], [i+50, 0], [i+50, 100], [i, 100]], 12, 'Black', 'Black')
    if click != -1:
        if ~show[click] :
            show[click] = True
            canvas.draw_polygon([[click*50, 0], [click*50+50, 0], [click*50+50, 100], [click*50, 100]], 10, 'Green', 'Green')
            canvas.draw_text(str(number[click]), [17.5+click*50,60], 30, 'white')
        else:

    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric