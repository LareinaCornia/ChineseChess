# -*- coding: utf-8 -*-
import pygame
import time
import constants
from button import Button
import pieces
import computer
import my_game as mg

class MainGame():
    window = None
    Start_X = constants.Start_X
    Start_Y = constants.Start_Y
    Line_Span = constants.Line_Span
    Max_X = Start_X + 8 * Line_Span
    Max_Y = Start_Y + 9 * Line_Span
    from_x = 0
    from_y = 0
    to_x = 0
    to_y = 0
    clickx=-1
    clicky=-1

    mgInit = mg.my_game()
    player1Color = constants.player1Color
    player2Color = constants.player2Color
    Putdownflag = player1Color
    piecesSelected = None

    button_go = None
    piecesList = []

    def start_game(self):
        MainGame.window = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
        pygame.display.set_caption("test")
        MainGame.button_go = Button(MainGame.window, "重新开始", constants.SCREEN_WIDTH - 100, 300)  # 创建开始按钮
        self.piecesInit()

        while True:
            time.sleep(0.1)
            # 获取事件
            MainGame.window.fill(constants.BG_COLOR)
            self.drawChessboard()
            #MainGame.button_go.draw_button()
            self.piecesDisplay()
            self.VictoryOrDefeat()
            self.Computerplay()
            self.getEvent()
            pygame.display.update()
            pygame.display.flip()

    def drawChessboard(self):
        mid_end_y = MainGame.Start_Y + 4 * MainGame.Line_Span
        min_start_y = MainGame.Start_Y + 5 * MainGame.Line_Span
        for i in range(0, 9):
            x = MainGame.Start_X + i * MainGame.Line_Span
            if i==0 or i ==8:
                y = MainGame.Start_Y + i * MainGame.Line_Span
                pygame.draw.line(MainGame.window, constants.BLACK, [x, MainGame.Start_Y], [x, MainGame.Max_Y], 1)
            else:
                pygame.draw.line(MainGame.window, constants.BLACK, [x, MainGame.Start_Y], [x, mid_end_y], 1)
                pygame.draw.line(MainGame.window, constants.BLACK, [x, min_start_y], [x, MainGame.Max_Y], 1)

        for i in range(0, 10):
            x = MainGame.Start_X + i * MainGame.Line_Span
            y = MainGame.Start_Y + i * MainGame.Line_Span
            pygame.draw.line(MainGame.window, constants.BLACK, [MainGame.Start_X, y], [MainGame.Max_X, y], 1)

        speed_dial_start_x =  MainGame.Start_X + 3 * MainGame.Line_Span
        speed_dial_end_x =  MainGame.Start_X + 5 * MainGame.Line_Span
        speed_dial_y1 = MainGame.Start_Y + 0 * MainGame.Line_Span
        speed_dial_y2 = MainGame.Start_Y + 2 * MainGame.Line_Span
        speed_dial_y3 = MainGame.Start_Y + 7 * MainGame.Line_Span
        speed_dial_y4 = MainGame.Start_Y + 9 * MainGame.Line_Span

        pygame.draw.line(MainGame.window, constants.BLACK, [speed_dial_start_x, speed_dial_y1], [speed_dial_end_x, speed_dial_y2], 1)
        pygame.draw.line(MainGame.window, constants.BLACK, [speed_dial_start_x, speed_dial_y2],
                         [speed_dial_end_x, speed_dial_y1], 1)
        pygame.draw.line(MainGame.window, constants.BLACK, [speed_dial_start_x, speed_dial_y3],
                         [speed_dial_end_x, speed_dial_y4], 1)
        pygame.draw.line(MainGame.window, constants.BLACK, [speed_dial_start_x, speed_dial_y4],
                         [speed_dial_end_x, speed_dial_y3], 1)

    def piecesInit(self):
        MainGame.piecesList.append(pieces.Rooks(MainGame.player2Color, 0,0))
        MainGame.piecesList.append(pieces.Rooks(MainGame.player2Color,  8, 0))
        MainGame.piecesList.append(pieces.Elephants(MainGame.player2Color,  2, 0))
        MainGame.piecesList.append(pieces.Elephants(MainGame.player2Color,  6, 0))
        MainGame.piecesList.append(pieces.King(MainGame.player2Color, 4, 0))
        MainGame.piecesList.append(pieces.Knighs(MainGame.player2Color,  1, 0))
        MainGame.piecesList.append(pieces.Knighs(MainGame.player2Color,  7, 0))
        MainGame.piecesList.append(pieces.Cannons(MainGame.player2Color,  1, 2))
        MainGame.piecesList.append(pieces.Cannons(MainGame.player2Color, 7, 2))
        MainGame.piecesList.append(pieces.Mandarins(MainGame.player2Color,  3, 0))
        MainGame.piecesList.append(pieces.Mandarins(MainGame.player2Color, 5, 0))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player2Color, 0, 3))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player2Color, 2, 3))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player2Color, 4, 3))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player2Color, 6, 3))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player2Color, 8, 3))

        MainGame.piecesList.append(pieces.Rooks(MainGame.player1Color,  0, 9))
        MainGame.piecesList.append(pieces.Rooks(MainGame.player1Color,  8, 9))
        MainGame.piecesList.append(pieces.Elephants(MainGame.player1Color, 2, 9))
        MainGame.piecesList.append(pieces.Elephants(MainGame.player1Color, 6, 9))
        MainGame.piecesList.append(pieces.King(MainGame.player1Color,  4, 9))
        MainGame.piecesList.append(pieces.Knighs(MainGame.player1Color, 1, 9))
        MainGame.piecesList.append(pieces.Knighs(MainGame.player1Color, 7, 9))
        MainGame.piecesList.append(pieces.Cannons(MainGame.player1Color,  1, 7))
        MainGame.piecesList.append(pieces.Cannons(MainGame.player1Color,  7, 7))
        MainGame.piecesList.append(pieces.Mandarins(MainGame.player1Color,  3, 9))
        MainGame.piecesList.append(pieces.Mandarins(MainGame.player1Color,  5, 9))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player1Color, 0, 6))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player1Color, 2, 6))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player1Color, 4, 6))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player1Color, 6, 6))
        MainGame.piecesList.append(pieces.Pawns(MainGame.player1Color, 8, 6))

    def piecesDisplay(self):
        for item in MainGame.piecesList:
            item.displaypieces(MainGame.window)
            #MainGame.window.blit(item.image, item.rect)

    def getEvent(self):
        # 获取所有的事件
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                if (
                        mouse_x > MainGame.Start_X - MainGame.Line_Span / 2 and mouse_x < MainGame.Max_X + MainGame.Line_Span / 2) and (
                        mouse_y > MainGame.Start_Y - MainGame.Line_Span / 2 and mouse_y < MainGame.Max_Y + MainGame.Line_Span / 2):
                    # print( str(mouse_x) + "" + str(mouse_y))
                    # print(str(MainGame.Putdownflag))
                    if MainGame.Putdownflag != MainGame.player1Color:
                        return

                    click_x = round((mouse_x - MainGame.Start_X) / MainGame.Line_Span)
                    click_y = round((mouse_y - MainGame.Start_Y) / MainGame.Line_Span)
                    click_mod_x = (mouse_x - MainGame.Start_X) % MainGame.Line_Span
                    click_mod_y = (mouse_y - MainGame.Start_Y) % MainGame.Line_Span
                    if abs(click_mod_x - MainGame.Line_Span / 2) >= 5 and abs(
                            click_mod_y - MainGame.Line_Span / 2) >= 5:
                        # print("有效点：x="+str(click_x)+" y="+str(click_y))
                        # 有效点击点
                        self.from_x = MainGame.clickx
                        self.from_y = MainGame.clicky
                        self.to_x = click_x
                        self.to_y = click_y
                        print(self.from_x)
                        print(self.from_y)
                        MainGame.clickx=click_x
                        MainGame.clicky=click_y
                        self.PutdownPieces(MainGame.player1Color, click_x, click_y)

                else:
                    print("out")
                if MainGame.button_go.is_click():
                    #self.restart()
                    print("button_go click")
                else:
                    print("button_go click out")

    def PutdownPieces(self, t, x, y):
        selectfilter=list(filter(lambda cm: cm.x == x and cm.y == y and cm.player == MainGame.player1Color,MainGame.piecesList))
        if len(selectfilter):
            MainGame.piecesSelected = selectfilter[0]
            return

        if MainGame.piecesSelected :
            #print("1111")

            arr = pieces.listPiecestoArr(MainGame.piecesList)
            if MainGame.piecesSelected.canmove(arr, x, y):
                self.PiecesMove(MainGame.piecesSelected, x, y)
                MainGame.Putdownflag = MainGame.player2Color
        else:
            fi = filter(lambda p: p.x == x and p.y == y, MainGame.piecesList)
            listfi = list(fi)
            if len(listfi) != 0:
                MainGame.piecesSelected = listfi[0]

    def PiecesMove(self,pieces,  x , y):
        for item in  MainGame.piecesList:
            if item.x ==x and item.y == y:
                MainGame.piecesList.remove(item)
        pieces.x = x
        pieces.y = y
        print("move to " +str(x) +" "+str(y))
        return True

    def Computerplay(self):

        if MainGame.Putdownflag == MainGame.player2Color:
            print("轮到电脑了")

            computermove = computer.getPlayInfo(MainGame.piecesList, self.from_x, self.from_y, self.to_x, self.to_y, self.mgInit)
            if computer==None:
                return
            piecemove = None
            for item in MainGame.piecesList:
                if item.x == computermove[0] and item.y == computermove[1]:
                    piecemove= item

            self.PiecesMove(piecemove, computermove[2], computermove[3])
            MainGame.Putdownflag = MainGame.player1Color

    #判断游戏胜利
    def VictoryOrDefeat(self):
        txt =""
        result = [MainGame.player1Color,MainGame.player2Color]
        for item in MainGame.piecesList:
            if type(item) ==pieces.King:
                if item.player == MainGame.player1Color:
                    result.remove(MainGame.player1Color)
                if item.player == MainGame.player2Color:
                    result.remove(MainGame.player2Color)

        if len(result)==0:
            return
        if result[0] == MainGame.player1Color :
            txt = "失败！"
        else:
            txt = "胜利！"
        MainGame.window.blit(self.getTextSuface("%s" % txt), (constants.SCREEN_WIDTH - 100, 200))
        MainGame.Putdownflag = constants.overColor

    def getTextSuface(self, text):
        pygame.font.init()
        # print(pygame.font.get_fonts())
        font = pygame.font.SysFont('kaiti', 18)
        txt = font.render(text, True, constants.TEXT_COLOR)
        return txt

    def endGame(self):
        print("exit")
        exit()

if __name__ == '__main__':
    MainGame().start_game()
