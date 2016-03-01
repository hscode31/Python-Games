import simplegui
import random
import math

width=600
height=400
p_height=80
p_width=10
p1_top=0
p2_top=0
height_mid=p_height/2
p1=[[0,0],[0,0],[0,0],[0,0]]
p2=[[0,0],[0,0],[0,0],[0,0]]
v1_paddle=0
v2_paddle=0
ball_pos=[0,0]
v_ball=[0,0]
player1=0
player2=0
def init():
    global p1_top,p2_top,player1,player2
    p1_top=random.randrange(p_height/2,height-p_height/2)
    p2_top=random.randrange(p_height/2,height-p_height/2)
    v_ball[0]=random.randrange(-3,3)
    if(v_ball[0]==0):
        v_ball[0]=1;
    v_ball[1]=random.randrange(-3,3)
    ball_pos[0]=width/2
    ball_pos[1]=height/2
    print p1_top,p2_top
    print p1
    
def key_down_handler(key):
    global p1_top,p2_top,v1_paddle,v2_paddle
    if(key==simplegui.KEY_MAP["down"]):
        v1_paddle=2
    elif(key==simplegui.KEY_MAP["up"]):
        v1_paddle=-2
    elif(key==simplegui.KEY_MAP['s']):
        v2_paddle=2
    elif(key==simplegui.KEY_MAP['w']):
        v2_paddle=-2
        
def key_up_handler(key):
    global v1_paddle,v2_paddle
    v1_paddle=0
    v2_paddle=0
    
def draw(canvas):
    set_paddle_position1()
    set_paddle_position2()
    set_ball_position()
    canvas.draw_line([p_width,0],[p_width,height],2,"White")
    canvas.draw_line([width-p_width,0],[width-p_width,height],2,"White")
    canvas.draw_line([width/2,0],[width/2,height],2,"White")
    canvas.draw_polygon(p1,2,"Red","Green")
    canvas.draw_polygon(p2,2,"Red","Green")
    canvas.draw_circle([ball_pos[0],ball_pos[1]],15,1,"Red","White")
    canvas.draw_text(str(player1),[200,100],20,"Red")
    canvas.draw_text(str(player2),[400,100],20,"Red")

def set_ball_position():
    global player1,player2,v1_paddle,v2_paddle
    ball_pos[0]+=v_ball[0]
    ball_pos[1]+=v_ball[1]
    if(ball_pos[1]<0+15):
        v_ball[1]=-v_ball[1]
        ball_pos[1]+=v_ball[1]
    elif(ball_pos[1]>height-1-15):
        v_ball[1]=-v_ball[1]
        ball_pos[1]+=v_ball[1]
    elif(ball_pos[0]<(p_width+15)and ball_pos[1]<(p1_top+height_mid)and ball_pos[1]>(p1_top-height_mid)):
        v_ball[0]=-v_ball[0]+1
        v_ball[1]+=v1_paddle
        ball_pos[0]+=v_ball[0]
    elif(ball_pos[0]<(p_width) and (ball_pos[1]>(p1_top+height_mid) or ball_pos[1]<(p1_top-height_mid))):
        player1+=1
        init()
    elif(ball_pos[0]>(width-p_width-15)and ball_pos[1]<(p2_top+height_mid)and ball_pos[1]>(p2_top-height_mid)):   
        v_ball[0]=-v_ball[0]-1
        v_ball[1]+=v2_paddle
        ball_pos[0]+=v_ball[0]
    elif(ball_pos[0]>(width-p_width)and (ball_pos[1]>(p2_top+height_mid) or ball_pos[1]<(p2_top-height_mid))):
        player2+=1
        init()
        
def set_paddle_position1():
    global p1,p1_top,p2_top
    p1_top=p1_top+v1_paddle
    if(p1_top+height_mid>height-1 or p1_top-height_mid<0):
        p1_top=p1_top-v1_paddle
    p1[0]=[0,p1_top-height_mid]
    p1[1]=[p_width,p1_top-height_mid]
    p1[2]=[p_width,p1_top+height_mid]
    p1[3]=[0,p1_top+height_mid]
    
    
def set_paddle_position2():
    global p2,p1_top,p2_top
    p2_top=p2_top+v2_paddle
    if(p2_top+height_mid>height-1 or p2_top-height_mid<0):
        p2_top=p2_top-v2_paddle
    p2[0]=[width-1,p2_top-height_mid]
    p2[1]=[width-1-p_width,p2_top-height_mid]
    p2[2]=[width-1-p_width,p2_top+height_mid]
    p2[3]=[width-1,p2_top+height_mid]
    
def restart():
    player1=0
    player2=0
    init()
    
    
    
    
frame=simplegui.create_frame("pong",width,height)
init()
frame.set_draw_handler(draw)
frame.start()
frame.set_keydown_handler(key_down_handler)
frame.set_keyup_handler(key_up_handler)
frame.add_button("Restart",restart)