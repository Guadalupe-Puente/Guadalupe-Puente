#Guadalupe Puente
#4.7.2.1 PROYECTO: TIC-TAC-TOE

def printingboard():
    flippedboard = np.flip(Board, 0)
    print(flippedboard)
    print("")
 
def drawboard():
    drawlines()
    drawfigures()
 
def drawlines():
    pygame.draw.line(Screen, colorofline, (0, 200), (600, 200), 10)
    pygame.draw.line(Screen, colorofline, (0, 400), (600, 400), 10)
    pygame.draw.line(Screen, colorofline, (200, 0), (200, 600), 10)
    pygame.draw.line(Screen, colorofline, (400, 0), (400, 600), 10)
 
def drawfigures():
    for col in range(Columns):
        for row in range(Rows):
            if Board[row][col] == 1:
                pygame.draw.circle(Screen, colorofcircle, (int(col * sizeofsquare + sizeofsquare / 2), int(row * sizeofsquare + sizeofsquare / 2)), radiusofcircle, circlelinewidth)
            elif Board[row][col] == 2:
                pygame.draw.line(Screen, xcolor, (col * sizeofsquare + offset, row * sizeofsquare + offset), (col * sizeofsquare + sizeofsquare - offset, row *sizeofsquare + sizeofsquare - offset), xlinewidth)
                pygame.draw.line(Screen, xcolor, (col * sizeofsquare + offset, row * sizeofsquare + sizeofsquare - offset), (col * sizeofsquare + sizeofsquare - offset, row * sizeofsquare + offset), xlinewidth)
 
def fullboard():
    for col in range(Columns):
        for row in range(Rows):
            if Board[row][col] == 0:
                return False
 
    return True