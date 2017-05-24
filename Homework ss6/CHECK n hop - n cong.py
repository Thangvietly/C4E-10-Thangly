#box_pusher
#box
#map
#destination

#set_pusher_coordinate
#rep: P
pusher_x = 1
pusher_y = 0
#set_box_coordinate
#rep: B
boxes=[
    {"x":3,"y":2},
    {"x":1,"y":3},
    {"x":0,"y":2}
    ]
#set_destination_coordinate
dests=[
    {"x":4,"y":5},
    {"x":1,"y":4},
    {"x":0,"y":3}
    ]

#set map_size
size_x=10
size_y=10



def in_map(size_x, size_y, x, y):
    return 0 <= x < size_x and 0 <= y < size_y
        
def check_overlap(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False

def print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests):
    for y in range (size_y):
        for x in range( size_x):
            if x == pusher_x and y == pusher_y:
                print(" P ", end = "")
                
            elif check_overlap(x, y, boxes):
                print(" B ", end = "")
                
            elif check_overlap(x, y, dests):
                print(" D ", end = "")
            else:
                print(" - ", end = "")
        print()
print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy = -1
    elif direction == "S":
        dy = 1
    elif direction == "D":
        dx = 1
    elif direction == "A":
        dx = -1
    else:
        print("You enter wrong button pls do this again bro:)")
    return dx, dy

def which_box(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return item
        
#main GAME_LOOP
while True:
    direction = input("What's your next move? W/A/S/D: ").upper()
    #xu ly dau vao
    dx,dy = input_process(direction)
    
    if check_overlap( pusher_x + dx, pusher_y +dy, boxes):
        if in_map(size_x, size_y, pusher_x +2*dx, pusher_y + 2*dy):
            pusher_x += dx
            pusher_y += dy
            box = which_box(pusher_x, pusher_y, boxes)
            box["x"]+= dx
            box["y"] += dy
        else:
            print(" | Box can't be moved T.T |")
                
    else: # CHO THANG DAY HOP CHAY
        if in_map(size_x, size_y, pusher_x + dx, pusher_y + dy):
            pusher_x += dx
            pusher_y += dy
        else:
            print(" | Hey, you can't go there bro T.T |")
                
    #Check win
    check = 0
    for box in boxes:
        if check_overlap(box["x"], box["y"], dests):
            check += 1
    if check == len(boxes):
        print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)
        print(" |YOU ARE THE WINNER |")
        break
    
    print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)
 
                      




