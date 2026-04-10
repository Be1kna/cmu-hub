#Palette
palette0 = 'goldenrod'
palette00 = 'indigo'
palette1 = 'crimson'
palette11 = 'lime'
palette2 = 'greenYellow'
palette22 = 'mediumVioletRed'
palette3 = 'green'
palette33 = 'lightCoral'
palette4 = 'blue'
palette44 = 'darkOrange'
palette5 = 'indigo'
palette55 = 'goldenrod'

#Imports
import random

#starting functions
def text(color3): #label color change
    text = Label('Press to roll a dice',200,30,size=30,font='monospace',bold=True,fill=color3)
    return ''
def diceroll(): #rolling a dice
    roll = random.randint(1,6) #rolling a digit
    
    #dice cube
    Circle(120,120,20,fill='ivory')
    Circle(280,120,20,fill='ivory')
    Circle(120,280,20,fill='ivory')
    Circle(280,280,20,fill='ivory')
    #drawing dots
    if roll == 1:
        Circle(200,200,25)
        return ''
    elif roll == 2:
        Circle(150,150,25)
        Circle(250,250,25)
        return ''
    elif roll == 3:
        Circle(150,150,25)
        Circle(200,200,25)
        Circle(250,250,25)
        return ''
    elif roll == 4:
        Circle(150,150,25)
        Circle(150,250,25)
        Circle(250,150,25)
        Circle(250,250,25)
        return ''
    elif roll == 5:
        Circle(150,150,25)
        Circle(150,250,25)
        Circle(250,150,25)
        Circle(250,250,25)
        Circle(200,200,25)
        return ''
    elif roll == 6:
        Circle(140,150,25)
        Circle(140,250,25)
        Circle(260,150,25)
        Circle(260,250,25)
        Circle(200,150,25)
        Circle(200,250,25)
        return ''
    pass

def palette():
    Rect(0,0,400,400,fill=None,border='black')
    Rect(20,320,40,40,fill=palette1,border='black')
    Rect(100,320,40,40,fill=palette2,border='black')
    Rect(180,320,40,40,fill=palette3,border='black')
    Rect(260,320,40,40,fill=palette4,border='black')
    Rect(340,320,40,40,fill=palette5,border='black')
    return ''
    
Rect(0,0,400,400,fill=palette0) #default background
print(text(palette00)) #default text
print(palette()) #palette boxes
    
#background change and dice rolling
def onMousePress(x,y):
    if y < 360 and y > 320 and x < 60 and x > 20: #first color
        Rect(0,0,400,400,fill=palette1)
        Rect(100,100,200,200,fill='ivory')
        Rect(100,100,20,20,fill=palette1)
        Rect(100,100,20,20,fill=palette1)
        Rect(280,280,20,20,fill=palette1)
        Rect(280,280,20,20,fill=palette1)
        print(palette())
        print(diceroll())
        print(text(palette11))
    elif y < 360 and y > 320 and x < 140 and x > 100: #second color
        Rect(0,0,400,400,fill=palette2)
        Rect(100,100,200,200,fill='ivory')
        Rect(100,100,20,20,fill=palette2)
        Rect(100,100,20,20,fill=palette2)
        Rect (280,100,20,20,fill=palette2)
        Rect (100,280,20,20,fill=palette2)
        Rect (280,280,20,20,fill=palette2)
        print (palette())
        print (diceroll())
        print (text(palette22))
    elif y < 360 and y > 320 and x < 220 and x > 180: #third color
        Rect (0,0,400,400,fill=palette3)
        Rect (100,100,200,200,fill='ivory')
        Rect (100,100,20,20,fill=palette3)
        Rect (280,100,20,20,fill=palette3)
        Rect (100,280,20,20,fill=palette3)
        Rect (280,280,20,20,fill=palette3)
        print (palette())
        print (diceroll())
        print (text(palette33))
    elif y < 360 and y > 320 and x < 300 and x > 260: #forth color
        Rect (0,0,400,400,fill=palette4)
        Rect (100,100,200,200,fill='ivory')
        Rect (100,100,20,20,fill=palette4)
        Rect (280,100,20,20,fill=palette4)
        Rect (100,280,20,20,fill=palette4)
        Rect (280,280,20,20,fill=palette4)
        print (palette())
        print (diceroll())
        print (text(palette44))
    elif y < 360 and y > 320 and x < 380 and x > 340: #fifth color
        Rect (0,0,400,400,fill=palette5)
        Rect (100,100,200,200,fill='ivory')
        Rect (100,100,20,20,fill=palette5)
        Rect (280,100,20,20,fill=palette5)
        Rect (100,280,20,20,fill=palette5)
        Rect (280,280,20,20,fill=palette5)
        print (palette())
        print (diceroll())
        print (text(palette55))
    else: #default color
        Rect (0,0,400,400,fill=palette0)
        Rect (100,100,200,200,fill='ivory')
        Rect (100,100,20,20,fill=palette0)
        Rect (280,100,20,20,fill=palette0)
        Rect (100,280,20,20,fill=palette0)
        Rect (280,280,20,20,fill=palette0)
        print (palette())
        print (diceroll())
        print (text (palette00))
