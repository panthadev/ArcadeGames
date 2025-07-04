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

    def __init__(self, screen, screen_width, screen_height, num_rooms, room_min_size, room_max_size):

        self.screen = {"screen": screen, "width": screen_width, "height": screen_height}

        self.num_rooms = num_rooms # number of rooms to create
        self.room_min_size = room_min_size # min wdith/height of rooms
        self.room_max_size = room_max_size # max wdith/height of rooms
        
        self.rooms_list = [] # list containing the rooms
        self.rooms_added_list = [] # rooms that have already been added onto the screen, used to check collision with other rooms
        

    def create_rooms(self):
        
        for i in range(self.num_rooms):

            w = random.randrange(self.room_min_size + 1, self.room_max_size + 1) # rng for room width
            h = random.randrange(self.room_min_size + 1, self.room_max_size + 1) # rng for room height

            room = Room(0, 0, w, h)
            self.rooms_list.append(room)
            
            print(self.rooms_list)


    

    def create_map(self):

        for i in range(self.num_rooms):

            if(len(self.rooms_added_list) == 0): # add first room to screen

                x = random.randrange(0, self.screen["width"]) # randomly generate position
                y = random.randrange(0, self.screen["height"])

                self.rooms_list[0].xpos = x # set position for first room
                self.rooms_list[0].ypos = y

                
                pass
            
            else:
                pass


        pass

    
    def update(self):
        
        self.create_rooms()



map_one = Map(None, 5, 50, 100)
map_one.update()


 