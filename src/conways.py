
import pygame, random, json
 
# Define some colors and other constants

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

INACTIVE = (0, 0, 0)
BACKGROUND = (0, 0, 0)
GRAY = (125, 25, 25)
RANDOM = (15, 25, 144)
RED = (255,0, 0)
GREEN = (21,180,0)
ACTIVE = (255,255,0)
WIN_W = 1250
WIN_H = 700
colorChoice = 0

[(0, 0, 0), (0, 0, 0), (255,255,0)]

class COLOR:
    def __init__(self, BACKGROUND, INACTIVE, ACTIVE, BBACKGROUND, BSTROKE, TEXT):
        self.BACKGROUND = BACKGROUND
        self.INACTIVE = INACTIVE
        self.ACTIVE = ACTIVE
        self.BBACKGROUND = BBACKGROUND
        self.BSTROKE = BSTROKE
        self.TEXT = TEXT


# defaultCS = COLOR((0, 0, 0), (0, 0, 0), (255,255,0), (0, 0, 0), (255,255,0), (255,255,0))
# goldCS = COLOR((255, 255, 255), (255, 255, 255), (255,215,0), (255, 255, 255), (255,215,0), (255,215,0))
# USACS = COLOR((60, 59, 110), (255, 255, 255), (178, 34, 52), (255,255,255), (60, 59, 110), (60, 59, 110) )
# GermanyCS = COLOR((255, 206, 0), (0, 0, 0), (221, 0, 0), (0,0,0), (255, 206, 0), (255, 206, 0) )
# greenCS = COLOR((0, 0, 0), (0, 0, 0), (57,255,21), (0, 0, 0), (57,255,21), (57,255,21))
# redCS = COLOR((0, 0, 0), (0, 0, 0), (255,0,0), (0, 0, 0), (255,0,0), (255,0,0))
# oceanCS = COLOR((0, 0, 0), (0,0,255), (0,255,255), (0, 0, 0), (0,255,255), (0,255,255))
bwCS = COLOR((127,127,127), (0,0,0), (255,255,255), (255, 255, 255), (0, 0, 0), (0, 0, 0))
# wbCS = COLOR((127,127,127), (255,255,255), (0,0,0), (255, 255, 255), (0, 0, 0), (0, 0, 0))
bbCS = COLOR((0,0,0), (0,0,0), (255,255,255), (0,0,0), (0,0,0), (255,255,255))
wwCS = COLOR((255,255,255), (255,255,255), (0,0,0), (255,255,255), (255,255,255), (0,0,0))
forestCS = COLOR((255,255,255), (255,255,255), (0,128,0), (0,128,0), (255, 255, 255), (255, 255, 255) )
trafficCS = COLOR((250,210,1), (251,18,47), (51,165,50), (250,210,1), (250,210,1), (0, 0, 0))
burnCS = COLOR((0,0,0), (51,165,50), (251,18,47), (0, 0, 0), (251,18,47), (251,18,47) )
warmCS = COLOR((255,165,0), (251,18,47), (255,255,0), (255,255,0), (255,165,0), (0,0,0))
plumCS = COLOR((76,0,153), (153,51,255), (229,204,255), (76,0,153), (229,204,255), (229,204,255))
strawberryCS = COLOR((255,204,229), (255,51,153), (153,0,76), (255,204,229), (153,0,76), (153,0,76))
hotCS = COLOR((0,0,0), (0,0,0), (255,0,127), (0,0,0), (255,0,127), (255,0,127))
broncoCS = COLOR((0,34,68), (251,79,20), (0,34,68), (0,0,0), (251,79,20), (251,79,20) )
woodCS = COLOR((210,180,140), (150,75,0), (210,180,140), (255,255,255), (150,75,0), (150,75,0))


(0,128,0)

pygame.init()

wildfire = []
wildFireGraph = {}

mylist = []

for i in range(0,125):
    x = random.randint(1,153)
    mylist.append(x)

mylist = list(set(mylist))

class Fire:
    def __init__(self, ID, place, color, horizontal, vertical, width, height):
        self.ID = ID
        self.place = place
        self.color = color
        self.horizontal = horizontal
        self.vertical = vertical
        self.width = width
        self.height = height

    def __str__(self):
        return f'ID: {self.ID}, status: {self.status}'
        
    def createFire(self, COLOR):
        pygame.draw.ellipse(self.place, COLOR, pygame.Rect(self.horizontal,self.vertical,self.width,self.height))


 
