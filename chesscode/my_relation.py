#此类包含的信息体现了某个棋子和其它棋子之间的关系，用于判断当前棋局中的攻守关系，帮助计算下一步最优的棋步
class relation:
    def __init__(self):
        self.chess_type = 0                 #棋子类型
        self.num_attack = 0                 #攻击该棋子者数量
        self.num_guard = 0                  #保护该棋子者数量
        self.num_attacked = 0               #被该棋子攻击者数量
        self.num_guarded = 0                #被该棋子保护者数量
        self.attack = [0, 0, 0, 0, 0, 0]    #攻击情况
        self.attacked = [0, 0, 0, 0, 0, 0]  #被攻击情况
        self.guard = [0, 0, 0, 0, 0, 0]     #保护情况
        self.guarded = [0, 0, 0, 0, 0, 0]   #被保护情况
