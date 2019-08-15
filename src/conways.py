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
YELLOW = (255,216,0)

WIN_SIZE = 500

pygame.init()

wildfire = []
wildFireGraph = {}
shortest_path = []

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
        
    def createFire(self, COLOR):
        pygame.draw.ellipse(self.place, COLOR, pygame.Rect(self.horizontal,self.vertical,self.width,self.height))


 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 




c = 100
w=0
x=10
y=10
generation = 1

while y < WIN_SIZE-10:

    if w in [100,101,102]:
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






print('before', wildfire[100].status)


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
        wildFireGraph[item.ID] = {item.ID-1, item.ID-11, item.ID+11} 
    elif (item.ID+1)%11 == 0 and (item.ID+1)%2 == 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID-12, item.ID-11, item.ID+10, item.ID+11}
    elif item.vertical%2 == 0:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-12, item.ID-11, item.ID+10, item.ID+11}
    else:
        wildFireGraph[item.ID] = {item.ID-1, item.ID+1, item.ID-11, item.ID-10, item.ID+11, item.ID+12}


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
    clock.tick(1)


 

    def bfs(starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        breadth = Queue()
        visited = []
        breadth.enqueue([starting_vertex])
        while breadth.size():

            path = breadth.dequeue()
            node = path[-1]

            if node not in visited:
                visited.append(node)
                if node == destination_vertex:
                    return path
                
                for neighbor in wildFireGraph[node]:
                    copy_path = path[:]
                    copy_path.append(neighbor)
                    breadth.enqueue(copy_path)

    def dfs(starting_vertex, destination_vertex):
            depth = Stack()
            visited = []
            depth.push([starting_vertex])
            while depth.size():
                path = depth.pop()
                node = path[-1]
                if node not in visited:
                    visited.append(node)
                    if node == destination_vertex:
                        return path

                    for neighbor in wildFireGraph[node]:
                        new_path = path[:]
                        new_path.append(neighbor)
                        depth.push(new_path)


    def dft(starting_vertex):

        depth = Stack()
        visited = []
        depth.push(starting_vertex)
        

        while depth.size():
            node = depth.pop()
            visited.append(node)
            fires_burning = 0

            for vertex in wildFireGraph[node]:
                if vertex not in visited and vertex not in depth.stack:
                    depth.push(vertex)

            for vertex in wildFireGraph[node]:
                if wildfire[vertex].status == 1:
                    fires_burning = fires_burning + 1


            if fires_burning < 2 and wildfire[node].status == 1:
                wildfire2[node].status = 0
                print(f'node {node} has changed to {wildfire2[vertex].status}')

            elif fires_burning in [2,3] and wildfire[node].status == 1:
                wildfire2[node].status = 1
                print(f'node {node} has changed to {wildfire2[vertex].status}')

            elif fires_burning >=4 and wildfire[node].status == 1:
                wildfire2[node].status = 1
                print(f'node {node} has changed to {wildfire2[vertex].status}')

            elif fires_burning == 3 and wildfire[node].status == 0:
                wildfire2[node].status = 1
                print(f'node {node} has changed to {wildfire2[vertex].status}')
        

    if generation > 1:
        dft(0)
        wildfire = wildfire2[:]


    print('after', wildfire[100].status,  wildfire[101].status,  wildfire[102].status)
    for item in wildfire:
        if item.status == 1:
            item.createFire(RED)
        else:
            item.createFire(YELLOW)

    pygame.display.flip()

    generation +=1


    # shortest_path = dfs(0,6)


    
    
     # Close the window and quit.
pygame.quit()
        # {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
