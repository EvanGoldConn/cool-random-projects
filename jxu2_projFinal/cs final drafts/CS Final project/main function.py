#CS Final Project
#Jing
#5/16
#Prank Sudoku
#This project initialize a Sudoku question
#But after the user inputs his answer, he will get a prank
from graphics import*
from ButtonClass import*
from GridClass import*
from Sudoku import*


 
def main():
    win1=GraphWin("Sudoku menu",600,600)
    win1.setCoords(0,0,600,600)
    prompt1=Text(Point(300,500),"Sudoku")
    prompt1.draw(win1)
    easybutton=Button(win1,Point(300,300),200,50,"Easiest Sudoku in the world")

    quitbutton=Button(win1,Point(500,100),50,30,"Quit")
    pt=win1.getMouse()
    
#    while not quitbutton.isClicked(pt):
    if easybutton.isClicked(pt):
        win1.close()
        easylevel()
        #pt=win1.getMouse()
    elif quitbutton.isClicked(pt):
        win1.close()


def easylevel():
    win2=GraphWin("Easy Sudoku",600,600) #open up another window
    game=Sudoku(win2,"easy")



main()
