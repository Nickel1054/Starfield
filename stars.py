import random as r
from tkinter import *
import time

W = 1280
H = 800

tk = Tk()
#tk.attributes('-fullscreen', True)
cv = Canvas(tk, width = W, height = H, bg = 'black')
cv.pack()

#img1 = PhotoImage(file = './5139.gif')
image = False

if image == False:
    c = 'black'
else:
    cv.create_image(W/2, H/2, image = img1)
    c = 'white'

class Star:
    def __init__(self, size = 1, color = c, out = c):
        self.size = size
        self.__iter = 0
        self.x = r.randint(W/2-200, W/2+200)
        self.y = r.randint(H/2-200, H/2+200)
        self.id = cv.create_oval(self.x, self.y, self.x+self.size, self.y+self.size, fill = color, outline = out, width = 0.5)
        self.v_x = (self.x-W/2)/30
        self.v_y = (self.y-H/2)/30

    def Move(self):
        cv.move(self.id, self.v_x, self.v_y)
        self.v_x *= 1.1
        self.v_y *= 1.1
                        
        x0, y0, x1, y1 = cv.coords(self.id)
        x1 += 0.06
        y1 += 0.06
        cv.coords(self.id, x0, y0, x1, y1)
        self.size = x1-x0
        if image == False:
            a = int(self.__iter*4)
            if a>256:
                self.color = 'white'
            else:
                self.color = '#{:02x}{:02x}{:02x}'.format(a, a, a)
            cv.itemconfig(self.id, fill = self.color, outline = self.color)
            self.__iter += 1
    
        
    def Delete(self):
        cv.delete(self.id)

    def XY(self, x=1):
        if x==1:
            return cv.coords(self.id)[0]
        else:
            return cv.coords(self.id)[1]


number = 500
ids = []

for i in range(number):
    s = Star()
    ids.append(s)

while(1):
    for i in range(0, number):
        ids[i].Move()
        if ids[i].XY(1)<0 or ids[i].XY(1)>W or ids[i].XY(2)<0 or ids[i].XY(2)>H or ids[i].size>10:
            ids[i].Delete()
            ids[i] = Star()
    #time.sleep(0.005)
    tk.update()
    



    
