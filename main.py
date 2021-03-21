import os
import sys
import time
import random
import numpy as np
from numpy.core.fromnumeric import size

# 解释器版本
# print(sys.version)

# 获取numpy版本
# print(np.__version__)

# 可迭代类型连乘
def multiple(l):
    assert np.iterable(l)
    ans = 1
    for i in l:
        ans = i * ans
    return ans

# 华容道游戏类
class HuarongRoad(object):
    def __init__(self, size=(3,3), chaos=1000):
        assert len(size) == 2
        # 获取棋盘大小
        self.size = size[:2]
        # 获取棋盘长度
        self.length = multiple(self.size)
        # 初始化棋盘
        self.board = np.array(range(self.length))
        self.board = self.board + 1
        self.board[-1] = 0
        self.board.resize(self.size)
        # 设置棋盘恢复目标
        self.aim = self.board.copy()
        # 随机打乱棋盘
        self.random_board(chaos)
    
    def random_board(self, chaos=1000):
        for i in range(chaos):
            self.move(random.choice(['up', 'down', 'left', 'right']))
    
    def locate_zero(self):
        x, y = np.where(self.board == 0)
        return (x[0], y[0])

    def move(self, forword):
        assert forword in ['up', 'down', 'left', 'right']
        # print('In Function Move of HuarongRoad Class! Forword is: ', forword)
        posi = self.locate_zero()
        # 开始矩阵移动
        if forword == 'up':
            line = self.board[:, posi[1]].copy()
            if posi[0]+1 < self.size[0]:
                line[posi[0]+1], line[posi[0]] = line[posi[0]], line[posi[0]+1]
                self.board[:, posi[1]] = line
        elif forword == 'down':
            line = self.board[:, posi[1]].copy()
            if posi[0]-1 >= 0:
                line[posi[0]-1], line[posi[0]] = line[posi[0]], line[posi[0]-1]
                self.board[:, posi[1]] = line
        elif forword == 'left':
            line = self.board[posi[0], :].copy()
            if posi[1]+1 < self.size[1]:
                line[posi[1]+1], line[posi[1]] = line[posi[1]], line[posi[1]+1]
                self.board[posi[0], :] = line
        elif forword == 'right':
            line = self.board[posi[0], :].copy()
            if posi[1]-1 >= 0:
                line[posi[1]-1], line[posi[1]] = line[posi[1]], line[posi[1]-1]
                self.board[posi[0], :] = line
        return True
    
    def show(self):
        print(self.board)
    
    def test(self):
        self.show()
        self.move('down')
        self.show()
    
    def is_win(self):
        return np.equal(self.board, self.aim).all()

    def play(self):
        step = 0
        game.show()
        while(not self.is_win):
            cmd = input('请输入方向(WASD), 并按回车确认: ')
            cmd = cmd.lower()
            if not cmd or not cmd in list('wasd'):
                print('输入有误, 请重新输入!')
                continue
            step += 1
            if cmd == 'w':
                self.move('up')
            elif cmd == 'a':
                self.move('left')
            elif cmd == 's':
                self.move('down')
            elif cmd == 'd':
                self.move('right')
            self.show()
        print('恭喜您, 游戏胜利!')
        print('您一共行走了 %d 步!' % step)
    
    def random_play(self):
        step = 0
        ans = []
        while(not self.is_win()):
            step += 1
            cmd = random.choice(['up', 'down', 'left', 'right'])
            # ans.append(cmd)
            self.move(cmd)
        print('胜利了, 共走了 %d 步骤' % step)
        return True

if __name__ == '__main__':
    print('欢迎游玩华容道游戏\n\n')
    game = HuarongRoad(size=(4,4), chaos=500)
    # game.test()
    # game.play()
    print('开始尝试!')
    start = time.time()
    game.random_play()
    end = time.time()
    print('共尝试了 %s 秒' % str(end - start))
