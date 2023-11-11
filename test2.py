arraiPosition = [[" " for x in range(16)]for y in range(16)]

""" cont_f = 0
cont_l = 0

for(x) in arraiPosition:
    #print("Fila: "+str(cont_f))
    if cont_f <= 7 :
        arraiPosition[cont_f][cont_f+2]=0
    cont_l=0
    for (y) in x:
     #   print("Linea: "+str(cont_l))
        
        cont_l+=1
    cont_f+=1 """

import time

def fill_array(arraiPosition,value):
    cont_f = 0
    cont_l = 0

    for(x) in arraiPosition:
        cont_l=0
        for (y) in x:
        #   print("Linea: "+str(cont_l))
            arraiPosition[cont_f][cont_l]= value
            cont_l+=1
        cont_f+=1
""" def print_array():
    for(x) in arraiPosition:
        print (x) """

def print_array():
    for row in arraiPosition:
        for col in row:
            print(col, end=' ')
        print()

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

def word_len(letter):
    pr_x = ""
    for x,y in string_to_led(letter):
        if str(x) not in str(pr_x):
            pr_x+=str(x)
    pr_x=pr_x.replace("1","")
    return(len(pr_x))

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
#def caca(np,arraiPosition):
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
        print_array()
        if i==15:
            i=0
        else:
            i+=1
        cont+=1
        if cont > 70:
            break






print(word_len("."))


exit
i=0
cont=0

fill_array(arraiPosition, " ")
frase="."
word_count=0
for f in frase:
    initial=True
    for x,y in string_to_led(f):
        if initial:
            initial=False
            print(word_len(str(x)))
            #word_count+=(word_len(str(x)))
            word_count+=(1)
            offset=16-(word_count)   
            #print(offset)
        x-=offset     
        if x-i<16: x-=i
        else: x=0
        arraiPosition[x][y] = 0
    word_count+=1
    if i==15:
        i=0
    else:
        i+=1
    cont+=1
arraiPosition=rotar_array(arraiPosition)
print_array()



while False:
    fill_array(arraiPosition, " ")
    frase="cc"
    word_count=0
    for f in frase:
        initial=True
        for x,y in string_to_led(f):
            if initial:
                initial=False
                word_count+=(word_len(str(x)))
                offset=15-(word_count)   
                #print(offset)
            x-=offset     
            if x-i<16: x-=i
            else: x=0
            arraiPosition[x][y] = 0

        if i==15:
            i=0
        else:
            i+=1
        cont+=1
    time.sleep(0.3)
    if cont > 0:
        break
    arraiPosition=rotar_array(arraiPosition)
    print_array()
    
    break
        

