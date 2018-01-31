import os
import click

def clear():
    os.system('cls')

def setCharInMap(inMap, inPos, inChar):
    mapArray = inMap[:]
    mapArray[inPos[1]] = mapArray[inPos[1]][:inPos[0]] + inChar + mapArray[inPos[1]][inPos[0] + 1:]
    return mapArray

def getCharInMap(inMap, inPos):
    return inMap[inPos[1]][inPos[0]]

def mapToString(inMap):
    mapString = ''
    for i, line in enumerate(inMap):
        mapString += line
    return mapString

def main():
    fullMap = open('map.txt', 'r').readlines()
    mapSize = [len(fullMap[0]) - 1, len(fullMap)]
    position = [1, 1]

    clear()
    backBufferString = mapToString(fullMap)
    click.echo(backBufferString)

    while True:
        char = click.getchar()
        fullMap, position = update(fullMap, mapSize, char, position)
        draw(fullMap)

def update(inMap, mapSize, inputChar, position):
    if inputChar == b's':
        if position[1] < mapSize[1] - 2:
            position[1] += 1
    if inputChar == b'w':
        if position[1] > 1:
            position[1] -= 1

    if inputChar == b'd':
        if position[0] < mapSize[0] - 2:
            position[0] += 1
    if inputChar == b'a':
        if position[0] > 1:
            position[0] -= 1

    inMap = setCharInMap(inMap, position, "@")
    return inMap, position

def draw(inMap):
    clear()
    backBufferString = mapToString(inMap)
    click.echo(backBufferString)

main()
