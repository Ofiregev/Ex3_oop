# import json
# import os
# from math import inf
# from types import SimpleNamespace
# import pygame
# from pygame import Color, display, gfxdraw
# from pygame.constants import RESIZABLE
#
# from GraphAlgo import GraphAlgo
#
#
# class Gui:
#     WIDTH, HEIGHT = 1080, 720
#     pygame.init()
#     screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
#     clock = pygame.time.Clock()
#     pygame.font.init()
#
#     FONT = pygame.font.SysFont('Arial', 20, bold=True)
#
#     def __init__(self,graph:GraphAlgo):
#         self.g = graph
#
#     def scale(data, min_screen, max_screen, min_data, max_data):
#         """
#         get the scaled data with proportions min_data, max_data
#         relative to min and max screen dimensions
#         """
#         return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen
#     # max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
#
#     # decorate scale with the correct values
#     def setLimits(self):
#         minX = inf
#         minY = inf
#         maxX = -inf
#         maxY = -inf
#         for i in self.g.g.graphDict.values():
#             minX = min(self.g.g.posGetX(i.pos),minX)
#             minY = min(self.g.g.posGetY(i.pos),minY)
#             maxX = max(self.g.g.posGetX(i.pos),maxX)
#             maxY = max(self.g.g.posGetX(i.pos),maxY)
#
#
#
#     def my_scale(self, x=False, y=False):
#         if x:
#             return scale(data, 50, screen.get_width() - 50, min_x, max_x)
#         if y:
#             return scale(data, 50, screen.get_height()-50, min_y, max_y)
#
#
#     radius = 15
#
#
#     while(True):
#         # check events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit(0)
#
#         # refresh screen
#         screen.fill(Color(0, 0, 0))
#
#         # draw nodes
#         for n in  :
#             x = my_scale(n.pos.x, x=True)
#             y = my_scale(n.pos.y, y=True)
#
#             # its just to get a nice antialiased circle
#             gfxdraw.filled_circle(screen, int(x), int(y),
#                                   radius, Color(64, 80, 174))
#             gfxdraw.aacircle(screen, int(x), int(y),
#                              radius, Color(255, 255, 255))
#
#             # draw the node id
#             id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
#             rect = id_srf.get_rect(center=(x, y))
#             screen.blit(id_srf, rect)
#
#         # draw edges
#         for e in graph.edges:
#             # find the edge nodes
#             src = next(n for n in graph.nodes if n.id == e.src)
#             dest = next(n for n in graph.nodes if n.id == e.dest)
#
#             # scaled positions
#             src_x = my_scale(src.pos.x, x=True)
#             src_y = my_scale(src.pos.y, y=True)
#             dest_x = my_scale(dest.pos.x, x=True)
#             dest_y = my_scale(dest.pos.y, y=True)
#
#             # draw the line
#             pygame.draw.line(screen, Color(61, 72, 126),
#                              (src_x, src_y), (dest_x, dest_y))
#
#         # update screen changes
#         display.update()
#
#         # refresh rate
#         clock.tick(60)