# Fill me in!
import colorsys
#Current colors
curR = 255
curG = 200
curB = 0
curI = 10
background = Rect(0,0,400,400,fill=rgb(0,42,255))

#Shift the hue
def hueS(r,g,b,shift):
    h, s, v = colorsys.rgb_to_hsv(r,g,b)
    h = (h+shift/800)%1.0
    rNew, gNew, bNew = colorsys.hsv_to_rgb(h,s,v)
    return rNew,gNew,bNew

#Reset Saturation
def resetContrast(r,g,b,contrast):
    h, s, v = colorsys.rgb_to_hsv(r/255,g/255,b/255)
    s = min(contrast,1.0)
    v = min(contrast,1.0)
    rNew, gNew, bNew = colorsys.hsv_to_rgb(h,s,v)
    return rNew*255,gNew*255,bNew*255

#Shift darkness
def light(r,g,b,i):
    if (r+i) >= 255:
        rL = 255
        rD = r-i
    elif (r-i) <= 0:
        rL = r+i
        rD = 0
    else:
        rL = r+i
        rD = r-i
    if (g+i) >= 255:
        gL = 255
        gD = g-i
    elif (g-i) <= 0:
        gL = g+i
        gD = 0
    else:
        gL = g+i
        gD = g-i
    if (b+i) >= 255:
        bL = 255
        bD = b-i
    elif (b-i) <= 0:
        bL = b+i
        bD = 0
    else:
        bL = b+i
        bD = b-i
    return rL,rD,gL,gD,bL,bD

#change the colors
def change(r,g,b,intensity):
    i=intensity
    #shift hue for Left and Right
    hueRL, hueGL, hueBL = hueS(r,g,b,-i)
    hueRR, hueGR, hueBR = hueS(r,g,b,i)
    #shift darkness for Lighter and Darker
    rL,rD,gL,gD,bL,bD = light(r,g,b,i)
    #shift hue and darkness (colorSideDarkness)
    #Ex.RLD - Red Left Darker
    hueRLL, hueGLL, hueBLL = hueS(rL,gL,bL,-i)
    hueRRL, hueGRL, hueBRL = hueS(rL,gL,bL,i)
    hueRLD, hueGLD, hueBLD = hueS(rD,gD,bD,-i)
    hueRRD, hueGRD, hueBRD = hueS(rD,gD,bD,i)
    
    #Row 1
    Rect(20,20,100,100,fill=rgb(hueRLL,hueGLL,hueBLL))
    Rect(150,20,100,100,fill=rgb(rL,gL,bL))
    Rect(280,20,100,100,fill=rgb(hueRRL,hueGRL,hueBRL))
    
    #Row 2
    Rect(20,150,100,100,fill=rgb(hueRL, hueGL, hueBL))
    Rect(150,150,100,100,fill=rgb(r,g,b))
    Rect(280,150,100,100,fill=rgb(hueRR, hueGR, hueBR))
    
    #Row 3
    Rect(20,280,100,100,fill=rgb(hueRLD,hueGLD,hueBLD))
    Rect(150,280,100,100,fill=rgb(rD,gD,bD))
    Rect(280,280,100,100,fill=rgb(hueRRD,hueGRD,hueBRD))
    
    
change(curR,curG,curB,curI)

def onMousePress(x,y):
    global curR,curG,curB,curI
    #shift darkness for Lighter and Darker
    rL,rD,gL,gD,bL,bD = light(curR,curG,curB,curI)
    #shift hue for Left and Right
    hueRL, hueGL, hueBL = hueS(curR,curG,curB,-curI)
    hueRR, hueGR, hueBR = hueS(curR,curG,curB,curI)
    #shift hue and darkness (colorSideDarkness)
    #Ex.RLD - Red Left Darker
    hueRLL, hueGLL, hueBLL = hueS(rL,gL,bL,-curI)
    hueRRL, hueGRL, hueBRL = hueS(rL,gL,bL,curI)
    hueRLD, hueGLD, hueBLD = hueS(rD,gD,bD,-curI)
    hueRRD, hueGRD, hueBRD = hueS(rD,gD,bD,curI)
    #Reset Saturation
    satR, satG, satB = resetContrast(curR,curG,curB,0.9)
    
    #First Row
    if x > 20 and x < 120 and y > 20 and y < 120:
        curR,curG,curB = hueRLL,hueGLL,hueBLL
        change(curR,curG,curB,curI)
    if x > 150 and x < 250 and y > 20 and y < 120:
        curR,curG,curB = rL,gL,bL
        change(curR,curG,curB,curI)
    if x > 280 and x < 380 and y > 20 and y < 120:
        curR,curG,curB = hueRRL,hueGRL,hueBRL
        change(curR,curG,curB,curI)
    
    #Second Row
    if x > 20 and x < 120 and y > 150 and y < 250:
        curR,curG,curB = hueRL,hueGL,hueBL
        change(curR,curG,curB,curI)
    if x > 150 and x < 250 and y > 150 and y < 250:
        curR,curG,curB = satR, satG, satB
        change(curR,curG,curB,curI)
    if x > 280 and x < 380 and y > 150 and y < 250:
        curR,curG,curB = hueRR,hueGR,hueBR
        change(curR,curG,curB,curI)
    
    #Third Row
    if x > 20 and x < 120 and y > 280 and y < 380:
        curR,curG,curB = hueRLD,hueGLD,hueBLD
        change(curR,curG,curB,curI)
    if x > 150 and x < 250 and y > 280 and y < 380:
        curR,curG,curB = rD,gD,bD
        change(curR,curG,curB,curI)
    if x > 280 and x < 380 and y > 280 and y < 380:
        curR,curG,curB = hueRRD,hueGRD,hueBRD
        change(curR,curG,curB,curI)
    
    background.fill=rgb(255-curR, 255-curG, 255-curB)
    