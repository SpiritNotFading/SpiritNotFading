import pygame,random

def var():
    global white, FPS, bgcolor,col,row,block,m_x,m_y,m_pos,mclick_pos,mclick_xpos,mclick_ypos,pressed,humanturn,board,MIN,MAX
    white = (255,255,255)
    FPS = 30
    bgcolor = white
    col = 900
    row = 1200
    block = 30
    m_pos = (1,1)
    mclick_pos = (1,1)
    mclick_xpos = 1
    mclick_ypos = 1
    humanturn = True
    board = [[0 for i in range(0,34)] for j in range(0,44)]
    MIN = -1000
    MAX = 1000
var()

def window():
    pygame.init()
    global WINDOWWIDTH,WINDOWHEIGHT,dis,bg,human,comp
    WINDOWWIDTH = 1230
    WINDOWHEIGHT = 930

    dis = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    bg = pygame.image.load('C:/Users/S.P.1.R.1.T/Desktop/XO_Project/bg1-resized.bmp')
    human = pygame.image.load('C:/Users/S.P.1.R.1.T/Desktop/XO_Project/x.bmp')
    comp = pygame.image.load('C:/Users/S.P.1.R.1.T/Desktop/XO_Project/o.bmp')


def score_pos(x,y):
    global board
    point = 0

#attack----------------------------------------------------------------------------------------------------------------
    if board[x][y] + board[x+1][y] == -1: point += 9 
    if board[x][y] + board[x-1][y] == -1: point += 9
    if board[x][y] + board[x][y+1] == -1: point += 9
    if board[x][y] + board[x][y-1] == -1: point += 9
    if board[x][y] + board[x+1][y+1] == -1: point += 9
    if board[x][y] + board[x-1][y-1] == -1: point += 9
    if board[x][y] + board[x-1][y+1] == -1: point += 9
    if board[x][y] + board[x+1][y-1] == -1: point += 9

    if board[x][y] + board[x+1][y] + board[x+2][y] == -2: point += 54
    if board[x][y] + board[x-1][y] + board[x-2][y] == -2: point += 54
    if board[x][y] + board[x][y+1] + board[x][y+2] == -2: point += 54
    if board[x][y] + board[x][y-1] + board[x][y-2] == -2: point += 30
    if board[x][y] + board[x+1][y+1] + board[x+2][y+2] == -2: point += 30
    if board[x][y] + board[x-1][y-1] + board[x-2][y-2] == -2: point += 30
    if board[x][y] + board[x-1][y+1] + board[x-2][y+2] == -2: point += 30
    if board[x][y] + board[x+1][y-1] + board[x+2][y-2] == -2: point += 30
    
    if board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y] == -3: point += 99
    if board[x][y] + board[x-1][y] + board[x-2][y] + board[x-3][y] == -3: point += 99
    if board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3] == -3: point += 99
    if board[x][y] + board[x][y-1] + board[x][y-2] + board[x][y-3] == -3: point += 99
    if board[x-1][y] + board[x][y] + board[x+1][y] + board[x+2][y] == -3: point += 99
    if board[x+1][y] + board[x][y] + board[x-1][y] + board[x-2][y] == -3: point += 99
    if board[x][y-1] + board[x][y] + board[x][y+1] + board[x][y+2] == -3: point += 99
    if board[x][y+1] + board[x][y] + board[x][y-1] + board[x][y-2] == -3: point += 99
    if board[x][y] + board[x+1][y+1] + board[x+2][y+2] + board[x+3][y+3] == -3: point += 99
    if board[x][y] + board[x-1][y-1] + board[x-2][y-2] + board[x-3][y-3] == -3: point += 99
    if board[x][y] + board[x-1][y+1] + board[x-2][y+2] + board[x-3][y+3] == -3: point += 99
    if board[x][y] + board[x+1][y-1] + board[x+2][y-2] + board[x+3][y-3] == -3: point += 99
    if board[x-1][y-1] + board[x][y] + board[x+1][y+1] + board[x+2][y+2] == -3: point += 99
    if board[x+1][y+1] + board[x][y] + board[x-1][y-1] + board[x-2][y-2] == -3: point += 99
    if board[x-1][y+1] + board[x][y] + board[x-1][y+1] + board[x-2][y+2] == -3: point += 99
    if board[x+1][y-1] + board[x][y] + board[x+1][y-1] + board[x+2][y-2] == -3: point += 99

    if board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y] + board[x+4][y] == -4: point += 1458
    if board[x][y] + board[x-1][y] + board[x-2][y] + board[x-3][y] + board[x-4][y] == -4: point += 1458
    if board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3] + board[x][y+4] == -4: point += 1458
    if board[x][y] + board[x][y-1] + board[x][y-2] + board[x][y-3] + board[x][y-4] == -4: point += 1458
    if board[x][y] + board[x+1][y+1] + board[x+2][y+2] + board[x+3][y+3] + board[x+4][y+4] == -4: point += 1458
    if board[x][y] + board[x-1][y-1] + board[x-2][y-2] + board[x-3][y-3] + board[x-4][y-4] == -4: point += 1458
    if board[x][y] + board[x-1][y+1] + board[x-2][y+2] + board[x-3][y+3] + board[x-4][y+4] == -4: point += 1458
    if board[x][y] + board[x+1][y-1] + board[x+2][y-2] + board[x+3][y-3] + board[x+4][y-4] == -4: point += 1458

