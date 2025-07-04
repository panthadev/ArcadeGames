import pygame
import random



class Room:

    def __init__(self, xpos, ypos, width, height): # initailze in Map methods

        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

        self.rect = pygame.rect.Rect(self.xpos, self.ypos, self.width, self.height)




class Map:

    def __init__(self, screen, screen_width, screen_height, num_rooms_min, room_min_size, room_max_size):

        self.screen = {"screen": screen, "width": screen_width, "height": screen_height}

        self.num_rooms = random.randrange(num_rooms_min, num_rooms_min + 5) # number of rooms to create
        self.room_min_size = room_min_size # min wdith/height of rooms
        self.room_max_size = room_max_size # max wdith/height of rooms
        
        self.rooms_list = [] # list containing the rooms
        self.rooms_added_list = [] # rooms that have already been added onto the screen, used to check collision with other rooms
        self.rooms_added_list_rects = []


    def create_rooms(self):
        
        while(len(self.rooms_list) != (self.num_rooms)):

            w = random.randrange(self.room_min_size + 1, self.room_max_size + 1) # rng for room width
            h = random.randrange(self.room_min_size + 1, self.room_max_size + 1) # rng for room height

            room = Room(0, 0, w, h)
            self.rooms_list.append(room)
            
            print(len(self.rooms_list), self.num_rooms)


    def create_map(self):
    
        if(len(self.rooms_added_list) == 0): # add first room to screen

            x = random.randrange(0, self.screen["width"]) # randomly generate position
            y = random.randrange(0, self.screen["height"])
            print(x, y)

            self.rooms_list[0].rect.x = x # set position for first room
            self.rooms_list[0].rect.y = y

            print(self.rooms_list[0].rect.x, self.rooms_list[0].rect.y)
            print(self.rooms_list[0].width, self.rooms_list[0].height)
            print(self.rooms_list[0])

            pygame.draw.rect(self.screen["screen"], (255, 255, 0), (self.rooms_list[0].rect.x, self.rooms_list[0].rect.y, self.rooms_list[0].width, self.rooms_list[0].height))
            self.rooms_added_list.append(self.rooms_list[0]) # add to list of rooms already on screen
            self.rooms_added_list_rects.append(self.rooms_list[0].rect) # add to list of room's rects already on screen
        
        else:
            while(len(self.rooms_added_list) != len(self.rooms_list)): # until all rooms are added
                print(len(self.rooms_added_list))
                print(len(self.rooms_list))

                for i in range(1, self.num_rooms): # for the second room onwards
                 
                    # self.rooms_added_list[i - 1] is the room before current
                    self.rooms_list[i].rect.x = self.rooms_added_list[i - 1].rect.x
                    self.rooms_list[i].rect.y = self.rooms_added_list[i - 1].rect.y

                    print(self.rooms_list[i].rect.x, self.rooms_list[i].rect.y)

                    direction_x = random.choice([-1, 1]) # randomly pick what direction to move the room in
                    direction_y = random.choice([-1, 1])

                    print(direction_x, direction_y)

                    while(self.rooms_list[i].rect.collidelist(self.rooms_added_list_rects) != -1): # while current room collides with previous rooms
                        
                        #print(self.rooms_list[i].rect.collidelist(self.rooms_added_list_rects))
                        self.rooms_list[i].rect.x = self.rooms_list[i].rect.x + (direction_x * 10) # move room in random direction
                        self.rooms_list[i].rect.y = self.rooms_list[i].rect.y + (direction_y * 10)
                        print(self.rooms_list[i].rect.x, self.rooms_list[i].rect.y)
                    
                    pygame.draw.rect(self.screen["screen"], (255, 255, 0), (self.rooms_list[0].rect.x, self.rooms_list[0].rect.y, self.rooms_list[0].width, self.rooms_list[0].height))
                    self.rooms_added_list.append(self.rooms_list[i]) # add to list of rooms already on screen
                    self.rooms_added_list_rects.append(self.rooms_list[i].rect) # add to list of room's rects already on screen


    
    def update(self):
        
        self.create_rooms()
        self.create_map()
        
        for i in range(len(self.rooms_added_list_rects)):
            pygame.draw.rect(self.screen["screen"], (255, 255, 0), (self.rooms_list[i].rect.x, self.rooms_list[i].rect.y, self.rooms_list[i].width, self.rooms_list[i].height))
                    



# map_one = Map(None, 800, 800, 5, 50, 100)
# map_one.update()


 