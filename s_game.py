import pygame

class DisplayArray():
    def __init__(self, *args):
        self.data = list(args)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, k):
        return self.data[k]

    def draw(self, size):
        block_width = size / len(self.data)

 
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
# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 
    # write draw code here
    # pygame.draw.circle(screen,(0,0,255),[x,y],20//z)
    pygame.draw.rect(screen, red, [100,100,200,200])
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)
 
# close the window and quit
pygame.quit()


