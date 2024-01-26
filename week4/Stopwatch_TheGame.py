import simplegui

# Global variables
time_interval = 100  # Timer interval in milliseconds (0.1 seconds)
time_count = 0       # Global integer to track time in tenths of seconds
running = False      # Boolean variable to track if the stopwatch is running
stop_count = 0       # Counter for total stops
success_count = 0    # Counter for successful stops

# Helper function to format time
def format(t):
    minutes = t // 600
    seconds = (t % 600) // 10
    tenths = t % 10
    return str(minutes) + ":" + str(seconds//10) + str(seconds%10) + "." + str(tenths)

# Event handler for timer
def timer_handler():
    global time_count
    time_count += 1

# Event handler for drawing on the canvas
def draw_handler(canvas):
    canvas.draw_text(format(time_count), (100, 150), 50, "White")
    canvas.draw_text(str(success_count)+"/"+str(stop_count),(225,50),50,"Red")


# Event handler for start button
def start_handler():
    global running
    timer.start()
    running = True

# Event handler for stop button
def stop_handler():
    global running, stop_count, success_count
    if running:
        timer.stop()
        running = False
        stop_count += 1
        if time_count % 10 == 0:
            success_count += 1

# Event handler for reset button
def reset_handler():
    global time_count, running, stop_count, success_count
    timer.stop()
    time_count = 0
    running = False
    stop_count = 0
    success_count = 0

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)

# Create a timer with the given interval
timer = simplegui.create_timer(time_interval, timer_handler)

# Start the frame
frame.start()
