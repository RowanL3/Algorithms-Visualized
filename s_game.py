import pygame
import random

def random_color():
    return [random.randint(30, 255) for _ in range(3)] + [255]

class DisplayArray():
    def __init__(self, *args):
        self.data = list(args)
        self.colors = [random_color() for _ in range(len(self.data))]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, k):
        return self.data[k]

    def draw(self, size, screen):
        max_width, max_height = size
        block_width = max_width / len(self.data)
        block_scale = max_height / max(self.data)

        for index,value in enumerate(self.data):
            horizontal_offset = index * block_width
            top_left = [horizontal_offset, max_height - block_scale * value]
            bottom_right = [horizontal_offset + block_width, max_height]
            pygame.draw.rect(screen, self.colors[index], top_left + bottom_right)
            

 
# initialize game engine
pygame.init()
# set screen width/height and caption
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()
red = (255, 0, 0, 255)

x,y,z = 100,100,100

display = DisplayArray(1,2,3,4,5)
# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 
    display.draw(size, screen)
    # write draw code here
    # pygame.draw.circle(screen,(0,0,255),[x,y],20//z)
    
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)
 
# close the window and quit
pygame.quit()


