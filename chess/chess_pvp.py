import pygame as pg
from pygame.constants import KEYDOWN
from pygame.locals import QUIT
import copy 

x ,y, chose_x ,chose_y, PressTimes ,a ,win = 0 ,7 ,-1, -1, 1 ,0 ,None
turn = True

#creat orginal chessboard
ChessBoard = [[3,4,5,6,10,5,4,3],            
              [2,2,2,2,2,2,2,2],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [-2,-2,-2,-2,-2,-2,-2,-2],
              [-3,-4,-5,-6,-10,-5,-4,-3]]

# chess location
chess_pos = [[(45,40),(89,40),(133,40),(177,40),(221,40),(266,41),(310,41),(354,41)],           
             [(45,87),(89,87),(133,87),(177,87),(221,87),(266,87),(310,87),(354,87)],
             [(45,132),(89,132),(133,132),(177,132),(221,132),(266,132),(310,132),(354,132)],
             [(45,176),(89,176),(133,176),(177,176),(221,176),(266,176),(310,176),(354,176)],
             [(45,221),(89,221),(133,221),(177,221),(221,221),(266,221),(310,221),(354,221)],
             [(45,266),(89,266),(133,266),(177,266),(221,266),(266,266),(310,266),(354,266)],
             [(45,311),(89,311),(133,311),(177,311),(221,311),(266,311),(310,311),(354,311)],
             [(45,355),(89,355),(133,355),(177,355),(221,355),(266,355),(310,355),(354,355)]]

#display every thing in the screen
def show():         
    screen.fill((255, 255, 255))
    checkerboard_picture = pg.image.load("C:/Users/User/Desktop/chess/checkerboard.jpg")
    screen.blit(checkerboard_picture,(5,5))

    for i in range(0 ,8 ,1):
        for j in range(0 ,8 ,1):
            if ChessBoard[i][j] == 0:
                continue
            elif ChessBoard[i][j] > 0:
                color = (255 ,0 ,0)
            else:
                color = (0 ,255 ,0)
            
            if i == chose_y and j == chose_x:
                color = (0 ,0 ,255)
            
            if abs(ChessBoard[i][j]) == 10:
                chess_kind = "K"
            elif abs(ChessBoard[i][j]) == 6:
                chess_kind = "Q"
            elif abs(ChessBoard[i][j]) == 5:
                chess_kind = "B"
            elif abs(ChessBoard[i][j]) == 4:
                chess_kind = "R"
            elif abs(ChessBoard[i][j]) == 3:
                chess_kind = "C"
            elif abs(ChessBoard[i][j]) == 2:
                chess_kind = "S"
            else:
                continue
                    
            font = pg.font.SysFont(None ,50)
            word = font.render(chess_kind,True,color)
            screen.blit(word,chess_pos[i][j])

            pg.draw.rect(screen ,(0, 0, 255), [chess_pos[y][x][0] - 5, chess_pos[y][x][1], 32, 32],3)

    pg.display.update()

#Promotion: When the Pawn go to the botton line,it must promote to any other chess except King.
def promotion():          
    if (chose_y-1 == 0 and abs(MoveRangeBoard[chose_y][chose_x]) == 2 and turn == True) or (chose_y+1 == 7 and abs(MoveRangeBoard[chose_y][chose_x]) == 2 and turn == False):
        screen.fill((255, 255, 255))
        chose_chess = pg.image.load("C:/Users/User/Desktop/chess/chose_chess.jpg")
        screen.blit(chose_chess,(10,5))
        pg.display.update()
        k = 0
        out = False
        pos = [110 ,186 ,264 ,338]

        while True:
            screen.fill((255, 255, 255))
            chose_chess = pg.image.load("C:/Users/User/Desktop/chess/chose_chess.jpg")
            screen.blit(chose_chess,(10,5))

            pg.draw.rect(screen ,(0, 0, 255),[24 ,pos[k], 370, 60],4)
            pg.display.update()

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                if event.type == KEYDOWN:
                    key = pg.key.get_pressed()
                    if key[pg.K_UP]:
                        if k != 0:
                            k -= 1
                    if key[pg.K_DOWN]:
                        if k != 3:
                            k += 1
                    if key[pg.K_SPACE]:
                        if k == 0:
                            if turn == True:
                                ChessBoard[y][x] = -3
                            else:
                                ChessBoard[y][x] = 3
                        if k == 1:
                            if turn == True:
                                ChessBoard[y][x] = -4
                            else:
                                ChessBoard[y][x] = 4
                        if k == 2:
                            if turn == True:
                                ChessBoard[y][x] = -6
                            else:
                                ChessBoard[y][x] = 6
                        if k == 3:
                            if turn == True:
                                ChessBoard[y][x] = -5
                            else:
                                ChessBoard[y][x] = 5
                        out = True
            if out == True:
                break

