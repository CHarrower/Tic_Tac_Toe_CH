import random

def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
    f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
    f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

def computer_move(spots):
    available_spots = [spot for spot in spots if spots[spot] not in ["X", "O"]]
    return random.choice(available_spots)

def check_turn(turn):
    if turn % 2 == 0: return 'O'
    else: return 'X'

def check_for_win(spots):
    #check horizontal 
    if  (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
        or (spots[7] == spots[8] == spots[9]):
        return True
    #check vertical
    elif (spots[1] == spots[4] == spots[7]) \
        or (spots[2] == spots[5] == spots[8]) \
        or (spots[3] == spots[6] == spots[9]):
        return True
    #check diagonal
    elif (spots[1] == spots[5] == spots[9]) \
        or (spots[3] == spots[5] == spots[7]):
        return True 

    else: return False 
