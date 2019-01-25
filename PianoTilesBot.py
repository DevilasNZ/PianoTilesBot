#this bot will automatically play paino tiles until it cannot keep up.
#the game can be found at http://tanksw.com/piano-tiles/
#turning the "show letters" option off may help performance.

import time
import pyautogui as gui

#track the positions of each of the tiles with this:
#use PositionFinder.py to find the points on the screen to click. note this is offset from the side of the game screen.
tilePositions = (50,150,250,350)#(1132, 1240, 1337, 1422)
tileY = 440
failCheckPosition = (50,50)#(1100,500)#check this pixel to find if the game is over.

#define the game area.(left,top,width,height)
gameArea = (1080, 247,500, 900)

#check each of the positions until a black tile is found. return the index of the tile
def checkTiles():
    while True:
        #capture the screen
        gameScreen = gui.screenshot(region=gameArea)

        #firstly, check the game isn't over.
        if gameScreen.getpixel(failCheckPosition) == (251, 62, 56):
            return -1

        #check the tiles, if one is black, return its index.
        for i in range(4):
            if gameScreen.getpixel((tilePositions[i],tileY)) == (17,17,17):
                return i

#find the index of the first three tiles. the bot will get these quickly, then continue
def findFirstThree():
    initialTileY = (400,250,100)
    initialTileIndices = [-1,-1,-1]
    gameScreen = gui.screenshot(region=gameArea)
    for i in range(4):
        #is the first tile here?
        if gameScreen.getpixel((tilePositions[i],initialTileY[0])) == (17,17,17):
            initialTileIndices[0] = i
        #is the second tile here?
        if gameScreen.getpixel((tilePositions[i],initialTileY[1])) == (17,17,17):
            initialTileIndices[1] = i
        #is the third tile here?
        if gameScreen.getpixel((tilePositions[i],initialTileY[2])) == (17,17,17):
            initialTileIndices[2] = i

    return initialTileIndices

#click the first three tiles, if they have been located, before proceeding to the main loop.
def clickFirstThree(firstIndices):
    keys = ('a','s','d','f')
    #first, click beside the game window to make sure the keys will register with the game.
    gui.click(gameArea[0]-50,gameArea[1])
    
    for i in range(3):
        gui.press(keys[firstIndices[i]])

#main game loop.
gameOver = False
keys = ('a','s','d','f')

firstIndices = findFirstThree()
print(firstIndices)
if -1 in firstIndices:
    raise ValueError("the bot could'nt find all the first three tiles. make sure the position of the game window and the tile positions are correct.")
else:
    clickFirstThree(firstIndices)

while not gameOver:
    #get the next black pixel
    tileToClick = checkTiles()
    if tileToClick == -1:
        gameOver = True
        print("game over!")
        if input("Play again? ") != "":
            gameOver = False
    else:
        #gui.click(tilePositions[tileToClick],tileY)
        gui.press(keys[tileToClick])
