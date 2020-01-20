import tkinter
import random

SIZE=10
HEIGHTOFTEXT=15
DIMRATE=0.95
textstoshow=list(range(12352, 12543))+(list(range(48, 57))*10)
#maybe random?

class rainstream:
    def __init__(self, startx):
        self.startx=startx
        #self.endy=random.randint(1000,2000)
        self.endy=1500
        #when the rain ends
        self.particles=[]
        self.text=[]
        self.fills=[]
        #the text that appears in this rain
        self.lasty=0
    def rain(self):
        self.lasty=self.lasty+HEIGHTOFTEXT
        #self.text.append(chr(random.randint(12352, 12543)))
        self.text.append(chr(random.choice(textstoshow)))
        self.fills.append([int('39', 16), int('FF', 16), int('14', 16)])
        self.particles.append(canvas.create_text(self.startx, self.lasty, text=self.text[len(self.text)-1], fill='#39FF14'))
        for index, text in enumerate(self.particles):
            fill='#'
            for rgbindex, color in enumerate(self.fills[index]):
                #because in each of self.fills there is a list of rgb values
                color*=DIMRATE
                self.fills[index][rgbindex]=color
                fill+=hex(int(color)).upper()[2:].rjust(2, '0')
                #take the hex of int of the color and upper it to look nice, then take off the first 2 letters: 0x int of the color float
                #then add 0s to its left
            #self.fills[index]*=DIMRATE
            canvas.itemconfigure(text, fill=fill)
        if self.lasty<self.endy:
            return False
    def erase(self):
        for particle in self.particles:
            canvas.delete(particle)

        #return true if end

rains=[]
#[[(text, color), (text, color)], [(text, color), (text, color)]]
#canvas.itemconfigure(particleid, text='text', fill='#FFFFFF')
root=tkinter.Tk()
root.geometry("1000x1000")
canvas=tkinter.Canvas(root, width=1000, height=1000, bg='#000000')
canvas.pack()

rains=[]

def repeat():
    #rains is list of rain streams, which each has rain particles
    if random.randint(1, 3)==1:
        rains.append(rainstream(random.randint(1, 1000)))
    for index, rain in enumerate(rains):
        dead=rain.rain()
        if dead:
            rain.erase()
            del rains[index]
    root.after(50, repeat)
    #50 to make less resource intensitive

root.after(1, repeat)
root.mainloop()
