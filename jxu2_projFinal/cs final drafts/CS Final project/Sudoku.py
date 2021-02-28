#game class

from graphics import*
from ButtonClass import*
from GridClass import*

class Sudoku:
    def __init__(self,win,level):
        self.level=level
        self.win=win
        SIZE=9
        win.setCoords(-3,-3,SIZE+2,SIZE+2) #Set the grid
        grid=Grid(win,0,0,9,9,1,1," ")
        checkbutton=Button(win,Point(8,10),2,1,"Check")
        checkbutton.activate()
        quitbutton=Button(win,Point(9,-2),2,1,"Quit")
        prompt4=Text(Point(1,9),"Click empty space to enter your answer")
        prompt5=Text(Point(1,8),"Click check to check your answer")

        prompt4.draw(win)
        prompt5.draw(win)

        qfile=open(level+"question.txt","r")
        qdata=qfile.readlines()
        y=0
        z=0
        while y<9:
            for x in range(8,-1,-1):
               # print(x,y)
                abutton=grid.getbutton(x,y)
                abutton.drawlabel(win,qdata[z])
                z=z+1
            y=y+1


 
        pt=win.getMouse()
        while True:
            while not quitbutton.isClicked(pt):
            
                while not checkbutton.isClicked(pt):
                    x=int(round(pt.getX()))
                    y=int(round(pt.getY()))
                    abutton1=grid.getbutton(y,x)  
                    text=abutton1.returnText()
                    if " \n" in text: #select those with space...
                        abutton1.entryobject(win)
                    
                    

                
                    
                    pt=win.getMouse()
            
                
                pic=Image(Point(5,5),"haha.gif")
                pic.draw(win)
                prompt5=Text(Point(5,7),"Sudoku is never easy!!")
                prompt5.draw(win)
            
                pt=win.getMouse()
            
            for x in range(15):
                prompt3=Text(Point(4,-3+x),"I WILL NOT LET YOU QUIT!")
                prompt3.setFill("red")
                prompt3.draw(win)
            pt=win.getMouse()
            


            
                
