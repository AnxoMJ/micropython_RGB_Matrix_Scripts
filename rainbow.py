# Complete project details at https://RandomNerdTutorials.com

import machine, neopixel, time, random
from shapes import *

n = 256
p = 13

arraiPosition = [[-7 for x in range(16)]for y in range(16)]

pixels = neopixel.NeoPixel(machine.Pin(p), n)
np=pixels
num_pixels = n
pixel_pin = p

#apaga el panel
pixels.fill((0, 0, 0))
pixels.write()

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.write()
        time.sleep(wait)

def llenar_array(arraiPosition):
    cont_y=15
    cont_interac=0
    invertido=True

    for i in range(256):
        if cont_interac==16:
            cont_y-=1
            cont_interac=0
            invertido= not invertido
            #print("cambio de fila "+str(cont_salto))
        x=cont_interac
        if invertido :
            x=(x-15)*-1
        arraiPosition[x][cont_y]=i
        #print("valor x: "+str(x)+" valor y: "+str(cont_y)+" valor: "+str(i))
        cont_interac+=1
    return arraiPosition

def leer_array(arraiPosition):
    for x in range(16):
        for y in range(16):
            print("valor x: "+str(x)+" valor y: "+str(y)+" valor: "+str(arraiPosition[x][y]))

#leer_array(arraiPosition)
def animacion_linea(np,arraiPosition):
    for x in range(16):
            for y in range(16):
                np[arraiPosition[0][y]] = (1, 1, 1)
                np[arraiPosition[1][y]] = (1, 1, 1)
                np[arraiPosition[2][y]] = (1, 1, 1)
                np[arraiPosition[3][y]] = (1, 1, 1)
                np[arraiPosition[4][y]] = (1, 1, 1)
                np[arraiPosition[5][y]] = (1, 1, 1)
                np[arraiPosition[6][y]] = (1, 1, 1)
                np[arraiPosition[7][y]] = (1, 1, 1)
                np[arraiPosition[8][y]] = (1, 1, 1)
                np[arraiPosition[9][y]] = (1, 1, 1)
                np[arraiPosition[10][y]] = (1, 1, 1)
                np[arraiPosition[11][y]] = (1, 1, 1)
                np[arraiPosition[12][y]] = (1, 1, 1)
                np[arraiPosition[13][y]] = (1, 1, 1)
                np[arraiPosition[14][y]] = (1, 1, 1)
                np[arraiPosition[15][y]] = (1, 1, 1)
                np.write()
                time.sleep(0.03)
                np.fill((0,0,0,))

def animacion_linea2(np,arraiPosition):
    for x in range(16):
            for y in range(16):
                np[arraiPosition[x][y]] = (1, 1, 1)

                np.write()
                time.sleep(0.03)
            
