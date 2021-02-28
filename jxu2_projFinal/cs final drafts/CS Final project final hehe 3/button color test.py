from graphics import*
from ButtonClass import*

def main():
    win=GraphWin("123",600,600)
    button1=Button(win,Point(300,300),50,50,"test")
    button1.setColor("blue")
    print(button1.returnColor())


main()
