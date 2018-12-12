# Author: Carlton Brady

import time
import random


def create_world(size_x, size_y):
    outer_list=[]
    for i in range(size_y):
        row = []
        for j in range(size_x):
            # Set the odds of a cell being alive in the initial state of the world
            random.seed()
            if random.random() > .95:
                row.append("X")
            else:
                row.append(" ")
        outer_list.append(row)
    return outer_list


def display_world(world):
    world_string = ""
    for i in range(len(world)):
        for j in range(len(world[0])):
            world_string+=world[i][j]
        world_string+="\n"
    return world_string


def count_live_neighbors(world, i, j):
    num_alive = 0
    if j < len(world[0])-1:
        if world[i][j+1] == "X":
            num_alive += 1
    if j > 0:
        if world[i][j-1] == "X":
            num_alive += 1
    if i > 0:
        if world[i-1][j] == "X":
            num_alive += 1
    if i < len(world)-1:
        if world[i+1][j] == "X":
            num_alive += 1
    if i > 0 and j < len(world[0])-1:
        if world[i-1][j+1] == "X":
            num_alive += 1
    if i > 0 and j > 0:
        if world[i-1][j-1] == "X":
            num_alive += 1
    if i < len(world)-1 and j > 0:
        if world[i+1][j-1]:
            num_alive += 1
    if i < len(world)-1 and j < len(world[0])-1:
        if world[i+1][j+1] == "X":
            num_alive += 1
    return num_alive


def get_next_generation(world, i, j):
    num_neighbors = count_live_neighbors(world, i, j)
    if world[i][j] == "X":
        if num_neighbors < 2:
            return " "
        elif num_neighbors == 2 or num_neighbors == 3:
            return "X"
        elif num_neighbors > 3:
            return " "
    else:
        if num_neighbors == 3:
            return "X"
        else:
            return " "


def tick(world):
    new_world = world
    for i in range(len(world)):
        for j in range(len(world[0])):
            new_world[i][j] = get_next_generation(world, i, j)
    return new_world


def start(size_x, size_y):
    state = create_world(size_x,size_y)
    while True:
        state = tick(state)
        time.sleep(.5)
        print(display_world(state))


# Run it with a certain world size
start(40,20)
