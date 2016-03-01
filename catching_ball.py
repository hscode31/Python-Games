import simplegui


y_counter =20
x_counter=20
flag=-1    
def increment_x():
    global x_counter
    x_counter=x_counter+5
    
def increment_y():
    global y_counter
    y_counter=y_counter+5
    
def tick():
    global y_counter
    global x_counter
    global flag
    if(flag==0):
        increment_x()
    elif(flag==1):
        increment_y()
    
    
def draw_handler(canvas):
    canvas.draw_circle((x_counter,y_counter),15,5,'Blue','Red')
    canvas.draw_polygon([(450,500),(500,500),(500,450),(450,450)],5,'Red')
def right_handler():
    global flag
    flag=0
    
def down_handler():
    global flag
    flag=1
    
    
def stop_handler():
    timer.stop()
    
    
frame =simplegui.create_frame("Circle Home",505,505)
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw_handler)

frame.add_button('right',right_handler)
frame.add_button('down',down_handler)
frame.add_button('stop',stop_handler)
timer.start()
frame.start()