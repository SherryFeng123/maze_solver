#Starting positions
ORIGIN_X = -200
ORIGIN_Y = 200
side = 10
begin_x = ORIGIN_X - 10
begin_y = ORIGIN_Y

def readMaze(filename):
    matrix = []
    f = open(filename,'r')
    lines = f.readlines()

    for x in lines:
        my_list = []
        for y in x:
            if y == "#":
                y = 1
                my_list.append(y)
            elif y == " ":
                y = 0
                my_list.append(y)
        matrix.append(my_list)

    return matrix

def drawSquare(x,y,side, t, col = "black"): 
    t.penup()
    t.goto(x+ORIGIN_X,y+ORIGIN_Y)
    t.color(col)
    t.begin_fill()
    t.pendown()

    for i in range(0,4):
        t.forward(side)
        t.left(90)
    t.end_fill()

def drawMaze(maze,t,col):
    t.color(col)
    for index in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if maze[index][j] == 1:
                drawSquare(side*j, side*-index, side, t,"black")
                
wall = 1

def followLeftWall(maze,t,col):
    t.color(col)
    i = 1
    j = 0
    currDirection = "East"
    drawSquare(side*j,side*-i, side,t,col = "yellow")

    while i != len(maze)-2 or j != len(maze[0])-1:
        print("I went", currDirection)
        currDirection = nextMove(maze,i,j,currDirection)
        t.penup()
        t.goto(begin_x,begin_y)
        t.pendown()

        if currDirection == "East":
            j = j+1
        elif currDirection == "North":
            i = i-1
        elif currDirection == "South":
            i = i+1
        elif currDirection == "West":
            j = j-1      
        drawSquare(10*j,10*-i, 10,t,col = "yellow")



def nextMove(maze,i,j,currDirection):
    
    #checkEast
    if currDirection == "East":
        if maze[i-1][j] != wall:
            return "North"
        elif maze[i][j+1]  != wall:
            return "East"
        elif maze[i+1][j] != wall:
            return "South"
        elif maze[i][j-1] != wall:
            return "West"
        
    #checkNorth
    if currDirection == "North":
        if maze[i][j-1]  != wall:
            return "West"
        elif maze[i-1][j] != wall:
            return "North"
        elif maze[i][j+1]  != wall:
            return "East"
        elif maze[i+1][j]  != wall:
            return "South"
                
                
    #checkSouth
    if currDirection == "West":
        if maze[i+1][j]  != wall:
            return "South"
        elif maze[i][j-1] != wall:
            return "West"
        elif maze[i-1][j] != wall:
            return "North"
        elif maze[i][j+1]  != wall:
            return "East"
        
    #checkWest
    if currDirection == "South":
        if maze[i][j+1]  != wall:
            return "East"
        elif maze[i+1][j]  != wall:
            return "South"
        elif maze[i][j-1]  != wall:
            return "West"
        elif maze[i-1][j]  != wall:
            return "North"

def main(filename,algorithm): 
    import turtle
    t = turtle.Turtle()
    screen = turtle.Screen()
    maze = readMaze(filename) 
    screen.tracer(0)
    drawMaze(maze,t,"black")
    screen.update()
    screen.tracer(10)
    if algorithm == "followLeftWall":
        followLeftWall(maze,t,"yellow")

main("testMaze3.txt","followLeftWall")


