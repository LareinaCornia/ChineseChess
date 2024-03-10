import pygame
class Button():
    #初始化按钮的属性
    def __init__(self, screen, msg, left,top):  #msg为要在按钮中显示的文本
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 150, 50
        self.button_color = (72, 61, 139)
        self.text_color = (255, 255, 255)
        
        pygame.font.init()
        self.font = pygame.font.SysFont('kaiti', 20)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.left = left
        self.top = top
        self.deal_msg(msg)  #渲染图像

    #将要显示在按钮上的文本渲染为图像并将其在按钮上居中
    def deal_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)   #render将存储在msg的文本转换为图像
        self.msg_img_rect = self.msg_img.get_rect()                                      #根据文本图像创建一个rect
        self.msg_img_rect.center = self.rect.center                                      #将该rect的center属性设置为按钮的center属性

    #在屏幕上绘制该按钮，通过blit方法将按钮的图像绘制到屏幕上
    def draw_button(self):
        self.screen.blit(self.msg_img, (self.left,self.top))
    
    #检查鼠标点击是否在按钮的范围内，如果是，则返回True，表示按钮被点击。具体实现是通过判断鼠标点击的位置是否在按钮的范围内，如果是则返回True，否则返回False
    def is_click(self):
        point_x, point_y = pygame.mouse.get_pos()
        x = self.left
        y = self.top
        w, h = self.msg_img.get_size()
        in_x = x < point_x < x + w
        in_y = y < point_y < y + h
        return in_x and in_y

