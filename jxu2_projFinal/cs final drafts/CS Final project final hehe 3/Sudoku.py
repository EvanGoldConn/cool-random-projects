#game class

from graphics import*
from ButtonClass import*
from GridClass import*

class Sudoku:

    def __init__(self,level):
        self.level=level
        
        SIZE=9
        win=GraphWin(level+"Sudoku",600,600)
        win.setCoords(-3,-3,SIZE+2,SIZE+2)
        grid=Grid(win,0,0,9,9,1,1," ")
        checkbutton=Button(win,Point(4,10),2,1,"Check")
        prompt1=Text(Point(4,9),"Click check to check your answers. A right answer will appear as green, a wrong answer will appear as red.")
        prompt1.draw(win)
        qfile=open(level+".txt","r")
        qdata=qfile.readlines()
        #-----answerMatrix------
        infile=open(level+".txt","r")
        qdata=infile.readlines()

        cleandata=[]
        for item in qdata:
            newitem=item.strip()
            cleandata.append(newitem)
   
        row=9
        col=9
        self.cleandatalist=[]
        y=0
        z=9
        for data1 in range(0,9):
            datalist=[]
            for data2 in cleandata[y:z]:
                datalist.append(data2)
            y=y+9
            z=z+9
            self.cleandatalist.append(datalist)
        #--------answerMatrix------
        questionlist=[]
        answerlist=[]
        for item in qdata:
            if "*" in item:
                item=" "
            questionlist.append(item)

        for item2 in qdata:
            if "*" in item2:
                item2=item2
            else:
                item2=" "
            answerlist.append(item2)
            
        y=0
        z=0
        while y<9:
            for x in range(8,-1,-1):
               # print(x,y)
                abutton=grid.getbutton(x,y)
                abutton.drawlabel(win,questionlist[z])
                z=z+1
            y=y+1

        pt=win.getMouse()

        colorlist=[]
        while True:
            if not checkbutton.isClicked(pt):
                x=int(round(pt.getX()))
                y=int(round(pt.getY()))
                abutton1=grid.getbutton(y,x)
                if abutton1.returnText() == " ":
                    abutton1.entryobject(win)
                pt=win.getMouse()


            else:
                for c in range(len(grid.buttonMatrix)):
                    for r in range(len(grid.buttonMatrix)):
                        eachbutton=grid.getbutton(c,r)

                        if eachbutton.getentryText() != "":
                            userinput=eachbutton.getentryText()
                            userinput=userinput+"*"
                            correctanswer=self.cleandatalist[r][8-c]
                            if userinput != correctanswer:
                                eachbutton.setColor("red")
                                
                            else:
                                eachbutton.drawlabel(win,userinput)
                                eachbutton.setColor("Green")
                                
                colorlist.append(grid.getAllcolor())
                print(colorlist)
                if "white" in colorlist:
                    print("!23")
                else:
                    print("yes")
##                pgrid.getAllcolor())
##                if "red" in grid.getAllcolor():
##                    color=0
##                else:
##                    color=1
##                
##
##
##
##                if color==1:
##                    prompt1=Text(Point(4,9),"You got all the numbers right, congradulations!")
##                    prompt1.draw(win)
##                    pt=win.getMouse()
##                    prompt1.undraw()
##                else:
##                    prompt2=Text(Point(4,9),"Check your answers again and check if there's any box you have not filled yet.")
##                    prompt2.draw(win)
##                    pt=win.getMouse()
##                    prompt2.undraw()
##    ##                        

        