#The movement of King
def king(board ,turn ,y ,x):            
    if turn == True and board[y][x] < 0:
        if y + 1 < 8 and x + 1 < 8 and board[y + 1][x + 1] >= 0:
            board[y + 1][x + 1] = True

        if y + 1 < 8 and board[y + 1][x] >= 0:
            board[y + 1][x] = True

        if y + 1 < 8 and x - 1 >= 0 and board[y + 1][x - 1] >= 0:
            board[y + 1][x - 1] = True

        if y - 1 >= 0 and x + 1 < 8 and board[y - 1][x + 1] >= 0: 
            board[y - 1][x + 1] = True

        if y - 1 >= 0 and board[y - 1 ][x] >= 0:
            board[y - 1 ][x] = True

        if y - 1 >= 0 and x - 1 >= 0 and board[y - 1][x - 1] >= 0:
            board[y - 1][x - 1] = True

        if x + 1 < 8 and  board[y][x + 1] >= 0:
            board[y][x + 1] = True

        if x - 1 >= 0 and board[y][x - 1] >= 0:
            board[y][x - 1] = True

    elif turn == False and board[y][x] > 0:
        if y + 1 < 8 and x + 1 < 8 and board[y + 1][x + 1] <= 0:
            board[y + 1][x + 1] = True

        if y + 1 < 8 and board[y + 1][x] <= 0:
            board[y + 1][x] = True

        if y + 1 < 8 and x - 1 >= 0 and board[y + 1][x - 1] <= 0:
            board[y + 1][x - 1] = True

        if y - 1 >= 0 and x + 1 < 8 and board[y - 1][x + 1] <= 0: 
            board[y - 1][x + 1] = True

        if y - 1 >= 0 and board[y - 1 ][x] <= 0:
            board[y - 1 ][x] = True

        if y - 1 >= 0 and x - 1 >= 0 and board[y - 1][x - 1] <= 0:
            board[y - 1][x - 1] = True

        if x + 1 < 8 and  board[y][x + 1] <= 0:
            board[y][x + 1] = True

        if x - 1 >= 0 and board[y][x - 1] <= 0:
            board[y][x - 1] = True
        
    return board

#The movement of Bishop
def bishop(board ,turn ,y ,x):          
    a ,b = y ,x
    if turn == True and board[y][x] < 0:
        while x > 0 and y > 0 :
            x -= 1
            y -= 1
            if board[y][x] != 0:
                if board[y][x] > 0:
                    board[y][x] = True
                break

            board[y][x] = True

        y ,x = a ,b
        while x > 0 and y < 7 :
            x -= 1
            y += 1
            if board[y][x] != 0:
                if board[y][x] > 0:
                    board[y][x] = True
                break

            board[y][x] = True

        y ,x = a ,b
        while x < 7 and y > 0 :
            x += 1
            y -= 1
            if board[y][x] != 0:
                if board[y][x] > 0:
                    board[y][x] = True
                break

            board[y][x] = True

        y ,x = a ,b
        while x < 7 and y < 7 :
            x += 1
            y += 1
            if board[y][x] != 0:
                if board[y][x] > 0:
                    board[y][x] = True
                break

            board[y][x] = True

    elif turn == False and board[y][x] > 0:
        while x > 0 and y > 0 :
            x -= 1
            y -= 1
            if board[y][x] != 0:
                if board[y][x] < 0:
                    board[y][x] = True
                break

            board[y][x] = True

        y ,x = a ,b
        while x > 0 and y < 7 :
            x -= 1
            y += 1
            if board[y][x] != 0:
                if board[y][x] < 0:
                    board[y][x] = True
                break

            board[y][x] = True

        y ,x = a ,b
        while x < 7 and y > 0 :
            x += 1
            y -= 1
            if board[y][x] != 0:
                if board[y][x] < 0:
                    board[y][x] = True
                break

            board[y][x] = True

        y ,x = a ,b
        while x < 7 and y < 7 :
            x += 1
            y += 1
            if board[y][x] != 0:
                if board[y][x] < 0:
                    board[y][x] = True
                break

            board[y][x] = True

    return board

