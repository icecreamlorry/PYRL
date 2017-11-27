import os
import click

def clear():
    os.system('cls')

def getMapSize(inMap):
    mapSize = [len(inMap[0]), len(inMap)]
    return mapSize

def render(inMap, inCharPos):
    mapString = ''
    for y, line in enumerate(inMap):
        for x, char in enumerate(line):
            if x == inCharPos[0] and y == inCharPos[1]:
                mapString += '@'
            else:
                mapString += char
    return mapString

def main():
    charPos = [2, 2]

    fullMap = open('map.txt', 'r').readlines()
    
    mapSize = getMapSize(fullMap)
    screenWidth = mapSize[0]
    screenHeight = mapSize[1]

    clear()
    backBufferString = render(fullMap, charPos)
    click.echo(backBufferString)

    while True:
        char = click.getchar()
        if char == b'w':
            charPos[1] = max(1, charPos[1]-1)
        elif char == b's':
            charPos[1] = min(screenHeight-2, charPos[1]+1)
        elif char == b'a':
            charPos[0] = max(1, charPos[0]-1)
        elif char == b'd':
            charPos[0] = min(screenWidth-2, charPos[0]+1)

        clear()
        backBufferString = render(fullMap, charPos)
        click.echo(backBufferString)

main()
