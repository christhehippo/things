import pygame
import os

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)

FPS = 60

IMG_TTT_O    =  pygame.image.load(os.path.join('Assets', 'TicTacToe', 'img_o.png'))
IMG_TTT_X    =  pygame.image.load(os.path.join('Assets', 'TicTacToe', 'img_x.png'))
IMG_TTT_GRID =  pygame.image.load(os.path.join('Assets', 'TicTacToe', 'img_grid.png'))
O    = pygame.transform.scale(IMG_TTT_O, (190, 190))
X    = pygame.transform.scale(IMG_TTT_X, (190, 190))
GRID = pygame.transform.scale(IMG_TTT_GRID, (600, 600))

def draw_window(board):
    WIN.fill(WHITE)
    WIN.blit(GRID, (0, 0))
    
    if board[0] > 0:
        if board[0] == 1:
            WIN.blit(X, (0, 0))
        elif board[0] == 2:
            WIN.blit(O, (0, 0))
    
    if board[1] > 0:
        if board[1] == 1:
            WIN.blit(X, (200, 0))
        elif board[1] == 2:
            WIN.blit(O, (200, 0))

    if board[2] > 0:
        if board[2] == 1:
            WIN.blit(X, (400, 0))
        elif board[2] == 2:
            WIN.blit(O, (400, 0))
        
    if board[3] > 0:
        if board[3] == 1:
            WIN.blit(X, (0, 200))
        elif board[3] == 2:
            WIN.blit(O, (0, 200))
    
    if board[4] > 0:
        if board[4] == 1:
            WIN.blit(X, (200, 200))
        elif board[4] == 2:
            WIN.blit(O, (200, 200))

    if board[5] > 0:
        if board[5] == 1:
            WIN.blit(X, (400, 200))
        elif board[5] == 2:
            WIN.blit(O, (400, 200))

    if board[6] > 0:
        if board[6] == 1:
            WIN.blit(X, (0, 400))
        elif board[6] == 2:
            WIN.blit(O, (0, 400))
             
    if board[7] > 0:
        if board[7] == 1:
            WIN.blit(X, (200, 400))
        elif board[7] == 2:
            WIN.blit(O, (200, 400))
    
    if board[8] > 0:
        if board[8] == 1:
            WIN.blit(X, (400, 400))
        elif board[8] == 2:
            WIN.blit(O, (400, 400))
             
             
    pygame.display.update() 

def main():
    board = [0,0,0,0,0,0,0,0,0]
    sum_old = sum(board)
    sum_new = sum_old
    turn  = 1 # If turn == 1 it is X if turn == 2 it is O
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board)
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                if mouse_pos[0] < 200:
                    if mouse_pos[1] < 200:
                        if board[0] == 0:
                            board[0] = turn
                    elif mouse_pos[1] < 400:
                        if board[3] == 0:
                            board[3] = turn
                    else:
                        if board[6] == 0:
                            board[6] = turn
                elif mouse_pos[0] < 400:
                    if mouse_pos[1] < 200:
                        if board[1] == 0:
                            board[1] = turn
                    elif mouse_pos[1] < 400:
                        if board[4] == 0:
                            board[4] = turn
                    else:
                        if board[7] == 0:
                            board[7] = turn
                else:
                    if mouse_pos[1] < 200:
                        if board[2] == 0:
                            board[2] = turn
                    elif mouse_pos[1] < 400:
                        if board[5] == 0:
                            board[5] = turn
                    else:
                        if board[8] == 0:
                            board[8] = turn        
        
        sum_new = sum(board)
        if sum_new > sum_old:
            if turn == 1:
                turn = 2
            else:
                turn = 1
            sum_old = sum_new
    
        draw_window(board)
    

    pygame.quit()


if __name__ == "__main__":
    main()
