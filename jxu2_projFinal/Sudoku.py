#Jing
#game class
#initialize the game and check user's answers
from graphics import*
from ButtonClass import*
from GridClass import*

class Sudoku:

    def __init__(self,level):
        self.level=level
        
        SIZE=9
        win=GraphWin(level+"Sudoku",600,600)
        win.setCoords(-3,-3,SIZE+2,SIZE+2)
        grid=Grid(win,0,0,9,9,1,1," ") #Make a grid
        checkbutton=Button(win,Point(4,10),2,1,"Check")
        prompt1=Text(Point(4,9),"Click check to check your answers. A right answer will appear as green, a wrong answer will appear as red.")
        prompt1.draw(win)

        qfile=open(level+".txt","r") #modify the code so that it works for all the levels of difficulty
        qdata=qfile.readlines()
        #-----answerMatrix------
        infile=open(level+".txt","r")
        qdata=infile.readlines()

        cleandata=[]
        for item in qdata:
            newitem=item.strip() #To get rid of the "\n", and make the list cleaner
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
            self.cleandatalist.append(datalist) #Now the cleandatalist has exactly the same format as buttonmatrix 
        #--------answerMatrix------
        questionlist=[]
        answerlist=[]
        for item in qdata: #separate the answer and the question
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
                abutton=grid.getbutton(x,y) #put the questions (numbers) into the grid in a correct order
                abutton.drawlabel(win,questionlist[z])
                z=z+1
            y=y+1

        pt=win.getMouse()
        while True: #If an empty square is clicked, an entry box is shown and the user can input the answers.
            if not checkbutton.isClicked(pt):
                x=int(round(pt.getX()))
                y=int(round(pt.getY()))
                abutton1=grid.getbutton(y,x)
                if abutton1.returnText() == " ":
                    abutton1.entryobject(win)
                pt=win.getMouse()


            else: #check the user's answers
                for c in range(len(grid.buttonMatrix)):
                    for r in range(len(grid.buttonMatrix)):
                        eachbutton=grid.getbutton(c,r) #loop through every single button and check the user's input if there's any

                        if eachbutton.getentryText() != "":
                            userinput=eachbutton.getentryText()
                            userinput=userinput+"*" #modify the input so that it looks the same as it is in the textfile
                            correctanswer=self.cleandatalist[r][8-c] #modify the index so that the answerMatrix and the buttonMatrix matches perfectly
                            if userinput != correctanswer:
                                eachbutton.setColor("red") #if the answer is wrong, make the square red
        
                            else:
                                eachbutton.drawlabel(win,userinput)
                                eachbutton.setColor("Green") #if the answer is right, make the square green 
    
                pt=win.getMouse()




