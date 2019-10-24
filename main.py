import pygame
import random
from operator import attrgetter
from algorithms import quickSort, bubbleSort, mergeSort

frames = []

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
    def __init__(self, *args):
        self.data = [DisplayElement(x) for x in args]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, k):
        return self.data[k]

    def __setitem__(self, k, element):
        self.data[k] = DisplayElement(element.value, element.color)
        # self.data[k].value = DisplayElement(element.value, element.color)
        frames.append([DisplayElement(el.value, el.color) for el in self.data])


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

# initialize game engine
pygame.init()
# set screen width/height and caption
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Visual Sorting")
# initialize clock. used later in the loop.
clock = pygame.time.Clock()
red = (255, 0, 0, 255)

x,y,z = 100,100,100

# display = DisplayArray([random.random() for _ in range(20)])
display = DisplayArray(*[random.random() for _ in range(300)])
quickSort(display, 0, len(display) - 1)
i = 0
# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
     
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 

    draw(frames[i], size, screen)

    if i < len(frames) - 1: 
        i += 1
    # write draw code here
    # pygame.draw.circle(screen,(0,0,255),[x,y],20//z)
    
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)
 
# close the window and quit
pygame.quit()