##defend-------------------------------------------------------------------------------------------------------------
    
    if board[x][y] + board[x+1][y] == 1: point += 3 
    if board[x][y] + board[x-1][y] == 1: point += 3
    if board[x][y] + board[x][y+1] == 1: point += 3
    if board[x][y] + board[x][y-1] == 1: point += 3
    if board[x][y] + board[x+1][y+1] == 1: point += 3
    if board[x][y] + board[x-1][y-1] == 1: point += 3
    if board[x][y] + board[x-1][y+1] == 1: point += 3
    if board[x][y] + board[x+1][y-1] == 1: point += 3


    if board[x][y] + board[x+1][y] + board[x+2][y] == 2: point += 4
    if board[x][y] + board[x-1][y] + board[x-2][y] == 2: point += 4
    if board[x][y] + board[x][y+1] + board[x][y+2] == 2: point += 4
    if board[x][y] + board[x][y-1] + board[x][y-2] == 2: point += 4
    if board[x][y] + board[x+1][y+1] + board[x+2][y+2] == 2: point += 4
    if board[x][y] + board[x-1][y-1] + board[x-2][y-2] == 2: point += 4
    if board[x][y] + board[x-1][y+1] + board[x-2][y+2] == 2: point += 4
    if board[x][y] + board[x+1][y-1] + board[x+2][y-2] == 2: point += 4

    if board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y] == 3: point += 162
    if board[x][y] + board[x-1][y] + board[x-2][y] + board[x-3][y] == 3: point += 162
    if board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3] == 3: point += 162
    if board[x][y] + board[x][y-1] + board[x][y-2] + board[x][y-3] == 3: point += 162
    if board[x-1][y] + board[x][y] + board[x+1][y] + board[x+2][y] == 3: point += 162
    if board[x+1][y] + board[x][y] + board[x-1][y] + board[x-2][y] == 3: point += 162
    if board[x][y-1] + board[x][y] + board[x][y+1] + board[x][y+2] == 3: point += 162
    if board[x][y+1] + board[x][y] + board[x][y-1] + board[x][y-2] == 3: point += 162
    if board[x][y] + board[x+1][y+1] + board[x+2][y+2] + board[x+3][y+3] == 3: point += 162
    if board[x][y] + board[x-1][y-1] + board[x-2][y-2] + board[x-3][y-3] == 3: point += 162
    if board[x][y] + board[x-1][y+1] + board[x-2][y+2] + board[x-3][y+3] == 3: point += 162
    if board[x][y] + board[x+1][y-1] + board[x+2][y-2] + board[x+3][y-3] == 3: point += 162
    if board[x-1][y-1] + board[x][y] + board[x+1][y+1] + board[x+2][y+2] == 3: point += 162
    if board[x+1][y+1] + board[x][y] + board[x-1][y-1] + board[x-2][y-2] == 3: point += 162
    if board[x-1][y+1] + board[x][y] + board[x-1][y+1] + board[x-2][y+2] == 3: point += 162
    if board[x+1][y-1] + board[x][y] + board[x+1][y-1] + board[x+2][y-2] == 3: point += 162

    if board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y] + board[x+4][y] == 4: point += 729
    if board[x][y] + board[x-1][y] + board[x-2][y] + board[x-3][y] + board[x-4][y] == 4: point += 729
    if board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3] + board[x][y+4] == 4: point += 729
    if board[x][y] + board[x][y-1] + board[x][y-2] + board[x][y-3] + board[x][y-4] == 4: point + 729
    if board[x][y] + board[x+1][y+1] + board[x+2][y+2] + board[x+3][y+3] + board[x+4][y+4] == 4: point += 729
    if board[x][y] + board[x-1][y-1] + board[x-2][y-2] + board[x-3][y-3] + board[x-4][y-4] == 4: point += 729
    if board[x][y] + board[x-1][y+1] + board[x-2][y+2] + board[x-3][y+3] + board[x-4][y+4] == 4: point += 729
    if board[x][y] + board[x+1][y-1] + board[x+2][y-2] + board[x+3][y-3] + board[x+4][y-4] == 4: point += 729
