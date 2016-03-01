import simplegui


counter = 0
x_counter=200
    
def increment():
    global counter
    counter=counter+1
    
def tick():
    global counter
    global x_counter
    increment()
    if(counter==150):
        counter=30
        x_counter=x_counter+15;
    
    
def draw_handler(canvas):
    canvas.draw_circle((x_counter,counter),10,4,'Blue','Red')
    
    
frame =simplegui.create_frame("Circle Home",500,500)
timer = simplegui.create_timer(50,tick)
frame.set_draw_handler(draw_handler)
timer.start()
frame.start()