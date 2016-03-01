import simplegui
import math
import random


list1=[]

def style():
    global list1
    j=0
    for i in range(10):
        list1.append([[j,0],[j,200],[j+80,200],[j+80,0]])
        print list1[i]
        j+=80

def init():
    global list1,number,counter,block,block1,num,count
    counter=0
    block=[]
    block1=[-1,-1]
    num=[-1,-1]
    flag=0
    count=0
    j=0
    number=range(0,10)
    random.shuffle(number)
    
def mouse(pos):
    global block1,count,num,flag,counter
    j=pos[0]//80
    if(pos[1]>0 and pos[1]<200 and pos[0]>0 and pos[0]<800 and not j in block and not j in block1):
        state_midd=1
        if(count==0):
            block1[count]=(j)
            index=number.index(j)
            num[count]=index//2
            count=1
            counter+=1
        elif(count==1):
            block1[count]=(j)
            index=number.index(j)
            num[count]=index//2
            mid_final=1
            count=2
            flag=0
            counter+=1
        elif(count==2):
            count=0
            block1=[-1,-1]
            num=[-1,-1]
            block1[count]=(j)
            index=number.index(j)
            num[count]=index//2
            count=1
            flag=0
            counter+=1
    
def draw(canvas):
    global block1,num,flag
    count1=0
    label1.set_text(str(counter))
    for i in range(10):
        if(not (i in block) and not i in block1):
            canvas.draw_polygon(list1[i],1,"black","green")
        elif(i in block1):
            index=number.index(i)
            num1=index//2
            canvas.draw_text(str(num1),[list1[i][0][0]+10,180],100,"white")  
            if(num[count1]==num[count1+1] and flag==0):
                block.extend(block1)
                flag=1
        elif(i in block):
            index=number.index(i)
            num2=index//2
            canvas.draw_text(str(num2),[list1[i][0][0]+10,180],100,"white")


def restart():
    init()


frame=simplegui.create_frame("test",801,201)
style()
init()
frame.set_draw_handler(draw)
label2=frame.add_label("Attempt")
label1=frame.add_label(str(0))
frame.set_mouseclick_handler(mouse)
frame.add_button("restart",restart)
frame.start()