def mario(np,arraiPosition):
    marron = (3,1,0)
    #marron = (26,5,1)
    #amarillo = (27,18,1)
    amarillo = (3,2,1)
    rojo = (2,0,0)


    np[arraiPosition[4][15]] = (rojo)
    np[arraiPosition[5][15]] = (rojo)
    np[arraiPosition[6][15]] = (rojo)
    np[arraiPosition[7][15]] = (rojo)
    np[arraiPosition[8][15]] = (rojo)

    np[arraiPosition[3][14]] = (rojo)
    np[arraiPosition[4][14]] = (rojo)
    np[arraiPosition[5][14]] = (rojo)
    np[arraiPosition[6][14]] = (rojo)
    np[arraiPosition[7][14]] = (rojo)
    np[arraiPosition[8][14]] = (rojo)
    np[arraiPosition[9][14]] = (rojo)
    np[arraiPosition[10][14]] = (rojo)
    np[arraiPosition[11][14]] = (rojo)

    np[arraiPosition[3][13]] = (marron)
    np[arraiPosition[4][13]] = (marron)
    np[arraiPosition[5][13]] = (marron)
    np[arraiPosition[6][13]] = (amarillo)
    np[arraiPosition[7][13]] = (amarillo)
    np[arraiPosition[8][13]] = (marron)
    np[arraiPosition[9][13]] = (amarillo)

    np[arraiPosition[2][12]] = (marron)
    np[arraiPosition[3][12]] = (amarillo)
    np[arraiPosition[4][12]] = (marron)
    np[arraiPosition[5][12]] = (amarillo)
    np[arraiPosition[6][12]] = (amarillo)
    np[arraiPosition[7][12]] = (amarillo)
    np[arraiPosition[8][12]] = (marron)
    np[arraiPosition[9][12]] = (amarillo)
    np[arraiPosition[10][12]] = (amarillo)
    np[arraiPosition[11][12]] = (amarillo)

    np[arraiPosition[2][11]] = (marron)
    np[arraiPosition[3][11]] = (amarillo)
    np[arraiPosition[4][11]] = (marron)
    np[arraiPosition[5][11]] = (marron)
    np[arraiPosition[6][11]] = (amarillo)
    np[arraiPosition[7][11]] = (amarillo)
    np[arraiPosition[8][11]] = (amarillo)
    np[arraiPosition[9][11]] = (marron)
    np[arraiPosition[10][11]] = (amarillo)
    np[arraiPosition[11][11]] = (amarillo)
    np[arraiPosition[12][11]] = (amarillo)

    np[arraiPosition[2][10]] = (marron)
    np[arraiPosition[3][10]] = (marron)
    np[arraiPosition[4][10]] = (amarillo)
    np[arraiPosition[5][10]] = (amarillo)
    np[arraiPosition[6][10]] = (amarillo)
    np[arraiPosition[7][10]] = (amarillo)
    np[arraiPosition[8][10]] = (marron)
    np[arraiPosition[9][10]] = (marron)
    np[arraiPosition[10][10]] = (marron)
    np[arraiPosition[11][10]] = (marron)

    np[arraiPosition[4][9]] = (amarillo)
    np[arraiPosition[5][9]] = (amarillo)
    np[arraiPosition[6][9]] = (amarillo)
    np[arraiPosition[7][9]] = (amarillo)
    np[arraiPosition[8][9]] = (amarillo)
    np[arraiPosition[9][9]] = (amarillo)
    np[arraiPosition[10][9]] = (amarillo)

    np[arraiPosition[3][8]] = (marron)
    np[arraiPosition[4][8]] = (marron)
    np[arraiPosition[5][8]] = (rojo)
    np[arraiPosition[6][8]] = (marron)
    np[arraiPosition[7][8]] = (marron)
    np[arraiPosition[8][8]] = (marron)

    np[arraiPosition[2][7]] = (marron)
    np[arraiPosition[3][7]] = (marron)
    np[arraiPosition[4][7]] = (marron)
    np[arraiPosition[5][7]] = (rojo)
    np[arraiPosition[6][7]] = (marron)
    np[arraiPosition[7][7]] = (marron)
    np[arraiPosition[8][7]] = (rojo)  
    np[arraiPosition[9][7]] = (marron)
    np[arraiPosition[10][7]] = (marron)  
    np[arraiPosition[11][7]] = (marron)

    np[arraiPosition[1][6]] = (marron)
    np[arraiPosition[2][6]] = (marron)
    np[arraiPosition[3][6]] = (marron)
    np[arraiPosition[4][6]] = (marron)
    np[arraiPosition[5][6]] = (rojo)
    np[arraiPosition[6][6]] = (rojo)
    np[arraiPosition[7][6]] = (rojo)
    np[arraiPosition[8][6]] = (rojo)  
    np[arraiPosition[9][6]] = (marron)
    np[arraiPosition[10][6]] = (marron)  
    np[arraiPosition[11][6]] = (marron)
    np[arraiPosition[12][6]] = (marron)

    np[arraiPosition[1][5]] = (amarillo)
    np[arraiPosition[2][5]] = (amarillo)
    np[arraiPosition[3][5]] = (marron)
    np[arraiPosition[4][5]] = (rojo)
    np[arraiPosition[5][5]] = (amarillo)
    np[arraiPosition[6][5]] = (rojo)
    np[arraiPosition[7][5]] = (rojo)
    np[arraiPosition[8][5]] = (amarillo)  
    np[arraiPosition[9][5]] = (rojo)
    np[arraiPosition[10][5]] = (marron)  
    np[arraiPosition[11][5]] = (amarillo)
    np[arraiPosition[12][5]] = (amarillo)

    np[arraiPosition[1][4]] = (amarillo)
    np[arraiPosition[2][4]] = (amarillo)
    np[arraiPosition[3][4]] = (amarillo)
    np[arraiPosition[4][4]] = (rojo)
    np[arraiPosition[5][4]] = (rojo)
    np[arraiPosition[6][4]] = (rojo)
    np[arraiPosition[7][4]] = (rojo)
    np[arraiPosition[8][4]] = (rojo)  
    np[arraiPosition[9][4]] = (rojo)
    np[arraiPosition[10][4]] = (amarillo)  
    np[arraiPosition[11][4]] = (amarillo)
    np[arraiPosition[12][4]] = (amarillo)

    np[arraiPosition[1][3]] = (amarillo)
    np[arraiPosition[2][3]] = (amarillo)
    np[arraiPosition[3][3]] = (rojo)
    np[arraiPosition[4][3]] = (rojo)
    np[arraiPosition[5][3]] = (rojo)
    np[arraiPosition[6][3]] = (rojo)
    np[arraiPosition[7][3]] = (rojo)
    np[arraiPosition[8][3]] = (rojo)  
    np[arraiPosition[9][3]] = (rojo)
    np[arraiPosition[10][3]] = (rojo)  
    np[arraiPosition[11][3]] = (amarillo)
    np[arraiPosition[12][3]] = (amarillo)

    np[arraiPosition[3][2]] = (rojo)
    np[arraiPosition[4][2]] = (rojo)
    np[arraiPosition[5][2]] = (rojo)
    np[arraiPosition[8][2]] = (rojo)  
    np[arraiPosition[9][2]] = (rojo)
    np[arraiPosition[10][2]] = (rojo)  

    np[arraiPosition[2][1]] = (marron)
    np[arraiPosition[3][1]] = (marron)
    np[arraiPosition[4][1]] = (marron)
    np[arraiPosition[9][1]] = (marron)
    np[arraiPosition[10][1]] = (marron)
    np[arraiPosition[11][1]] = (marron)

    np[arraiPosition[1][0]] = (marron)
    np[arraiPosition[2][0]] = (marron)
    np[arraiPosition[3][0]] = (marron)
    np[arraiPosition[4][0]] = (marron)
    np[arraiPosition[9][0]] = (marron)
    np[arraiPosition[10][0]] = (marron)
    np[arraiPosition[11][0]] = (marron)
    np[arraiPosition[12][0]] = (marron)

    np.write()