# Set the width and height of the screen [width, height]
size = (WIN_W, WIN_H)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 




c = 10
w=0
x=10
y=10
generation = 1
last_generation = 1

while y < WIN_H-60:

    fire = Fire(w, screen, woodCS.BACKGROUND,x,y,20,20)
    wildfire.append(fire)


    x = x + 35

    w +=1


    if x >=1220:
        y = y + 35
        
        if y%2 == 0:
            x = 10
        else:
            x = 27

fiery_start = []

for i in range(0, 301):
    fiery_start.append(random.randint(0,629))

fiery_start = list(set(fiery_start))



def start():
    status = []
    for i in range(0,len(wildfire)):
        if i in fiery_start:
            status.append(1)
        else:
            status.append(0)
    return status

status = start()
status2 = status[:]
lineage = [status]
lineage_last = False
row_count = 35
row_minus = 34
row_plus = 36
circle_total = 629
circle_startend = 595

for item in wildfire:

    if item.ID == 0:
        wildFireGraph[item.ID] = {item.ID+1, item.ID+row_count}
    elif item.ID == row_minus:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+row_minus, item.ID+row_count}
    elif item.ID == circle_startend:
        wildFireGraph[item.ID] = {item.ID+1, item.ID-row_minus, item.ID-row_count}
    elif item.ID == circle_total:
        wildFireGraph[item.ID] = {item.ID-1, item.ID-row_count}
    elif item.ID > 0 and item.ID < row_minus:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID+row_minus, item.ID+row_count}
    elif item.ID > circle_startend and item.ID < circle_total:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-row_minus, item.ID-row_count}
    elif item.ID%row_count == 0 and item.ID%2 != 0:
        wildFireGraph[item.ID] = {item.ID+1, item.ID-row_minus, item.ID-row_count, item.ID+row_count, item.ID+row_plus}
    elif item.ID%row_count == 0 and item.ID%2 == 0:
        wildFireGraph[item.ID] = {item.ID+1, item.ID-row_count, item.ID+row_count} 
    elif (item.ID+1)%row_count == 0 and (item.ID+1)%2 != 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID-row_plus, item.ID-row_count, item.ID+row_minus, item.ID+row_count} 
    elif (item.ID+1)%row_count == 0 and (item.ID+1)%2 == 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID-row_count, item.ID+row_count}
    elif item.vertical%2 == 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-row_plus, item.ID-row_count, item.ID+row_minus, item.ID+row_count}
    else:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-row_count, item.ID-row_minus, item.ID+row_count, item.ID+row_plus}

def dft(before, after, p):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    global status
    global lineage_last

    if p == False:
        depth = Stack()
        visited = []
        fires_burning = 0
        depth.push(0)
        while depth.size():
            node = depth.pop()
            visited.append(node)


            for neighbor in wildFireGraph[node]:
                if neighbor not in visited and neighbor not in depth.stack:
                    depth.push(neighbor)

            for neighbor in wildFireGraph[node]:
                if before[neighbor] == 1:
                    fires_burning+=1

            if before[node] == 1:
                if fires_burning in [2,3]:
                    after[node] = 1
                else:
                    after[node] = 0
            else:
                if fires_burning == 3:
                    after[node] = 1
                else:
                    after[node] = 0
            fires_burning = 0         

        lineage.append(after)
        if status == status2 and generation != 1:
            lineage_last = True

        return after
    else:
        status = lineage[-1]


