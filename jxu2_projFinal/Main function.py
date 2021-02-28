#CS Final Project
#Jing
#5/10
#Sudoku game including 3 levels, and infinite check functions.
#The right answer will be green, the red answer will be red

from graphics import*
from ButtonClass import*
from GridClass import*
from Sudoku import*


def easylevel(): #sub-functions for different levels
    game=Sudoku("easy")
    
def mediumlevel():
    game=Sudoku("medium")

def hardlevel():
    game=Sudoku("hard")


def main():
    #A menu window for the user including descriptions and choices of levels
    win1=GraphWin("Sudoku menu",600,600)
    win1.setCoords(0,0,600,600)
    prompt1=Text(Point(300,570),"Sudoku")
    prompt1.draw(win1) #Descriptions
    prompt2=Text(Point(300,550),"This is a Sudoku game program. You can choose three levels of difficulty.")
    prompt2.draw(win1)
    prompt3=Text(Point(300,530),"Once you start a game, there's no quit button, although you can close the window to close the game.")
    prompt3.draw(win1)
    prompt4=Text(Point(300,510),"There will be infinite chances for checking.")
    prompt4.draw(win1)
    prompt5=Text(Point(300,490),"A right answer will appear to be green, a wrong one will appear to be red.")
    prompt5.draw(win1)
    prompt6=Text(Point(300,470),"Once all the entry squares are green, you win the game.")
    prompt6.draw(win1)
    easybutton=Button(win1,Point(300,400),100,50,"Easy") #different levels
    mediumbutton=Button(win1,Point(300,300),100,50,"Medium")
    hardbutton=Button(win1,Point(300,200),100,50,"Hard")
    quitbutton=Button(win1,Point(500,100),50,30,"Quit")
    pt=win1.getMouse()
    while not quitbutton.isClicked(pt):
        if easybutton.isClicked(pt):
            win1.close() #Since the sudoku class opens another window, the previous window is closed after clicked
            easylevel()
        elif mediumbutton.isClicked(pt):
            win1.close()
            mediumlevel()
        elif hardbutton.isClicked(pt):
            win1.close()
            hardlevel()
            #pt=win1.getMouse()
    win1.close()

#answerMatrix()
main()
