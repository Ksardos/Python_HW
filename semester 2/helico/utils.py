from random import randint as rand
import os


def randbool(r, mxr):
    t = rand(0, mxr)
    return t <= r


def randcell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return (tw, th)


# 0 - наверх, 1 - направо, 2 - вниз, 3 - налево
def randcell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)


def game_over(score):
    os.system("CLS")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("                                  ")
    print("GAME OVER, YOU SCORE IS", score)
    print("                                  ")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    exit(0)