#---------------
    return point
    
def machine():
    point = 0
    max_point = 0
    comp_x = 0
    comp_y = 0
    for x in range(1,40):
        for y in range(1,30):
            point = score_pos(x,y)
            if point > max_point and board[x][y] == 0:
                max_point = point
                comp_x = x
                comp_y = y
    board[comp_x][comp_y] = -1

def draw_mouse_and_XO(m_x,m_y,pressed,mclick_xpos,mclick_ypos):
    global humanturn
    for i in range(block,row,block):
        for j in range(block,col,block):
            i_div_block = i//block
            j_div_block = j//block
            if (i < m_x < (i+block)) and (j < m_y < (j+block)): 
                pygame.draw.rect(dis,white,[i,j,block,block])
            
            if board[i_div_block][j_div_block] == -1 : bg.blit(comp,(i,j))
            if board[i_div_block][j_div_block] == 1 : bg.blit(human,(i,j))

            if pressed == True and humanturn == True:
                if (i < mclick_xpos < (i+block)) and (j < mclick_ypos < (j+block)) and board[i_div_block][j_div_block] == 0:
                    board[i_div_block][j_div_block] = 1
                    humanturn = False
                    

            checkwin(i_div_block,j_div_block)
    if humanturn == False : 
        machine()
        humanturn = True

def checkwin(i,j): 
    global winner
    if board[i][j] + board[i-1][j] +   board[i-2][j] +   board[i-3][j] +   board[i-4][j]   == 5: winner = 'human'
    if board[i][j] + board[i][j-1] +   board[i][j-2] +   board[i][j-3] +   board[i][j-4]   == 5: winner = 'human'
    if board[i][j] + board[i-1][j-1] + board[i-2][j-2] + board[i-3][j-3] + board[i-4][j-4] == 5: winner = 'human'
    if board[i][j] + board[i+1][j-1] + board[i+2][j-2] + board[i+2][j-3] + board[i+3][j-3] + board[i+4][j-4] == 5: winner = 'human'

    if board[i][j] + board[i-1][j] +   board[i-2][j] +   board[i-3][j] +   board[i-4][j]   == -5: winner = 'computer'
    if board[i][j] + board[i][j-1] +   board[i][j-2] +   board[i][j-3] +   board[i][j-4]   == -5: winner = 'computer'
    if board[i][j] + board[i-1][j-1] + board[i-2][j-2] + board[i-3][j-3] + board[i-4][j-4] == -5: winner = 'computer'
    if board[i][j] + board[i+1][j-1] + board[i+2][j-2] + board[i+3][j-3] + board[i+4][j-4] == -5: winner = 'computer' 

def map():
    dis.blit(bg,(0,0))
    pygame.draw.line(dis,white,(block,block),(row,block))
    pygame.draw.line(dis,white,(block,block),(block,col))
    pygame.draw.line(dis,white,(row,block),(row,col))
    pygame.draw.line(dis,white,(block,col),(row,col))
    for i in range(block,row): 
        if i % block == 0 : pygame.draw.line(dis,white,(i,block),(i,col))
    for i in range(block,col): 
        if i % block == 0 : pygame.draw.line(dis,white,(block,i),(row,i))

def gameloop():
    global mclick_xpos,mclick_ypos,run,winner
    fpsClock = pygame.time.Clock()
    run = True
    pressed = False
    winner = ''
    while run:
        if winner != '' : 
            print('winner is :',winner)
            
        pressed = False
        map()
        for event in pygame.event.get():
            m_pos = pygame.mouse.get_pos()
            m_x = m_pos[0]
            m_y = m_pos[1]
            if pygame.mouse.get_pressed()[0] == 1: 
                mclick_pos = m_pos
                mclick_xpos = mclick_pos[0]
                mclick_ypos = mclick_pos[1]
                pressed = True
            if event.type == pygame.QUIT:
                run = False
            
           
        draw_mouse_and_XO(m_x,m_y,pressed,mclick_xpos,mclick_ypos)
        
        pygame.display.update()
        fpsClock.tick(FPS)
    
window()
gameloop()