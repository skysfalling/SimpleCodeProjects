import random


tiles = [] #double array
width = 10
height = 10

# create tiles
def init_tileset():
    for i in range(height):
        row = [] #start a new row
        for j in range(width):
            row.append(".") #add column values
        tiles.append(row) #add row to tileset

# print tiles
def print_tileset():
    tiles_string = ""
    for i in range(len(tiles)): #for amount of rows
        for j in range(len(tiles[i])): #for amount of columns in chosen row
            tiles_string += str(tiles[i][j]) + " " #add value based on x, y coordinate
        tiles_string += "\n" #new line for every row
    print(tiles_string) #print everthing after done


def create_entrance():
    # random index in first line is entrance
    random_index = random.randint(0, width-1)
    tiles[0][random_index] = "e"
    print("entrance index: " + str(random_index))

def create_endRoom():
    # random index in first line is entrance
    random_index = random.randint(0, width-1)
    tiles[len(tiles) - 1][random_index] = "B"
    print("end room index: " + str(random_index))

# =========================================================


init_tileset() #create set
create_entrance() #add entrance
create_endRoom() #add end room


print_tileset()


# entrance - 'e'
# battle room - 'b'
# boss room - 'B'
# pathway - 0
# wall - x