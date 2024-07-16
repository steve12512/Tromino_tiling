import sys
import argparse


#create the function that will initialize an empty tromino
def initialize_square(n):

    square= []
    for i in range(0, 2**n):
        row = []
        for j in range(0, 2**n):
            row.append('.')
        square.append(row)

    return square


#define the function that will be creating trominos
def give_values(current_power, square = None, bigger_square = None, x_start = None, x_end = None, y_start = None, y_end =None, quarter = None, is_hollow = None):

    global placed_black_pixel

    #if we are on the first execution, initialize our biggest square, at original power n
    if (current_power == n ):
        square = initialize_square(n)


    center = 2**current_power // 2 - 1

    #check if the current power is 1 and if it is, create a simple tromino
    if (current_power == 1):
        #create a simple tromino
        square = initialize_square(1)
        square[0][0] = 'G'
        square[1][0] = 'G'
        square[1][1] = 'G'
        for x in square:
            print(' '.join(filter(lambda char: char not in ["'", ","], x)))
        exit()
    elif (current_power == 2):
        #check the quarter that we are in

        #check if original n ==2 
        if (n == current_power):
            square[1][1] = 'G'
            square[1][2] = 'G'
            square[2][1] = 'G'
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[2][2] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[0][2] = 'R'
            square[0][3] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[3][0] = 'R'
            square[3][1] = 'R'
            square[3][3] = 'X'
            
            #print our square and exit afterwards
            for x in square:
                print(' '.join(filter(lambda char: char not in ["'", ","], x)))
            exit()

        elif (quarter == 0):
            #check to see if we are at the square that contains the X pixel
            if (bigger_square[3][3] == 'X'):
                square[center][center] = 'G'
                square[center][center + 1] = 'G'
                square[center + 1][center] = 'G'
                #print('DGEAHBNSRBJ')
            #first quarter
            #check whether or not we are coming from a hollow square
            elif (is_hollow):
                #if it is hollow, create a center green tromino opposite of the quarter
                square[center][center + 1]= 'G'
                square[center + 1][center] = 'G'
                square[center + 1][center + 1] = 'G'
                 
            else:
                #if it isnt, create a center green tromino that is like the quarter 
                square[center][center] = 'G'
                square[center][center + 1] = 'G'
                square[center + 1][center] = 'G'
        elif (quarter == 1):
            if not(is_hollow):
                square[center][center] = 'G'
                square[center][center + 1] = 'G'
                square[center + 1][center + 1] = 'G'
            else:
                square[center][center] = 'G'
                square[center + 1][center] = 'G'
                square[center + 1][center + 1] = 'G'    
        elif (quarter == 2):
            if not(is_hollow):
                square[center][center] = 'G'
                square[center + 1][center] = 'G'
                square[center + 1][center + 1] = 'G'
            else:
                square[center][center] = 'G'
                square[center][center + 1] = 'G'
                square[center + 1][center + 1] = 'G'

        else:
            if not(is_hollow):
                square[center][center + 1]= 'G'
                square[center + 1][center] = 'G'
                square[center + 1][center + 1] = 'G'
            else:
                square[center][center] = 'G'
                square[center][center + 1] = 'G'
                square[center + 1][center] = 'G'

        give_colors(square, quarter, is_hollow)
        update_tromino(x_start, x_end, y_start, y_end, square, bigger_square)
        #check to see if we are at the last execution and last iteration

    else :
        
        #place a green tromino in the center position depending on which quarter we are at, and if we are at the upper left(that has the hollow pixel), check whether or not we have already placed it.
        place_green_on_square(quarter, square, center, is_hollow)

        #we have to reduce our square into n-1 squares
        current_power -= 1      

        #for every quarter
        for i in range(0,4):

            divided_square = initialize_square(current_power)
            x_start, x_end, y_start, y_end, quarter = set_coordinates(i,current_power,divided_square)

        
            is_hollow = check_hollowness(quarter, square, center) 
            #then proceed with the recursion
           
            give_values(current_power, divided_square, square, x_start, x_end, y_start, y_end, quarter, is_hollow)


            #once the sub square is filled and its recursions have stopped, fill the bigger square
            update_tromino(x_start, x_end, y_start, y_end, divided_square, square)

            #check whether or not we should place the black pixel
            if (current_power == 3 or n == 3) and (quarter == 0) and not(placed_black_pixel):
                square[center // 2][center // 2] = 'X'
                placed_black_pixel = True
                square = fix_square(square)
                if (n == 3):
                    square[3][3] = 'X'

        #once all recursions and iteration finish, update the final bigger square.
        update_tromino(x_start, x_end, y_start, y_end, divided_square, square)
        #print('last')

        return square
        
def place_green_on_square(quarter, square, center, is_hollow = True):
    #place the green tromino on the center of the current square, depending on the quarter we are in

    if (quarter == 0):
        if (is_hollow):
            #use reverse green trominos
            square[center][center + 1] = 'G'
            square[center + 1 ][center] = 'G'
            square[center + 1 ][center + 1] = 'G'
        else:
            square[center][center] = 'G'
            square[center][center + 1] = 'G'
            square[center + 1][center] = 'G'
    elif (quarter == 1):
        if not(is_hollow):
            square[center][center] = 'G'
            square[center][center + 1] = 'G'
            square[center + 1][center + 1] = 'G'
        else:
            square[center][center] = 'G'
            square[center + 1][center] = 'G'
            square[center + 1][center + 1] = 'G'
    elif (quarter == 2):
        if not(is_hollow):
            square[center][center] = 'G'
            square[center + 1][center] = 'G'
            square[center + 1][center + 1] = 'G'
        else:
            square[center][center] = 'G'
            square[center][center + 1] = 'G'
            square[center + 1][center + 1] = 'G'
    else:
        if not(is_hollow):
            square[center][center + 1] = 'G'
            square[center + 1 ][center] = 'G'
            square[center + 1 ][center + 1] = 'G'
        else:
            square[center][center] = 'G'
            square[center][center + 1] = 'G'
            square[center + 1][center] = 'G'







def update_tromino(x_start, x_end, y_start, y_end, square, bigger_square):
    #update the original square(tromino) based on the divided square at the time
        #before we proceed with the division, append our new square green center tromino to the original(tromino) square
            #initiliaze the coordinates of the divided square
            k = 0
            for i in range(x_start, x_end):
                l = 0
                for j in range(y_start, y_end):
                    #check that the initial square's coordinates are not already colored
                    if (bigger_square[i][j] not in ['R', 'G', 'B', 'X']):
                        bigger_square[i][j]= square[k][l]
                    l +=1
                k += 1

        


def set_coordinates(i,current_power, square):

    #depending on the quarter (specified by i), we pass  different square coordinates
    if (i ==0):
        #pass the upper left square to the function
        x_start = 0
        x_end = 2**current_power 
        y_start = 0
        y_end = 2**current_power

    elif (i == 1):
        #pass the upper right
        x_start = 0
        x_end = 2**current_power
        y_start = 2**current_power
        y_end = y_start * 2

    elif (i == 2):
        #pass the lower left
        x_start = 2**current_power 
        x_end = x_start * 2
        y_start = 0
        y_end =  2**current_power

    else:
        #pass the lower right
        x_start = 2**current_power 
        x_end = x_start * 2
        y_start = 2**current_power
        y_end = y_start * 2

    #depending on which quarter we are at, and whether or not we have placed(or leaved empty the spave of) the hollow pixel, we can judge the way the center tromino is going to be placed.
    quarter = i

    return x_start, x_end, y_start, y_end, quarter

def check_hollowness(quarter, square, center):
    #check the coordinates of the bigger square to decide whether or not it is hollow

        #first check to see whether or not we are at current power 3(square == 8x8) and quarter = 0  and this is the first time this happens, which we check by placing the X pixel and saving it in a boolean variable
    if (len(square) == 8) and (quarter == 0) and placed_black_pixel:
        is_hollow = False

    if (quarter == 0 ):
        if (square[center][center] != 'G'):
            is_hollow = True
        else :
            is_hollow = False
    elif (quarter == 1):
        if (square[center][center + 1] != 'G'):
            is_hollow = True
        else:
            is_hollow = False
    elif (quarter == 2):
        if (square[center + 1][center] != 'G'):
            is_hollow = True        
        else:
            is_hollow = False
    else:
        if (square[center + 1][center + 1] != 'G'):
            is_hollow = True
        else:
            is_hollow = False

    return is_hollow


def fix_square(square):
    #change the upper left quarter green tromino in order to stop the reversal of the shape, due to hollow pixels
    square[1][1] = 'G'
    square[0][0] = 'B'
    square[0][1] = 'B'
    square[1][0] = 'B'
    square[2][2] = 'B'
    square[2][3] = 'B'
    square[3][2] = 'B'
    square[0][2] = 'R'
    square[0][3] = 'R'
    square[1][3] = 'R'
    square[2][0] = 'R'
    square[3][0] = 'R'
    square[3][1] = 'R'

    return square


def give_colors(square, quarter, is_hollow):
    #paint red and blue colors in the 2x2 square, based on where its green tromino is positioned at

    if (quarter == 0):
        if (is_hollow):
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[0][2] = 'R'
            square[0][3] = 'R'
            square[1][0] = 'B'
            square[1][1] = 'B'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[3][0] = 'R'
            square[3][1] = 'R'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[3][3] = 'B'
        else:
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[2][2] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[0][2] = 'R'
            square[0][3] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[3][0] = 'R'
            square[3][1] = 'R'
    elif (quarter == 1):
        if (is_hollow):
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[3][3] = 'B'
            square[0][2] = 'R'
            square[1][2] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[3][0] = 'R'
            square[3][1]=  'R'
        else:
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[3][2] = 'B'
            square[3][3] = 'B'
            square[0][2] = 'R'
            square[0][3] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[2][1] = 'R'
            square[3][1] = 'R'
    elif (quarter == 2):
        if (is_hollow):
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[3][2] = 'B'
            square[3][3] = 'B'
            square[0][2] = 'R'
            square[0][3] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[2][1] = 'R'
            square[3][1] = 'R'
        else:
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[3][3] = 'B'
            square[0][2] = 'R'
            square[1][2] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[3][0] = 'R'
            square[3][1]=  'R'
    elif (quarter == 3):
        if (is_hollow):
            square[0][0] = 'B'
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[2][2] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[0][2] = 'R'
            square[0][3] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[3][0] = 'R'
            square[3][1] = 'R'
        else:
            square[0][1] = 'B'
            square[1][0] = 'B'
            square[1][1] = 'B'
            square[2][3] = 'B'
            square[3][2] = 'B'
            square[3][3] = 'B'
            square[0][2] = 'R'
            square[0][3] = 'R'
            square[1][3] = 'R'
            square[2][0] = 'R'
            square[3][0] = 'R'
            square[3][1]=  'R'
    return square

### START ###
#read the argument
n = sys.argv[1]

#turn the argument into an integer
n = int(n)

#save whether or not we have placed the black pixel yet
placed_black_pixel = False

#create our colors, by firstly passing the original power    
square = give_values(n)
for x in square:
    print(' '.join(filter(lambda char: char not in ["'", ","], x)))