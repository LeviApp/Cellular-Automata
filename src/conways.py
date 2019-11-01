# import pygame, random
 
# import json
# # Define some colors and other constants

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)


# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (125, 25, 25)
# RANDOM = (15, 25, 144)
# RED = (255,0, 0)
# GREEN = (21,180,0)

# WIN_SIZE = 500

# pygame.init()

# wildfire = []
# wildFireGraph = {}
# shortest_path = []

# class Fire:
#     def __init__(self, ID, place, color, horizontal, vertical, width, height):
#         self.ID = ID
#         self.place = place
#         self.color = color
#         self.horizontal = horizontal
#         self.vertical = vertical
#         self.width = width
#         self.height = height

#     def __str__(self):
#         return f'ID: {self.ID}, status: {self.status}'
        
#     def createFire(self, COLOR):
#         pygame.draw.ellipse(self.place, COLOR, pygame.Rect(self.horizontal,self.vertical,self.width,self.height))


 
# # Set the width and height of the screen [width, height]
# size = (WIN_SIZE, WIN_SIZE)
# screen = pygame.display.set_mode(size)

# # Add a title
# pygame.display.set_caption("Conway's Game of Life")
 
# # Loop until the user clicks the close button.
# done = False
 
# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()
 




# c = 100
# w=0
# x=10
# y=10
# generation = 1

# while y < WIN_SIZE-10:

#     fire = Fire(w, screen, WHITE,x,y,20,20)
#     wildfire.append(fire)



#     x = x + 35

#     w +=1


#     if x >=381:
#         y = y + 35
        
#         if y%2 == 0:
#             x = 10
#         else:
#             x = 27





# status = []

# for i in range(0,len(wildfire)):
#     if i in [0,1,2,3,4,5,6,7,8,9,10]:
#         status.append(1)
#     else:
#         status.append(0)


# def new_generation(s, array):

#     for i in range(0, len(s)):
#         if i == 0:
#             if s[i] == 1:
#                 fires_burning = [s[i+1], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]
#                 if len(fires_burning) == 2:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#         elif i == 10:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) >= 2:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif i == 143:
#             if s[i] == 1:
                
#                 fires_burning = [s[i+1], s[i-10], s[i-11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if fires_burning >= 2:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i+1], s[i-10], s[i-11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif i == 153:

#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i-11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 2:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif i > 0 and i < 10:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i+1], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i+1], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif i > 143 and i < 153:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i+1], s[i-10], s[i-11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i+1], s[i-10], s[i-11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif i%11 == 0 and i%2 != 0:
#             if s[i] == 1:
                
#                 fires_burning = [s[i+1], s[i-10], s[i-11], s[i+11], s[i+12]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i+1], s[i-10], s[i-11], s[i+11], s[i+12]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif i%11 == 0 and i%2 == 0:
#             if s[i] == 1:
                
#                 fires_burning = [s[i+1], s[i-11], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i+1], s[i-11], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif (i+1)%11 == 0 and (i+1)%2 != 0:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i-11], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i-11], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif (i+1)%11 == 0 and (i+1)%2 == 0:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i-12], s[i-11], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i-12], s[i-11], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif (i+1)%11 == 0 and (i+1)%2 == 0:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i-12], s[i-11], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i-12], s[i-11], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         elif array[i].vertical%2 == 0:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i+1], s[i-12], s[i-11], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i+1], s[i-12], s[i-11], s[i+10], s[i+11]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0

#         else:
#             if s[i] == 1:
                
#                 fires_burning = [s[i-1], s[i+1], s[i-11], s[i-10], s[i+11], s[i+12]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) in [2,3]:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#             if s[i] == 0:  
                
#                 fires_burning = [s[i-1], s[i+1], s[i-11], s[i-10], s[i+11], s[i+12]]
#                 fires_burning = [item for item in s if item == 1]

#                 if len(fires_burning) == 3:
#                     s[i] = 1
#                 else:
#                     s[i] = 0
#     print(s)
#     return s



# # -------- Main Program Loop -----------
# while not done:
#     # --- Main event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
 
#     # --- Game logic should go here
    

    
#     # --- Screen-clearing code goes here
 
#     # Here, we clear the screen to gray. Don't put other drawing commands
#     # above this, or they will be erased with this command.
#     screen.fill(BLACK)
 
#     # --- Drawing code should go here

  
    

#     # --- Go ahead and update the screen with what we've drawn.
 
#     # --- Limit to 5 frames per second
#     clock.tick(1)

#     # if generation > 1:
#     #     wildfire = new_generation(wildfire,wildfire2)
#     print(status)
#     status = new_generation(status, wildfire)     
#     print(status)
#     for i in range(0,len(status)):
#         if status[i] == 1:
#             wildfire[i].createFire(RED)
        
#         else:
#             wildfire[i].createFire(GREEN)

#     generation +=1

#     pygame.display.flip()



#     # shortest_path = dfs(0,6)


    
    
#      # Close the window and quit.
# pygame.quit()
#         # {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}



















































































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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 25, 25)
RANDOM = (15, 25, 144)
RED = (255,0, 0)
GREEN = (21,180,0)
YELLOW = (255,255,0)
WIN_W = 1250
WIN_H = 700

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

while y < WIN_H-10:

    fire = Fire(w, screen, WHITE,x,y,20,20)
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

for i in range(0, 651):
    fiery_start.append(random.randint(0,699))

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
circle_total = 699
circle_startend = 665

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

def dft(before, after):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    global lineage_last
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
    screen.fill(BLACK)
 
    # --- Drawing code should go here

  
    

    # --- Go ahead and update the screen with what we've drawn.
 
    # --- Limit to 5 frames per second
    clock.tick(10)




            

    if (generation > 1 and lineage_last == False) or (generation == 1) :
        status = dft(status,status2)
    
    else:
        status = start()
        status2 = status[:]
        generation = 1
        lineage_last = False

    for i in range(0,len(status)):
        if status[i] == 1:
            wildfire[i].createFire(YELLOW)
        else:
            wildfire[i].createFire(BLACK)
    

    status2 = status[:]

    pygame.display.flip()


    generation +=1

   
    if [1,2] == [1, 2]:
        pygame.display.set_caption(f'Generation {generation}')

    else:
        pygame.display.set_caption(f'Generation X')



    
    
     # Close the window and quit.
pygame.quit()



