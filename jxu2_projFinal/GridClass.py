from graphics import*
from ButtonClass import*

class Grid:
    def __init__(self, win, startX, startY, numCols, numRows, squareWidth, squareHeight, text):

        self.buttonMatrix=[]
        self.numCols=numCols
        self.numRows=numRows
        self.startY=startY
        self.startX=startX
        self.text=text
        
        for y in range(startY,numRows):
            ButtonList=[]
            for x in range(startX,numCols):
                ButtonList.append(Button(win, Point(x,y),squareWidth,squareHeight,text))
                
            self.buttonMatrix.append(ButtonList)

    def getClickPos(self, clickPt):
        for i in self.buttonMatrix:
            for j in i:
                if j.isClicked(clickPt):
                    return (j.xmax//1), (j.ymax//1)

##        if self.buttonMatrix[x][y].isClicked(clickPt):
##            return x,y


    def getbutton(self,x,y): #return the specific button
        return self.buttonMatrix[x][y]


    def setSquareColor(self,x,y,color):
        self.buttonMatrix[x][y].setColor(color)




                    

        
