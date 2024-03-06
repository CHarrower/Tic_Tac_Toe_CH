from main_board_1 import draw_board, check_turn, check_for_win, computer_move
import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn

    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot (1-9) or press 'q' to quit:")
    choice = input()

    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in ["X", "O"]:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8: playing = False

    # Computer's move
    if playing and not complete:
        computer_spot = computer_move(spots)
        turn += 1
        spots[computer_spot] = check_turn(turn)

    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8: playing = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

if complete:
    if check_turn(turn) == 'X':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
else:
    print("It's a draw")

print("Thanks for playing!")
