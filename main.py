import random
from copy import copy
from operator import attrgetter

import pygame

from algorithms import quickSort, bubbleSort, mergeSort

# Bugs:
# Jittery display when moving the tallest bar
# [Fixed] 0th frame is actually one frame into the animation

def random_swap(data):
    rand1 = random.randint(0, len(data)-1)
    rand2 = random.randint(0, len(data)-1)

    display[rand1], display[rand2] = display[rand2], display[rand1]

def random_color():
    return [random.randint(30, 255) for _ in range(3)] + [255]


class DisplayElement():
    def __init__(self, value, color = None):
        self.value = value
        if color == None:
            self.color = random_color()
        else:
            self.color = color
    
    def __lt__(self, other):
        return self.value < other.value


class DisplayArray():
    def __init__(self, size, data):
        self.base = [DisplayElement(x) for x in data]
        self.current = [copy(el) for el in self.base]
        self.deltas = []
        self.frame = 0

    def __len__(self):
        return len(self.current)

    def __getitem__(self, k):
        return self.current[k]

    def __setitem__(self, k, element):
        self.current[k] = DisplayElement(element.value, element.color)
        self.deltas.append((k, copy(element)))
        self.frame += 1

    def rewind(self):
        self.frame = 0
        self.current = [copy(el) for el in self.base]

    def advance(self):
        index, change = self.deltas[self.frame]
        self.current[index] = change
        self.frame += 1

def draw(data, size, screen):
    max_width, max_height = size
    block_width = max_width / len(data)
    block_scale = max_height / max(data).value

    for index, element in enumerate(data):
        block_height = block_scale * element.value
        horizontal_offset = index * block_width
        top_left = [horizontal_offset, max_height - block_height]
        block_size = [block_width, block_height]

        pygame.draw.rect(screen, element.color, top_left + block_size)

pygame.init()

size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Visual Sorting")
clock = pygame.time.Clock()

display = DisplayArray(size, [random.random() for _ in range(10000)])
quickSort(display, 0, len(display) - 1)
display.rewind()

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            display.rewind()
     
    screen.fill((255, 255, 255)) 

    draw(display.current, size, screen)
    display.advance()

    pygame.display.update()

    clock.tick(20)
 
pygame.quit()
