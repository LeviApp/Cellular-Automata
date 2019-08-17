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



















































































import pygame, random
 
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

WIN_WIDTH = 440
WIN_HEIGHT = 500


pygame.init()

wildfire = []
wildFireGraph = {}

mylist = []

for i in range(0,75):
    x = random.randint(1,153)
    mylist.append(x)

mylist = list(set(mylist))

class Fire:
    def __init__(self, ID, place, color, horizontal, vertical, width, height, status):
        self.ID = ID
        self.place = place
        self.color = color
        self.horizontal = horizontal
        self.vertical = vertical
        self.width = width
        self.height = height
        self.status = status

    def __str__(self):
        return f'ID: {self.ID}, status: {self.status}'
        
    def createFire(self, COLOR):
        pygame.draw.ellipse(self.place, COLOR, pygame.Rect(self.horizontal,self.vertical,self.width,self.height))


 
# Set the width and height of the screen [width, height]
size = (WIN_WIDTH, WIN_HEIGHT)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 





generation = 1




def start():
    w=0
    x=10
    y=10
    wildfire = []
    while y < WIN_HEIGHT-10:

        if w in [5,6,15,16,17]:
            fire = Fire(w, screen, WHITE,x,y,20,20,1)
            wildfire.append(fire)

        else:
            fire = Fire(w, screen, WHITE,x,y,20,20,0)
            wildfire.append(fire)


        x = x + 35

        w +=1


        if x >=381:
            y = y + 35
            
            if y%2 == 0:
                x = 10
            else:
                x = 27
    
    return wildfire


wildfire = start()
wildfire2 = wildfire[:]

for item in wildfire:

    if item.ID == 0:
        wildFireGraph[item.ID] = {item.ID+1, item.ID+11}
    elif item.ID == 10:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+10, item.ID+11}
    elif item.ID == 143:
        wildFireGraph[item.ID] = {item.ID+1, item.ID-10, item.ID-11}
    elif item.ID == 153:
        wildFireGraph[item.ID] = {item.ID-1, item.ID-11}
    elif item.ID > 0 and item.ID < 10:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID+10, item.ID+11}
    elif item.ID > 143 and item.ID < 153:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-10, item.ID-11}
    elif item.ID%11 == 0 and item.ID%2 != 0:
        wildFireGraph[item.ID] = {item.ID+1, item.ID-10, item.ID-11, item.ID+11, item.ID+12}
    elif item.ID%11 == 0 and item.ID%2 == 0:
        wildFireGraph[item.ID] = {item.ID+1, item.ID-11, item.ID+11} 
    elif (item.ID+1)%11 == 0 and (item.ID+1)%2 != 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID-12, item.ID-11, item.ID+10, item.ID+11} 
    elif (item.ID+1)%11 == 0 and (item.ID+1)%2 == 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID-11, item.ID+11}
    elif item.vertical%2 == 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-12, item.ID-11, item.ID+10, item.ID+11}
    else:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-11, item.ID-10, item.ID+11, item.ID+12}

print(wildFireGraph)
def dft(before, after):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """

    depth = Stack()
    visited = []
    fires_burning = 0
    depth.push(100)

    while depth.size():
        node = depth.pop()
        visited.append(node)


        for neighbor in wildFireGraph[node]:
            if neighbor not in visited and neighbor not in depth.stack:
                depth.push(neighbor)

        for neighbor in wildFireGraph[node]:
            if before[neighbor].status == 1:
                fires_burning+=1

        if before[node].status == 1:
            if fires_burning == [2,3]:
                after[node].status = 1
            else:
                after[node].status = 0
        else:
            if fires_burning == 3:
                after[node].status = 1
            else:
                after[node].status = 0
        fires_burning = 0         


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
    clock.tick(0.1)




            

    if generation > 1:
        # if wildfire == dft(wildfire,wildfire2):
        #     wildfire = start()
        #     generation = 1

        # else:
        wildfire = dft(wildfire,wildfire2)    




    for fire in wildfire:
        if fire.status == 1:
           fire.createFire(RED)
        else:
            fire.createFire(GREEN)
    
    wildfire2 = wildfire[:]

    pygame.display.flip()


    generation +=1

   

    pygame.display.set_caption(f'Generation {generation}')


    
    
     # Close the window and quit.
pygame.quit()















































































































































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
#     def __init__(self, ID, place, color, horizontal, vertical, width, height, status):
#         self.ID = ID
#         self.place = place
#         self.color = color
#         self.horizontal = horizontal
#         self.vertical = vertical
#         self.width = width
#         self.height = height
#         self.status = status

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
# generation = 0

# while y < WIN_SIZE-10:

#     if w in [0,1,2,3,4,5,6,7,8,9,10]:
#         fire = Fire(w, screen, WHITE,x,y,20,20,1)
#         wildfire.append(fire)

#     else:
#         fire = Fire(w, screen, WHITE,x,y,20,20,0)
#         wildfire.append(fire)


#     x = x + 35

#     w +=1


#     if x >=381:
#         y = y + 35
        
#         if y%2 == 0:
#             x = 10
#         else:
#             x = 27








# wildfire2 = wildfire[:]

# for item in wildfire:

#     if item.ID == 0:
#         wildFireGraph[item.ID] = {item.ID+1, item.ID+11}
#     elif item.ID == 10:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID+10, item.ID+11}
#     elif item.ID == 143:
#         wildFireGraph[item.ID] = {item.ID+1, item.ID-10, item.ID-11}
#     elif item.ID == 153:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID-11}
#     elif item.ID > 0 and item.ID < 10:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID+10, item.ID+11}
#     elif item.ID > 143 and item.ID < 153:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-10, item.ID-11}
#     elif item.ID%11 == 0 and item.ID%2 != 0:
#         wildFireGraph[item.ID] = {item.ID+1, item.ID-10, item.ID-11, item.ID+11, item.ID+12}
#     elif item.ID%11 == 0 and item.ID%2 == 0:
#         wildFireGraph[item.ID] = {item.ID+1, item.ID-11, item.ID+11} 
#     elif (item.ID+1)%11 == 0 and (item.ID+1)%2 != 0:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID-11, item.ID+11} 
#     elif (item.ID+1)%11 == 0 and (item.ID+1)%2 == 0:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID-12, item.ID-11, item.ID+10, item.ID+11}
#     elif item.vertical%2 == 0:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-12, item.ID-11, item.ID+10, item.ID+11}
#     else:
#         wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-11, item.ID-10, item.ID+11, item.ID+12}


# index = 1


# def bfs(starting_vertex, destination_vertex):
#     """
#     Return a list containing the shortest path from
#     starting_vertex to destination_vertex in
#     breath-first order.
#     """

#     breadth = Queue()
#     visited = []
#     breadth.enqueue([starting_vertex])
#     while breadth.size():

#         path = breadth.dequeue()
#         node = path[-1]

#         if node not in visited:
#             visited.append(node)
#             if node == destination_vertex:
#                 return path
            
#             for neighbor in wildFireGraph[node]:
#                 copy_path = path[:]
#                 copy_path.append(neighbor)
#                 breadth.enqueue(copy_path)



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
#     clock.tick(5)




            

        




#     for item in wildfire:
#         if item.ID in bfs(0,index):
#             item.createFire(RED)
#         else:
#             item.createFire(GREEN)

#     pygame.display.flip()

#     index +=1

#     if index == 154:
#         index = 1




    
    
#      # Close the window and quit.
# pygame.quit()