s = 5
looping = False
paused = False
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    

    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(woodCS.BACKGROUND)
 
    # --- Drawing code should go here




    # --- Go ahead and update the screen with what we've drawn.
 
    # --- Limit to 5 frames per second

    def speed_up():
        global s
        if s < 20 and s >=1:
            s+=1
        elif s < 1:
            s = round(s + 0.1, 1)

        else:
            s = 20
    

    def slow_down():
        global s
        if s >= 2:
            s-=1
        
        elif s >= 0.3 and s <= 1:
            s = round(s - 0.1, 1)
        
        else:
            s = 0.2


    def restart():
        global status, status2, generation, lineage_last, paused
        paused = False
        status = start()
        status2 = status[:]
        generation = 1
        lineage_last = False
    

    def pauser():
        global paused
        if paused == True:
            paused = False
        
        else:
            paused = True

    def loop():
        global looping
        if looping == True:
            looping = False
        
        else:
            looping = True

    def rand():
        global fiery_start
        fiery_start = []
        for i in range(0, 301):
            fiery_start.append(random.randint(0,629))    
        fiery_start = list(set(fiery_start))
        restart()
    def button_func(x1,y1,w1,h1,x2,y2,w2,h2,x3,y3,txt, action=None, l=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x1 + w1 > mouse[0] > x1 and y1 + h1 > mouse[1] > y1 or l == True:
            pygame.draw.rect(screen, woodCS.BBACKGROUND, pygame.Rect(x1,y1,w1,h1))
            pygame.draw.rect(screen, woodCS.TEXT, pygame.Rect(x2,y2,w2,h2))
            font = pygame.font.SysFont("Arial", 25)
            text = font.render(txt, 1, woodCS.BBACKGROUND)
            screen.blit(text, (x3,y3))
            if click[0] == 1 and action != None:
                action()
                

        else:
            pygame.draw.rect(screen, woodCS.BSTROKE, pygame.Rect(x1,y1,w1,h1))
            pygame.draw.rect(screen, woodCS.BBACKGROUND, pygame.Rect(x2,y2,w2,h2))
            font = pygame.font.SysFont("Arial", 25)
            text = font.render(txt, 1, woodCS.TEXT)
            screen.blit(text, (x3,y3))
    
    button_func(22,647,126,46,25,650,120,40,35,655, 'Restart', restart)
    button_func(145,647,126,46,148,650,120,40,155,655, 'Rewind')
    button_func(268,647,126,46,271,650,120,40,275,655, 'Loop', loop, looping)
    if paused == False:
        button_func(391,647,126,46,394,650,120,40,395,655, 'Pause', pauser)
    
    else:
        button_func(391,647,126,46,394,650,120,40,395,655, 'Play', pauser)
 
    button_func(514,647,126,46,517,650,120,40,524,655, 'Random', rand)
    button_func(637,647,126,46,640,650,120,40,644,655, 'Color')
    button_func(760,647,65,46,763,650,60,40,940,655, '-', slow_down)


    pygame.draw.rect(screen, woodCS.BSTROKE, pygame.Rect(822,647,106,46))
    pygame.draw.rect(screen, woodCS.BBACKGROUND, pygame.Rect(825,650,100,40))
    font = pygame.font.SysFont("Arial", 25)
    text = font.render('Speed', 1, woodCS.TEXT)
    screen.blit(text, (840,655))

    button_func(922,647,51,46,925,650,45,40,940,655, '-', slow_down)
    button_func(972,647,51,46,975,650,45,40,990,655, '+', speed_up)

    pygame.draw.rect(screen, woodCS.BSTROKE, pygame.Rect(1022,647,206,46))
    pygame.draw.rect(screen, woodCS.BBACKGROUND, pygame.Rect(1025,650,200,40))
    font = pygame.font.SysFont("Arial", 25)
    text = font.render(f'Generation: {generation}', 1, woodCS.TEXT)
    screen.blit(text, (1050,655))    

    clock.tick(s)




            

    if (generation > 1 and lineage_last == False) or (generation == 1) :
        status = dft(status,status2, paused)
    
    else:
        if looping == True:
            status = start()
            status2 = status[:]
            generation = 1
            lineage_last = False
    

    if paused == False:
        for i in range(0,len(status)):
            if status[i] == 1:
                wildfire[i].createFire(woodCS.ACTIVE)
            else:
                wildfire[i].createFire(woodCS.INACTIVE)
    
    else:
        status = lineage[-1]
        for i in range(0,len(status)):
            if status[i] == 1:
                wildfire[i].createFire(woodCS.ACTIVE)
            else:
                wildfire[i].createFire(woodCS.INACTIVE)

    status2 = status[:]

    pygame.display.flip()

    if lineage_last == False and paused == False:
        generation +=1





    
    
     # Close the window and quit.
pygame.quit()



