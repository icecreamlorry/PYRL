import os
import click

def clear():
    os.system('cls')

def setCharInMap(inMap, inPos, inChar):
    mapArray = inMap[:]
    mapArray[inPos[1]] = mapArray[inPos[1]][:inPos[0]] + inChar + mapArray[inPos[1]][inPos[0] + 1:]
    return mapArray

def mapToString(inMap):
    mapString = ''
    for i, line in enumerate(inMap):
        mapString += line
    return mapString

def main():
    fullMap = open('map.txt', 'r').readlines()
    mapSize = [len(fullMap[0]), len(fullMap)]

    clear()
    backBufferString = mapToString(fullMap)
    click.echo(backBufferString)

    while True:
        char = click.getchar()
        update(mapSize, char)
        draw(fullMap)

def update(mapSize, inputChar):
    #make the game react to input here
    #this can't be empty so...
    LB = 'god'

def draw(inMap):
    clear()
    backBufferString = mapToString(inMap)
    click.echo(backBufferString)

main()
