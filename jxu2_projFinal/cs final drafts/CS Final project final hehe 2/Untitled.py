#CS Final Project
#Jing
#5/10
#1.make a big 3x3 grid. for each button in the grid, make 3x3 grid again.
from graphics import*
from ButtonClass import*
from GridClass import*
from Sudoku import*


def easylevel():
 #   win2=GraphWin("Easy Sudoku",600,600)
    game=Sudoku("easy")
    
def mediumlevel():
 #   win3=GraphWin("Medium Sudoku",600,600)
    game=Sudoku("medium")

def hardlevel():
 #   win4=GraphWin("Hard Sudoku",600,600)
    game=Sudoku("hard")


def main():
    win1=GraphWin("Sudoku menu",600,600)
    win1.setCoords(0,0,600,600)
    prompt1=Text(Point(300,500),"Sudoku")
    prompt1.draw(win1)
    easybutton=Button(win1,Point(300,400),100,50,"Easy")
    mediumbutton=Button(win1,Point(300,300),100,50,"Medium")
    hardbutton=Button(win1,Point(300,200),100,50,"Hard")
    quitbutton=Button(win1,Point(500,100),50,30,"Quit")
    pt=win1.getMouse()
#    while not quitbutton.isClicked(pt):
    if easybutton.isClicked(pt):
        win1.close()
        easylevel()
    elif mediumbutton.isClicked(pt):
        win1.close()
        mediumlevel()
    elif hardbutton.isClicked(pt):
        win1.close()
        hardlevel()
        #pt=win1.getMouse()
        

#answerMatrix()
main()
