# Fill me in!
#Sky and mountains
Rect(0,0,400,100,fill=gradient('lightBlue','royalBlue',start='bottom'))
RegularPolygon(80,80,40,3,fill=gradient('lightSteelBlue','lightSlateGrey',start='bottom'))
RegularPolygon(130,80,60,3,fill=gradient('lightSteelBlue','lightSlateGrey',start='bottom'))
RegularPolygon(270,80,60,3,fill=gradient('lightSteelBlue','lightSlateGrey',start='bottom'))
RegularPolygon(230,90,30,3,fill=gradient('lightSteelBlue','lightSlateGrey',start='bottom'))

#Sun
Star(380,20,140,18, roundness=10,fill=gradient('yellow','gold'),opacity=50)
Star(380,20,80,18, roundness=20,fill=gradient('yellow','gold'),opacity=80)
Circle(380,20,20,fill=gradient('yellow','gold'))

#Bushes
Oval(40,100,50,40,fill='green')
Oval(150,90,70,40,fill='green')
Oval(100,100,50,30,fill='forestGreen')
Oval(290,100,60,30,fill='green')
Oval(330,100,65,40,fill='forestGreen')

#Grass
Rect(0,100,400,300,fill=gradient('seaGreen','limeGreen',start='bottom-left'))
Oval(140,180,140,80,fill='limeGreen',opacity=40)
Oval(290,230,180,120,fill='limeGreen',opacity=40)
Oval(100,320,170,120,fill='limeGreen',opacity=40)
Oval(360,410,200,150,fill='limeGreen',opacity=40)

#Circus Tent
def circus(x,y,size):
    Polygon(x-size, y+size*7, x, y, x+size*7, y, x+size*8, y+size*7, fill=gradient('crimson','fireBrick',start='top'))
    Line(x+size, y, x, y+size*7, fill='navajoWhite',lineWidth=size*0.8)
    Line(x+size*2.5, y, x+size*2, y+size*7, fill='navajoWhite',lineWidth=size*0.8)
    Line(x+size*4.5, y, x+size*5, y+size*7, fill='navajoWhite',lineWidth=size*0.8)
    Line(x+size*6, y, x+size*7, y+size*7, fill='navajoWhite',lineWidth=size*0.8)
    Polygon(x, y+size*0.5, x-size, y, x+size, y-size*0.5, x+size*3.5, y-size*3, x+size*6, y-size*0.5, x+size*8, y, x+size*7, y+size*0.5, fill=gradient('crimson','fireBrick',start='top'))
    #Entrance
    Polygon(x+size, y+size*7, x, y+size*5.5, x+size*3.5, y+size*2.5, fill='darkRed')
    Polygon(x+size*3.5, y+size*2.5, x+size*7, y+size*5.5, x+size*6, y+size*7,fill='darkRed')
    Polygon(x+size, y+size*7, x+size*3.5, y+size*2.5, x+size*6, y+size*7, fill=rgb(100,0,0))