#The movement of Knight
def knight(board ,turn ,y ,x):           
    if turn == True and board[y][x] < 0:
        if y+1 < 8 and x-2 > -1 and board[y+1][x-2] >= 0:
            board[y+1][x-2] = True

        if y-1 > -1 and x-2 > -1 and board[y-1][x-2] >= 0:
            board[y-1][x-2] = True

        if y+1 < 8 and x+2 < 8 and board[y+1][x+2] >= 0:
            board[y+1][x+2] = True

        if y-1 > -1 and x+2 < 8 and board[y-1][x+2] >= 0:
            board[y-1][x+2] = True

        if y+2 < 8 and x+1 < 8 and  board[y+2][x+1] >= 0:
            board[y+2][x+1] = True

        if y+2 < 8 and x-1 > -1 and board[y+2][x-1] >= 0:
            board[y+2][x-1] = True
            
        if y-2 > -1 and x+1 < 8 and board[y-2][x+1] >= 0:
            board[y-2][x+1] = True
            
        if y-2 > -1 and x-1 > -1 and board[y-2][x-1] >= 0:
            board[y-2][x-1] = True

    elif turn == False and board[y][x] > 0:
        if y+1 < 8 and x-2 > -1 and board[y+1][x-2] <= 0:
            board[y+1][x-2] = True

        if y-1 > -1 and x-2 > -1 and board[y-1][x-2] <= 0:
            board[y-1][x-2] = True

        if y+1 < 8 and x+2 < 8 and board[y+1][x+2] <= 0:
            board[y+1][x+2] = True

        if y-1 > -1 and x+2 < 8 and board[y-1][x+2] <= 0:
            board[y-1][x+2] = True

        if y+2 < 8 and x+1 < 8 and  board[y+2][x+1] <= 0:
            board[y+2][x+1] = True

        if y+2 < 8 and x-1 > -1 and board[y+2][x-1] <= 0:
            board[y+2][x-1] = True
            
        if y-2 > -1 and x+1 < 8 and board[y-2][x+1] <= 0:
            board[y-2][x+1] = True
            
        if y-2 > -1 and x-1 > -1 and board[y-2][x-1] <= 0:
            board[y-2][x-1] = True

    return board

#The movement of Rook
def rook(board ,turn ,y ,x):            
    if turn == True and board[y][x] < 0:
        for i in range(y-1 ,-1 ,-1):
            if board[i][x] != 0:
                if board[i][x] > 0:
                    board[i][x] = True
                break
            board[i][x] = True
            
        for i in range(y+1 ,8 ,1):
            if board[i][x] != 0:
                if board[i][x] > 0:
                    board[i][x] = True
                break
            board[i][x] = True
            
        for i in range(x-1 ,-1, -1):
            if board[y][i] != 0:
                if board[y][i] > 0:
                    board[y][i] = True
                break
            board[y][i] = True
            
        for i in range(x+1 ,8, 1):
            if board[y][i] != 0:
                if board[y][i] > 0:
                    board[y][i] = True
                break
            board[y][i] = True

    elif turn == False and board[y][x] > 0:
        for i in range(y-1 ,-1 ,-1):
            if board[i][x] != 0:
                if board[i][x] < 0:
                    board[i][x] = True
                break
            board[i][x] = True
            
        for i in range(y+1 ,8 ,1):
            if board[i][x] != 0:
                if board[i][x] < 0:
                    board[i][x] = True
                break
            board[i][x] = True
            
        for i in range(x-1 ,-1, -1):
            if board[y][i] != 0:
                if board[y][i] < 0:
                    board[y][i] = True
                break
            board[y][i] = True
            
        for i in range(x+1 ,8, 1):
            if board[y][i] != 0:
                if board[y][i] < 0:
                    board[y][i] = True
                break
            board[y][i] = True
            
    return board

#The movement of Pawn
def pawn(board ,turn ,y ,x):               
    if turn == True and board[y][x] < 0:
        if y == 6 :
            for i in range(1, 3, 1):
                if board[y - i][x] != 0:
                    break
                board[y - i][x] = True
        
        else:
            if board[y - 1][x] == 0:
                board[y - 1][x] = True

        if y - 1 >= 0 and x + 1 < 8 and board[y - 1][x + 1] > 0: 
            board[y - 1][x + 1] = True
        if y - 1 >= 0 and x - 1 >= 0 and board[y - 1][x - 1] > 0:
            board[y - 1][x - 1] = True

    elif turn == False and board[y][x] > 0:
        if y == 1:
            for i in range(1, 3, 1):
                if board[y + i][x] != 0:
                    break
                board[y + i][x] = True
        
        else:
            if board[y + 1][x] == 0:
                board[y + 1][x] = True

        if y + 1 >= 0 and x + 1 < 8 and board[y + 1][x + 1] < 0: 
            board[y + 1][x + 1] = True
        if y + 1 >= 0 and x - 1 >= 0 and board[y + 1][x - 1] < 0:
            board[y + 1][x - 1] = True

    return board

