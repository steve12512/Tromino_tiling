Read the assignment pdf for more info.
The purpose of the project is to create a specifically colored square that only has one hollow point. 
The user runs the tromino_tiling.py file passing an integer from the command line and the program creates a square of  2^integer x 2^integer dimensions.
Then the program proceeds to call itself recursively for 4 squares  whose each side has half the length of the previous square.
The process repeats until we have 2x2 squares that we then color in a specific way.
Run the script and save the results in a txt file.
Then proceed to pass the txt file as input in the draw_tromino_tiling.py file which will paint the square.
