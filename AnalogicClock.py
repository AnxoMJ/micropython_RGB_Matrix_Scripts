""" arraiPosition = [[1 for x in range(16)]for y in range(16)]

cont_f = 0
cont_l = 0

for(x) in arraiPosition:
    #print("Fila: "+str(cont_f))
    if cont_f <= 7 :
        arraiPosition[cont_f][cont_f+2]=0
    cont_l=0
    for (y) in x:
     #   print("Linea: "+str(cont_l))
        
        cont_l+=1
    cont_f+=1


for(x) in arraiPosition:
    print (x)
 """

import time
import math
import datetime

def show_array(arr):
    for(x) in arr:
        print (x)

def rotar_array(arr):
    arrTMP = [[0 for x in range(16)]for y in range(16)]
    cont_f=0
    for(x) in arr:
        cont_l=0
        for (y) in x:
        #   print("Linea: "+str(cont_l))
            arrTMP[15-cont_l][cont_f]=y
            cont_l+=1
        cont_f+=1

    return arrTMP

#import numpy as np

#[[" " for x in range(16)]for y in range(16)]
#Finds a line between two points
def get_line(x0, y0, x1, y1, arr, filler):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while (x0 != x1) or (y0 != y1):
        points.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    points.append((x0, y0))

    for point in points:
        x, y = point
        arr[x][y] = filler
    
    return points



def create_analog_clock():
    arr = [[" " for x in range(16)]for y in range(16)]

    center_x, center_y = 7, 8

    #current_time = input("Enter the time in HH:MM format: ")
    #hours, minutes = map(int, current_time.split(':'))

    hours = (datetime.datetime.now().hour-12)*-1
    minutes = datetime.datetime.now().minute
    seconds = datetime.datetime.now().second

    hour_angle = math.radians((360 / 12) * (hours % 12) + (30 / 60) * minutes)
    minute_angle = math.radians((360 / 60) * minutes)
    second_angle = math.radians((360 / 60) * seconds)

    hour_x = int(4 * math.sin(hour_angle) + center_x)
    hour_y = int(4* math.cos(hour_angle) + center_y)

    minute_x = int(6 * math.sin(minute_angle)+ center_x)
    minute_y = int(6 * math.cos(minute_angle)+ center_y)

    second_x = int(7 * math.sin(second_angle)+ center_x)
    second_y = int(7 * math.cos(second_angle)+ center_y)

    arr[center_x][center_y] = 'O'
    arr[hour_x][hour_y] = 'H'
    arr[minute_x][minute_y] = 'M'
    arr[second_x][second_y] = 'S'

    # Get the line points
    get_line(center_x, center_y,hour_x,hour_y,arr,"H")
    # Get the line points
    get_line(center_x, center_y,minute_x,minute_y,arr,"M")
    # Get the line points
    get_line(center_x, center_y,second_x,second_y,arr,"S")

    return arr

def update_clock():
    clock_array = create_analog_clock()
    clock_array = rotar_array(clock_array)
    show_array(clock_array)


for x in range(60):
    update_clock()
    print("                    ")
    time.sleep(2)