llenar_array(arraiPosition)


def string_to_led(text):
    return {
        'a': ([15,0],[15,1],[15,2],[14,3],[14,1],[13,0],[13,1],[13,2]),
        'b': ([15,1],[14,0],[14,2],[13,1],[13,2],[13,3]),
        'c': ([15,0],[15,3],[14,0],[14,3],[13,1],[13,2]),
        'd': ([15,1],[15,2],[14,0],[14,3],[13,0],[13,1],[13,2],[13,3]),
        'e': ([15,0],[15,2],[14,0],[14,1],[14,3],[13,1],[13,2]),
        'f': ([15,1],[15,3],[14,1],[14,3],[13,0],[13,1],[13,2],[13,3]),
        'g': ([15,0],[15,1],[15,3],[14,0],[14,1],[14,3],[13,0],[13,1],[13,2],[13,3]),
        'h': ([15,0],[15,1],[14,2],[13,0],[13,1],[13,2],[13,3]),
        'i': ([15,0],[15,3],[14,0],[14,1],[14,2],[14,3],[13,0],[13,3]),
        'j': ([15,1],[15,2],[15,3],[14,0],[14,3],[13,1],[13,3]),
        'k': ([15,0],[15,3],[14,1],[14,2],[13,0],[13,1],[13,2],[13,3]),
        'l': ([15,0],[14,0],[13,0],[13,1],[13,2],[13,3]),
        'm': ([15,0],[15,1],[15,2],[15,3],[14,2],[13,0],[13,1],[13,2],[13,3]),
        'n': ([15,0],[15,1],[14,2],[13,0],[13,1],[13,2]),
        'ñ': ([15,0],[15,1],[14,2],[14,3],[13,0],[13,1],[13,2],[15,3]),
        'o': ([15,1],[15,2],[14,0],[14,3],[13,1],[13,2]),
        'p': ([15,2],[14,1],[14,3],[13,0],[13,1],[13,2],[13,3]),
        'q': ([13,2],[14,1],[14,3],[15,0],[15,1],[15,2],[15,3]),
        'r': ([13,0],[13,1],[13,2],[13,3],[14,1],[14,3],[15,0],[15,2]),
        's': ([13,0],[13,2],[14,0],[14,3],[15,1],[15,3]),
        't': ([13,3],[14,0],[14,1],[14,2],[14,3],[15,3]),
        'u': ([13,0],[13,1],[13,2],[13,3],[14,0],[15,0],[15,1],[15,2],[15,3]),
        'v': ([13,1],[13,2],[13,3],[14,0],[15,1],[15,2],[15,3]),
        'w': ([13,0],[13,1],[13,2],[13,3],[14,1],[15,0],[15,1],[15,2],[15,3]),
        'x': ([13,0],[13,3],[14,1],[14,2],[15,0],[15,3]),
        'y': ([13,3],[14,0],[14,1],[14,2],[15,3]),
        'z': ([13,0],[13,1],[13,3],[14,0],[14,2],[14,3],[15,0],[15,3]),
        '1': ([13,2],[13,0],[14,0],[14,1],[14,2],[14,3],[15,0]),
        '2': ([13,2],[13,0],[14,0],[14,1],[14,3],[15,0],[15,2]),
        '3': ([13,0],[13,3],[14,1],[14,3],[15,0],[15,2]),
        '3': ([13,0],[13,3],[14,1],[14,0],[14,3],[15,0],[15,2],[15,1],[15,3]),
        '4': ([13,2],[13,1],[14,1],[14,3],[15,0],[15,2],[15,1],[15,3]),
        '5': ([13,2],[13,3],[13,1],[14,0],[14,3],[15,1],[15,3]),
        '6': ([15,0],[15,1],[15,3],[14,0],[14,1],[14,3],[13,0],[13,1],[13,2]),
        '7': ([15,2],[15,3],[14,0],[14,1],[14,3],[13,3]),
        '8': ([15,0],[15,2],[14,1],[14,3],[13,0],[13,2]),
        '9': ([15,0],[15,1],[15,2],[14,1],[14,3],[13,2]),
        '0': ([15,1],[15,2],[14,0],[14,3],[13,1],[13,2]),
        '.': ([15,0],[15,0]),
        ',': ([15,1],[14,0]),
        '!': ([15,0],[15,2],[15,3]),
        '¡': ([15,0],[15,1],[15,3]),
        '?': ([15,2],[14,0],[14,1],[14,3]),
        '¿': ([15,0],[15,1],[15,3],[14,2]),
        '|': ([15,0],[15,1],[15,2],[15,3]),
        ')': ([15,1],[15,2],[14,0],[14,3]),
        '(': ([15,0],[15,3],[14,1],[14,2]),
        '=': ([15,0],[15,2],[14,0],[14,2],[13,0],[13,2]),
        '-': ([15,1],[14,1],[13,1]),
        '_': ([15,0],[14,0],[13,0]),
        '<': ([15,0],[15,2],[14,1]),
        '>': ([15,1],[14,0],[14,2]),
        '^': ([15,1],[14,2],[13,1]),
        '+': ([15,1],[14,0],[14,1],[14,2],[13,1]),
        '[': ([15,0],[15,3],[14,0],[14,1],[14,2],[14,3]),
        ']': ([15,0],[15,1],[15,2],[15,3],[14,0],[14,3]),
        ':': ([15,0],[15,2]),
    }.get(text,())
