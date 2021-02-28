#April 15 2018
#Jing and Tatiana
from graphics import *

#create a button class to call later
class Button:
    """A button is a labeled rectange in a window. It is enabled
    or disabled with the activate() and deactivate() methods.
    The isClicked(pt) method returns True if and only if the button is enabled
    and pt has to be 'inside' the button."""

    def __init__(self, win, center, width, height, label):
        """creates a rectanguar button where:
        win is the GraphWin object where the button will be drawn
        center is a Point object the button will be centered on
        width is an integer specifying the width of the button
        height is an integer specifying the height of the button
        label is a string that will appear on the button
        e.g. quitButton = Button(myWin, centerPoint, width, height, "Quit")"""
        #write code here to build and draw the button
        self.x = center.getX()
        self.y = center.getY()
        self.xmax = self.x + width/2
        self.xmin = self.x - width/2
        self.ymax = self.y + height/2
        self.ymin = self.y - height/2
        self.rect = Rectangle(Point(self.xmin,self.ymax),Point(self.xmax,self.ymin))
        self.rect.draw(win)
        self.rect.setFill("white")
        self.words = Text(Point(self.x,self.y), label)
        self.words.draw(win)
        self.activate()
    # a method called activate to make sure the button looks "acticated"
    #letting the user know they can click the button

    def drawlabel(self,win,text):
        self.words.setText(text)

    def returnText(self):
        return self.words.getText()

    def activate(self):
        """Activates the button by raising the boolean flag active and making the
        boundary bolder"""
        self.active = True #flag for recording weather we are in active mode
        self.words.setFill("black")
        self.rect.setWidth(2)

    #a method called deactivate where the user knows not to click
    #the button since it looks grayed out
    def deactivate(self):
        """deactivate the button bu lowering the boolean flag active
        and making the boundary thinner and graying out the label."""
        self.active = False
        self.words.setFill("darkgray")
        self.rect.setWidth(1)
        
    #a method to check if the user clicked the button
    def isClicked(self,pt):
        """returns True if button is active and Point pt is on the button.
        Otherwise returns False"""
        if self.active and (pt.getX() <= self.xmax and pt.getX() >= self.xmin
                        and pt.getY() <= self.ymax and pt.getY() >= self.ymin):
            return True
        else:
            return False

    def setColor(self,color):
        self.rect.setFill(color)

    def entryobject(self,win):
        self.win=win
        input_text=Entry(Point(self.x,self.y),1)
        input_text.draw(win)
        


if __name__ == '__main__':
    main()

