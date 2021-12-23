import random
from math import inf, sqrt

import pygame
import json

from pygame.constants import RESIZABLE
from GraphAlgo import GraphAlgo


class gui:

    def __init__(self, ag: GraphAlgo):
        self.g = ag
        clock = pygame.time.Clock()
        pygame.init()
        video_infos = pygame.display.Info()
        WIDTH, HIGHT = video_infos.current_w, video_infos.current_h - 50
        self.screen = pygame.display.set_mode((WIDTH, HIGHT), depth=32, flags=RESIZABLE)
        FONT = pygame.font.SysFont('Arial', 18, bold=True)
        """finding the scale(Min,Max) of the graph"""
        min_x = inf
        min_y = inf
        max_x = -inf
        max_y = -inf

        for n in self.g.g.graphDict.values():
            pos = n.pos.split(",")
            """if there is not pos to this id we will cast lots some location between Min<x/y> to Max<x,y> """
            if pos[0]=='':
                if min_x == inf:
                    min_x = 0
                    min_y = 0
                    max_x = 100
                    max_y = 100
                pos =[]
                pos.append(random.uniform(min_x,max_x))
                pos.append(random.uniform(min_y,max_y))
                st =''
                st +=str(pos[0])+","+str(pos[1])+",0.0"
                n.pos = st
                print(n.pos)
                continue
            else:
                if min_x > float(pos[0]):
                    min_x = float(pos[0])
                if max_x < float(pos[0]):
                    max_x = float(pos[0])
                if min_y > float(pos[1]):
                    min_y = float(pos[1])
                if max_y < float(pos[1]):
                    max_y = float(pos[1])

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            self.screen.fill(pygame.Color(10, 140, 200))
            for n in self.g.g.graphDict.values():
                    pos = n.pos.split(",")
                    x = scale(float(pos[0]), 30, self.screen.get_width() - 30, min_x, max_x)
                    y = scale(float(pos[1]), 20, self.screen.get_height() - 20, min_y, max_y)
                    for e in self.g.g.all_out_edges_of_node(n.id):
                        other_pos = self.g.g.graphDict.get(e).pos.split(',')
                        o_x = scale(float(other_pos[0]), 30, self.screen.get_width() - 30, min_x, max_x)
                        o_y = scale(float(other_pos[1]), 20, self.screen.get_height() - 20, min_y, max_y)
                        self.arrow(self,[x, y], [o_x, o_y], 25, 10)
            """draw the arrow of the function and the nodes"""
            for n in self.g.g.graphDict.values():
                pos = n.pos.split(",")
                x = scale(float(pos[0]), 30, self.screen.get_width() - 30, min_x, max_x)
                y = scale(float(pos[1]), 20, self.screen.get_height() - 20, min_y, max_y)
                pygame.draw.circle(self.screen, pygame.Color(7, 0, 0), (x, y), 8)
                id_srf = FONT.render(str(n.id), True, pygame.Color(255, 11, 249))
                rect = id_srf.get_rect(center=(x, y - 5))
                self.screen.blit(id_srf, rect)
            clock.tick(60)
            pygame.display.update()

    def arrow(self, start, end, d, h):
        dx = float(end[0] - start[0])
        dy = float(end[1] - start[1])
        D = float(sqrt(dx * dx + dy * dy))
        xm = float(D - d)
        xn = float(xm)
        ym = float(h)
        yn = -h
        sin = dy / D
        cos = dx / D
        x = xm * cos - ym * sin + start[0]
        ym = xm * sin + ym * cos + start[1]
        xm = x
        x = xn * cos - yn * sin + start[0]
        yn = xn * sin + yn * cos + start[1]
        xn = x
        points = [(end[0] - 3, end[1] - 3), (int(xm) - 3, int(ym) - 3), (int(xn) - 3, int(yn) - 3)]
        pygame.draw.line(self.screen, pygame.Color(240, 240, 240), start, end, width=1)
        pygame.draw.polygon(self.screen, pygame.Color(240, 240, 240), points)


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

