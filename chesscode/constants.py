import pygame

#定义与游戏界面相关的常量
SCREEN_WIDTH=900      #屏幕宽度
SCREEN_HEIGHT=650     #屏幕高度
Start_X = 50          #起始位置横坐标
Start_Y = 50          #起始位置纵坐标
Line_Span = 60        #线段间距离

player1Color = 1      #玩家1颜色
player2Color = 2      #玩家2颜色
overColor = 3         #游戏结束颜色

#定义并设置颜色
BG_COLOR=pygame.Color(200, 200, 200)
Line_COLOR=pygame.Color(255, 255, 200)
TEXT_COLOR=pygame.Color(255, 0, 0)
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

repeat = 0

#加载棋子的图片：字典的键是棋子名称，值是相应的图像对象
pieces_images = {
    'b_rook': pygame.image.load("imgs/s2/b_c.gif"),
    'b_elephant': pygame.image.load("imgs/s2/b_x.gif"),
    'b_king': pygame.image.load("imgs/s2/b_j.gif"),
    'b_knigh': pygame.image.load("imgs/s2/b_m.gif"),
    'b_mandarin': pygame.image.load("imgs/s2/b_s.gif"),
    'b_cannon': pygame.image.load("imgs/s2/b_p.gif"),
    'b_pawn': pygame.image.load("imgs/s2/b_z.gif"),

    'r_rook': pygame.image.load("imgs/s2/r_c.gif"),
    'r_elephant': pygame.image.load("imgs/s2/r_x.gif"),
    'r_king': pygame.image.load("imgs/s2/r_j.gif"),
    'r_knigh': pygame.image.load("imgs/s2/r_m.gif"),
    'r_mandarin': pygame.image.load("imgs/s2/r_s.gif"),
    'r_cannon': pygame.image.load("imgs/s2/r_p.gif"),
    'r_pawn': pygame.image.load("imgs/s2/r_z.gif"),
}