#To distinguish the kind if chess and compute their movement
def ChessMoveRange(board ,turn ,y ,x):      
    a = []
    if abs(ChessBoard[y][x]) == 10:
        a = king(board ,turn ,y ,x)

    if abs(ChessBoard[y][x]) == 6:
        a = bishop(board ,turn ,y ,x)
        rook(board ,turn ,y ,x)

    if abs(ChessBoard[y][x]) == 5:
        a = bishop(board ,turn ,y ,x)


    if abs(ChessBoard[y][x]) == 4:
        a = knight(board ,turn ,y ,x)

    if abs(ChessBoard[y][x]) == 3:
        a = rook(board ,turn ,y ,x)

    elif abs(ChessBoard[y][x]) == 2:
        a = pawn(board ,turn ,y ,x)

    return a

# To judge who is the winner and whether the chess game ended or not.
def WinOrLose():            
    win = None
    green_team = 0
    red_team = 0
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if ChessBoard[i][j] == 10:
                green_team = 1
                break
        if green_team == 1:
            break
    
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if ChessBoard[i][j] == -10:
                red_team = 1
                break
        if red_team == 1:
            break

    if red_team == 0:
        win = "Red win"
    elif green_team == 0:
        win = "Green win"
    else:
        win = None        
    return win

#Main program
pg.init()
pg.display.set_caption("chess")
screen = pg.display.set_mode((422,428))

while True:         
    show()
    #when the "x" is pressed ,close the sreen
    for event in pg.event.get():       
        if event.type == QUIT:
            pg.quit()
        
        #Control the marquee
        if event.type == KEYDOWN:       
            key = pg.key.get_pressed()
            if key[pg.K_UP]:
                if y != 0:
                    y -= 1
            if key[pg.K_DOWN]:
                if y != 7:
                    y += 1
            if key[pg.K_LEFT]:
                if x != 0:
                    x -= 1
            if key[pg.K_RIGHT]:
                if x != 7:
                    x += 1
            
            #The program of the chose process
            if key[pg.K_SPACE]:            
                #Players can't chose the place where there is no chess and competitor's.
                if PressTimes == 1:
                    if (turn == True and ChessBoard[y][x] > 0) or (turn == False and ChessBoard[y][x] < 0) or (ChessBoard[y][x] == 0):      
                        continue
                    else:
                        chose_y ,chose_x = y ,x
                        MoveRangeBoard = copy.deepcopy(ChessBoard)
                        MoveRangeBoard = ChessMoveRange(MoveRangeBoard ,turn ,y ,x)     
                        PressTimes += 1

                #If they chosed again, it should be cancled . 
                elif y == chose_y and x == chose_x: 
                    chose_y ,chose_x = -1, -1
                    PressTimes = 1
                    continue

                #Change the chess chosen if players chosed anthoer.
                elif ChessBoard[chose_y][chose_x] * ChessBoard[y][x] > 0:       
                    chose_y ,chose_x = y ,x
                    MoveRangeBoard = copy.deepcopy(ChessBoard)
                    MoveRangeBoard = ChessMoveRange( MoveRangeBoard ,turn ,y ,x)
                    continue
                
                #Move the chess to the correct place
                elif PressTimes == 2 and  MoveRangeBoard[y][x] == True:     
                    ChessBoard[y][x] = ChessBoard[chose_y][chose_x]
                    ChessBoard[chose_y][chose_x] = 0
                    win = WinOrLose()
                    if win != None:
                        break
                    
                    promotion()
                    show()
                    
                    chose_x ,chose_y = -1 ,-1
                    PressTimes = 1
                    turn = not turn             
    if win != None:
        break

#If the chess game is over, show the font who is winner.
screen.fill((255, 255, 255))    
font = pg.font.SysFont(None ,50)
word = font.render(win,True,(0, 200, 200))
screen.blit(word,(140 ,200))
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()


