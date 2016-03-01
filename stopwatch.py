# template for "Stopwatch: The Game"
import simplegui
import math
# define global variables
counter=0
attempt=0
pass1=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global counter,milli_count,sec_count,min_count
    milli_count=str(counter%10)
    temp=int(math.floor(counter/10))
    min_count=str(int(math.floor(temp/60)))
    temp=temp%60
    if(temp<10):
        sec_count=str(0)+str(temp)
    else:
        sec_count=str(temp)
    return(min_count+":"+sec_count+"."+milli_count)
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()  
 
def stop():
    global attempt,pass1
    timer.stop()
    if(counter%10==0):
        attempt+=1
        pass1+=1
    else:
        attempt+=1
    
def reset():
    global counter
    counter=0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter+=1

# define draw handler
def draw(canvas):
    canvas.draw_text(str(pass1)+"/"+str(attempt),[250,40],30,"Red")
    canvas.draw_text(format(counter),[80,150],40,"Red")
    
# create frame
frame = simplegui.create_frame("stopwatch",300,300)
frame.set_draw_handler(draw)
frame.add_button("Start",start)
frame.add_button("Stop",stop)
frame.add_button("reset",reset)
timer=simplegui.create_timer(100,tick)
frame.start()

# register event handlers


# start frame


# Please remember to review the grading rubric
