#quick change variables
logolines = 'white'
width = 10
background = 'midnightBlue'
lines = 'lightCyan'
outline = 'lime'
#logo
Rect(0,0,400,400,fill=background)
Circle(200,200,150,fill=gradient('powderBlue','steelBlue',start='top',),border=logolines,borderWidth=width)
#lines
Line(200,60,200,340,fill=logolines,lineWidth=width)
Oval(200,200,175,300,fill=None,border=logolines,borderWidth=width)
Line(60,200,340,200,fill=logolines,lineWidth=width)
Oval(200,60,300,175,fill=None,border=logolines,borderWidth=width)
Oval(200,340,300,175,fill=None,border=logolines,borderWidth=width)
Circle(200,200,250,fill=None,border=background,borderWidth=100)
#connection
Line(30,30,370,30,fill=lines,lineWidth=5)
Line(370,30,370,370,fill=lines,lineWidth=5)
Line(370,370,40,370,fill=lines,lineWidth=5)
Line(30,370,30,30,fill=lines,lineWidth=5)
dot=Circle(30,30,10,fill='red',border=lines,borderWidth=3)
#computers
Line(40,65,60,65,fill=outline,lineWidth=5)
Rect(20,20,60,40,border=outline)
Line(340,65,360,65,fill=outline,lineWidth=5)
Rect(320,20,60,40,border=outline)
Line(340,385,360,385,fill=outline,lineWidth=5)
Rect(320,340,60,40,border=outline)
Line(40,385,60,385,fill=outline,lineWidth=5)
Rect(20,340,60,40,border=outline)

#moving dot
def onMousePress(mouseX,mouseY):
    if dot.centerY == 30:
        dot.centerX=dot.centerX+20
    if dot.centerX == 370:
        dot.centerY=dot.centerY+20
    if dot.centerY == 370:
        dot.centerX=dot.centerX-20
    if dot.centerX == 30:
        dot.centerY=dot.centerY-20