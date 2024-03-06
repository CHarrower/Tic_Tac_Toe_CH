from main_board import draw_board, check_turn, check_for_win
import os

spots = {1 :'1', 2 :'2', 3 :'3', 4 :'4', 5 :'5', 6 : '6', 7 :'7', 8 :'8', 9 :'9'}

playing = True 
complete = False
turn = 0
prev_turn = -1

while playing:
    #reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #if an invalid turn occurred, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1) + "'s turn: Pick your spot or press 'q' to quit:")
    #get the input from the player
    choice = input()
    if choice == 'q':
        playing == False 
    #check if the player gave a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        #check if the spot has already been taken
        if not spots[int(choice)] in ["X", "O"]:
            #valid input, update board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    #check if the game has ended (if someone won)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing - False 

#Print Result
#Draw the board one last time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#if the is a winner, say who won
if complete:
    if check_turn(turn) == 'X': print("player 1 wins!")
    else: print("player 2 wins!")
else:
    #tie
    print("Its a draw")

print("Thanks for playing!")