#Food Stand
def stand(x,y,text,size):
    red = rgb(220,70,50)
    Line(x+size*0.6, y-size*7, x+size*0.6, y, lineWidth=size*0.6, fill='lightCoral',opacity=60)
    Line(x+size*0.6, y-size*7, x+size*0.6, y, lineWidth=size*0.4, fill='maroon',dashes=(6,2))
    Line(x+size*11.4, y-size*7, x+size*11.4, y, lineWidth=size*0.6, fill='lightCoral',opacity=60)
    Line(x+size*11.4, y-size*7, x+size*11.4, y, lineWidth=size*0.4, fill='maroon',dashes=(6,2))
    Polygon(x, y-size*7, x+size, y-size*10, x+size*11, y-size*10, x+size*12, y-size*7, fill=red)
    Label(text,x+size*6, y-size*8.5, size=size*2, font='montserrat',bold=True,fill='ivory')
    
    #Food
    Rect(x+size*1.5, y-size*2.5, size*5, size*0.3, fill='gold')
    Rect(x+size*1.5, y-size*2.2, size*5, size*2.5, fill='goldenrod')
    #Hot Dog
    if text == 'Hot Dog':
        Rect(x+size*8, y-size*3, size, size*3, fill='crimson')
        Rect(x+size*8.3, y-size*3.6, size*0.4, size*0.6, fill='crimson')
        Rect(x+size*9.5, y-size*3, size, size*3, fill='lightYellow')
        Rect(x+size*9.8, y-size*3.6, size*0.4, size*0.6, fill='lightYellow')
    #Popcorn
    if text == 'Popcorn':
        Circle(x+size*7.7, y-size*3, size*0.5, fill=gradient('khaki','goldenrod','darkGoldenrod'))
        Circle(x+size*8.7, y-size*3.3, size*0.5, fill=gradient('khaki','goldenrod','darkGoldenrod'))
        Circle(x+size*8.8, y-size*4.2, size*0.5, fill=gradient('khaki','goldenrod','darkGoldenrod'))
        Circle(x+size*9.4, y-size*3.5, size*0.5, fill=gradient('khaki','goldenrod','darkGoldenrod'))
        Circle(x+size*9.8, y-size*2.8, size*0.5, fill=gradient('khaki','goldenrod','darkGoldenrod'))
        Circle(x+size*8, y-size*3.8, size*0.5, fill=gradient('khaki','goldenrod','darkGoldenrod'))
        Polygon(x+size*7.5, y, x+size*7, y-size*3, x+size*10.5, y-size*3, x+size*10, y, fill=gradient('red','white','red','white','red','white','red','white','red','white','red',start='left'),borderWidth=size*0.2,border='crimson')
    
    #Bottom Part
    step = size*1.2
    ySize = size*6
    Rect(x+size*0.5, y, step, ySize, fill='cornSilk')
    Rect(x+step + size*0.5, y, step, ySize, fill=red)
    Rect(x+step*2 + size*0.5, y, step, ySize, fill='cornSilk')
    Rect(x+step*3 + size*0.5, y, step, ySize, fill=red)
    Rect(x+step*4 + size*0.5, y, step, ySize, fill='cornSilk')
    Rect(x+step*5 + size*0.5, y, step, ySize, fill=red)
    Rect(x+step*6 + size*0.5, y, step, ySize, fill='cornSilk')
    Rect(x+step*7 + size*0.5, y, step, ySize, fill=red)
    Rect(x+step*8 + size*0.5, y, step, ySize, fill='cornSilk')
    Rect(x,y, step*10, ySize,fill=None,borderWidth=size*0.8,border=red)
    
    #Wheels
    if text == "Popcorn" or text == "Hot Dog":
        Circle(x+size*2.5, y+size*6, size*2.2, fill=None,borderWidth=size, border='saddleBrown')
        Star(x+size*2.5, y+size*6, size*1.8, 6,roundness=size*2, fill='saddleBrown')
        Circle(x+size*2.5, y+size*6, size*2, fill=None,borderWidth=size*0.6, border='goldenrod')
        Circle(x+size*9.5, y+size*6, size*2.2, fill=None,borderWidth=size, border='saddleBrown')
        Star(x+size*9.5, y+size*6, size*1.8, 6,roundness=size*2, fill='saddleBrown')
        Circle(x+size*9.5, y+size*6, size*2, fill=None,borderWidth=size*0.6, border='goldenrod')

#Ferris Wheel
#Carts
def carts(x,y,color,size):
    Rect(x-size*2, y, size*4, size*2, fill=color,borderWidth=size*0.2,border='darkBlue')
    Oval(x, y, size*4, size*2, fill=color,borderWidth=size*0.2,border='darkBlue')
    Oval(x, y+size*2, size*4, size*2, fill=color,borderWidth=size*0.2,border='darkBlue')
    Rect(x-size*1.8, y, size*3.6, size*2.2, fill=color)
    Oval(x, y+size*0.5, size*3.6, size*1.5, fill='powderBlue')
    
#Ferris Wheel Stand
def ferrisWheel(x,y,size):
    Star(x,y,size*11,10,roundness=20,fill='skyBlue')
    Star(x,y,size*11,10,roundness=20,fill='salmon',rotateAngle=15)

    #Ferris Wheel Support
    Line(x, y, x+size*4, y+size*13, lineWidth=size*0.8, fill='darkSlateGrey')
    Line(x, y, x-size*4, y+size*13, lineWidth=size*0.8, fill='darkSlateGrey')
    Circle(x, y, size*3, fill='darkSlateGrey')
    Rect(x-size*6, y+size*12, size*12, size*2, fill='salmon',borderWidth=size*0.4,border='darkSlateGrey')
    Line(x-size*5, y+size*13, x+size*5, y+size*13, fill='darkSlateGrey',dashes=(4,4))
    Star(x, y, size*2.5, 5, fill=rgb(200,180,255))

    #Cart's Ring
    Circle(x,y,size*9,fill=None,borderWidth=size,border='mediumSlateBlue')
    Circle(x,y,size*6,fill=None,borderWidth=size,border='mediumSlateBlue')
    
    #Spawn carts
    carts(x,y-size*9,'paleVioletRed',size)
    carts(x+size*7.5,y-size*5,'darkTurquoise',size)
    carts(x+size*7.5,y+size*3,'orange',size)
    carts(x,y+size*8,'paleVioletRed',size)
    carts(x-size*7.5,y+size*3,'darkTurquoise',size)
    carts(x-size*7.5,y-size*5,'orange',size)
  
#Spawn Everything  
ferrisWheel(140,90,8)
stand(15,200,'Popcorn',5)
circus(240,140,15)
stand(310,260,'Hot Dog',7)
stand(70,330,'Tickets',10)
