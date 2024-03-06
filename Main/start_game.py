import os
import subprocess

def main():
    print("Welcome to Tic Tac Toe!")
    print("1: Single Player Game")
    print("2: Two Player Game")
    choice = input("Enter your choice: ")

    if choice == '1':
        path_to_game = os.path.join('single_player', 'tic_tac_toe_1.py')
        print("\nStarting Single Player Game...")
    elif choice == '2':
        path_to_game = os.path.join('two_player', 'tic_tac_toe_2.py')
        print("\nStarting Two Player Game...")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()
        return

    try:
        # Make sure the path is absolute
        current_directory = os.path.dirname(os.path.abspath(__file__))
        game_path = os.path.join(current_directory, path_to_game)

        # Execute the Python script
        subprocess.run(['python3', game_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to start the game: {e}")
    except FileNotFoundError:
        print(f"The game file {path_to_game} does not exist.")

if __name__ == "__main__":
    main()


