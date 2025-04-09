import pygame

player = pygame.image.load('sprites/player/player.png')

skeleton_forward = pygame.image.load('sprites/enemy/Skeleto_new/skeleton_forward.png')
skeleton_back = pygame.image.load('sprites/enemy/Skeleto_new/skeleton_back.png')
skeleton_left = pygame.image.load('sprites/enemy/Skeleto_new/skeleton_left.png')
skeleton_right = pygame.image.load('sprites/enemy/Skeleto_new/skeleton_right.png')

main_forward = pygame.image.load('sprites/player/new_main_anim/main_anim_forward.png')
main_back = pygame.image.load('sprites/player/new_main_anim/main_anim_back.png')
main_left = pygame.image.load('sprites/player/new_main_anim/main_anim_left.png')
main_right = pygame.image.load('sprites/player/new_main_anim/main_anim_right.png')

wall_1 = pygame.image.load('sprites/map/wall_1.png')
wall_2 = pygame.image.load('sprites/map/wall_2.png')

map_1 = [[wall_1, 290, 280],
         [wall_1, 350, 340],
         [wall_1, 350, 280],
         [wall_1, 350, 220],

         [wall_1, 160, -10],
         [wall_1, 160, 50],
         [wall_1, 160, 110],
         [wall_1, 160, 170],
         [wall_1, 100, 170],

         [wall_1, 160, 560],
         [wall_1, 160, 500],
         [wall_1, 160, 440],
         [wall_1, 160, 380],
         [wall_1, 100, 380],
         
         [wall_1, 650, 280],
         [wall_1, 590, 340],
         [wall_1, 590, 280],
         [wall_1, 590, 220],
         
         [wall_1, 780, -10],
         [wall_1, 780, 50],
         [wall_1, 780, 110],
         [wall_1, 780, 170],
         [wall_1, 840, 170],

         [wall_1, 780, 560],
         [wall_1, 780, 500],
         [wall_1, 780, 440],
         [wall_1, 780, 380],
         [wall_1, 840, 380],]

map_2 = [[wall_2, 470, 80],
         [wall_2, 410, 80],
         [wall_2, 350, 80],
         [wall_2, 530, 80],
         [wall_2, 590, 80],
         [wall_2, 470, 140],

         [wall_2, 70, 80],
         [wall_2, 130, 80],
         [wall_2, 190, 80],
         [wall_2, 70, 130],
         [wall_2, 70, 170],
         [wall_2, 70, 200],

         [wall_2, 750, 80],
         [wall_2, 810, 80],
         [wall_2, 870, 80],
         [wall_2, 870, 130],
         [wall_2, 870, 170],
         [wall_2, 870, 200],
         
         [wall_2, 320, 280],
         [wall_2, 620, 280],
         [wall_2, 320, 340],
         [wall_2, 620, 340],

         [wall_2, 620, 400],
         [wall_2, 680, 400],
         [wall_2, 740, 400],
         [wall_2, 800, 400],
         [wall_2, 860, 400],
         [wall_2, 860, 460],

         [wall_2, 320, 400],
         [wall_2, 260, 400],
         [wall_2, 200, 400],
         [wall_2, 140, 400],
         [wall_2, 80, 400],
         [wall_2, 80, 460],

         [wall_2, 260, 340],
         [wall_2, 680, 340],]

rect_map_1 = [pygame.Rect(cor[1], cor[2], 60, 60) for cor in map_1]
rect_map_2 = [pygame.Rect(cor[1], cor[2], 60, 60) for cor in map_2]
