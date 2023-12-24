# -*- coding: cp1251 -*-

# Задание 1
class Cash:
    def __init__(self, money=0):
        self.money = money

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        result = self.money // 1000
        return result

    def take_away(self, x):
        if self.money < x:
            print("Недостаточно денег")

        else:
            self.money -= x


# Задание 2
class Turtle(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.step = 1

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.step += 1

    def degrade(self):
        if self.step > 0:
            self.step -= 1
        else:
            print("Ошибка")

    def count_moves(self, x2, y2):
        moves = 0
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        if dx % self.step == 0:
            dx1 = dx // self.step
        else:
            dx1 = dx // self.step + 1

        if dy % self.step == 0:
            dy1 = dy // self.step
        else:
            dy1 = dy // self.step + 1
        moves += dx1 + dy1
        return moves


