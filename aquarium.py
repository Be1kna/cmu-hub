# Fill me in!
#Background
app.background=gradient('peru','burlyWood',start='bottom-left')

#Table
Rect(15,370,10,100,fill='saddleBrown')
Rect(375,370,10,100,fill='saddleBrown')
Rect(45,310,10,100,fill='saddleBrown')
Rect(345,310,10,100,fill='saddleBrown')
Polygon(10,370,40,310,360,310,390,370,fill='saddleBrown',border=rgb(100,50,0),borderWidth=4)

#Aquarioum
aquarioum = Group(
    Polygon(30,360,50,320,350,320,370,360,fill='darkGrey',opacity=15,border='steelBlue'),
    Rect(50,110,300,210,fill='darkGrey',opacity=15,border='steelBlue'),
    Polygon(30,360,30,130,50,110,50,320,fill='darkGrey',opacity=15,border='steelBlue'),
    Polygon(350,110,370,130,370,360,350,320,fill='darkGrey',opacity=15,border='steelBlue')
    )


#Spawn Fish
def fishSpawn(x,y,size,side,color):
    s = size
    f = Group()
    if side == 'right':
        f.add(
            Oval(x+s,y,s*6,s*3.5,fill=color),
            Polygon(x-s,y,x-s*4,y-s*2,x-s*4,y+s*2,fill=color),
            Circle(x+s*2.5,y-s*0.7,s*0.5)
        )
    if side == 'left':
        f.add(
            Oval(x-s,y,s*6,s*3.5,fill=color),
            Polygon(x+s,y,x+s*4,y+s*2,x+s*4,y-s*2,fill=color),
            Circle(x-s*2.5,y-s*0.7,s*0.5)
        )
    return f

#Ranges for fish colors and sides
sides = ['left','right']
colors = ['red','salmon','darkOrange','yellow','gold','lime','green','aquamarine','skyBlue','dodgerBlue','violet','slateBlue','hotPink','chocolate','snow','dimGrey']

#Initialize Fishes
fish1 = fishSpawn(120,200,10,'left',choice(colors))
fish2 = fishSpawn(220,310,10,'right',choice(colors))
fish3 = fishSpawn(280,230,10,'left',choice(colors))
fishes = [fish1,fish2,fish3]

#Front panel glass and water
waterLayer = Group(
    Polygon(30,160,50,140,350,140,370,160,fill='cornflowerBlue',opacity=35,border='royalBlue'),
    Rect(30,160,340,200,fill='cornflowerBlue',opacity=35))

aquarioum2 = Group(
    Rect(30,130,340,230,fill='darkGrey',opacity=15,border='steelBlue'))


#Spawn invisible hearts
def spawnHearts(x,y):
    y -= 30
    h = Group(
        Polygon(x,y-6,x+5,y-10,x+10,y-7,x+10,y,x,y+10,x-10,y,x-10,y-7,x-5,y-10,fill='lightPink',border='red',borderWidth=2)
        )
    h.visible=False
    return h

#initialize hearts
hearts = [spawnHearts(120,200),spawnHearts(220,310),spawnHearts(280,230)]
heartTimer = [0,0,0]


#Button UI
Rect(20,20,100,60,fill='khaki')
Label('Clean',70,50,size=25)

Rect(150,20,100,60,fill='khaki')
Label('Feed',200,50,size=25)

Rect(280,20,100,60,fill='khaki')
Label('New',330,50,size=25)


#Mouse Presses
def onMousePress(x,y):
    if y <= 80 and y >= 20:
        
        #Clean Button
        if x <=120 and x >= 20:
            aquarioum.opacity = 15
            aquarioum2.opacity = 15
        
        #Feed Button
        if x <=250 and x >= 150:
            starvingFish = [
                f for f in fishes 
                if f.left > 33 and f.right < 367 and f.bottom < 357 and f.top > 143]
            if len(starvingFish) > 0:
                totalFishes = len(fishes)
                fish = choice(starvingFish)
                fish.width += 9
                fish.height += 5.25
        
        #New Button
        if x <=380 and x >= 280:
            
            #Spawn new fish
            fishX = randrange(70,330)
            fishY = randrange(160,340)
            fishSize = randrange(8,12)
            side = choice(sides)
            newColor = choice(colors)
            newFish = fishSpawn(fishX,fishY,fishSize,side,newColor)
            fishes.append(newFish)
            
            #Spawn invisible heart
            newHeart = spawnHearts(fishX,fishY)
            hearts.append(newHeart)
            heartTimer.append(0)
            
            #Glass and water layer to front
            aquarioum2.toFront()
            waterLayer.toFront()


#Mouse Releases   
def onMouseRelease(x,y):
    for fish in fishes:
        
        #Make the heart visible
        if x > fish.left and x < fish.right and y > fish.top and y < fish.bottom:
            index = fishes.index(fish)
            hearts[index].visible = True
            heartTimer[index] = 5
            
    
    
#Animation
def onStep():
    
    #Glass getting dirtier
    if aquarioum.opacity < 80:
        aquarioum.opacity += 0.1
        aquarioum2.opacity += 0.1
    
    for fish in fishes:
        index = fishes.index(fish)
        
        #Fishes getting smaller or disapearing
        if fish.width <= 30:
            fish.visible = False
            hearts[index].visible = False
            fishes.remove(fish)
            hearts.pop(index)
            heartTimer.pop(index)
        else:
            fish.width -= 0.09
            fish.height -= 0.05
        
            #Make the heart disapear after some time
            if heartTimer[index] <= 0:
                hearts[index].visible = False
            else:
                heartTimer[index] -= 0.333
        
print('''Welcome to my aquarium simulator!
    Feed the fishes so they dont starve
    Clean the aquarium glass to see better
    Add as many new fish as you would like
    And you can also pet them!''')