def caca(np,arraiPosition):
    i=0
    cont=0
    while True:
        time.sleep(0.1)
        np.fill((0,0,0))
        for x,y in string_to_led("c"):
            x-=12
            if x-i<16: x-=i
            else: x=0
            np[arraiPosition[x][y]] = (0,0,1)
        for x,y in string_to_led("a"):
            x-=8
            if x-i<16: x-=i
            else: x=0
            np[arraiPosition[x][y]] = (1,0,0)
        for x,y in string_to_led("c"):
            x-=4
            if x-i<16: x-=i
            else: x=0
            np[arraiPosition[x][y]] = (1,0,1)
        for x,y in string_to_led("a"):
            if x-i<16: x-=i
            else: x=0
            np[arraiPosition[x][y]] = (0,1,0)
        np.write()
        if i==15:
            i=0
        else:
            i+=1
        cont+=1
        if cont > 70:
            break


i=0
cont=0
while True:
    time.sleep(0.1)
    np.fill((0,0,0))
    for x,y in string_to_led("6"):
        if x-i<16: x-=i
        else: x=0
        np[arraiPosition[x][y]] = (0,0,1)
    np.write()
    if i==15:
        i=0
    else:
        i+=1
    cont+=1
    if cont > 5:
        break


#random.randint(0,1)

""" np[arraiPosition[15][0]] = (0,0,1)
np[arraiPosition[15][1]] = (0,0,1)
np[arraiPosition[15][2]] = (0,0,1)
np[arraiPosition[14][3]] = (0,0,1)
np[arraiPosition[14][1]] = (0,0,1)
np[arraiPosition[13][0]] = (0,0,1)
np[arraiPosition[13][1]] = (0,0,1)
np[arraiPosition[13][2]] = (0,0,1) """










np.write()

#time.sleep(2)
#pixels.fill((0, 0, 0))
#pixels.write()





