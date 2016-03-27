# James Purpura 88625456

# othello_interface

import othello_logic

### Game Views

def _score_view(othello: othello_logic.OthelloState) -> None:
    """Prints the score"""
    print("B:", othello.calculate_score("B"), "W:", othello.calculate_score("W"))

def _board_view(othello: othello_logic.OthelloState) -> str:
    """Returns the board in a clear format"""
    rows = othello.rows()
    columns = othello.columns()
    board = othello.board()
    for row in range(rows):
        this_row = ""
        for column in range(columns):
            if board[row][column] == 0:
                this_row += ". "
            else:
                this_row += (board[row][column] + " ")
        print(this_row)

### Winning Messages

def _print_winner(othello: othello_logic.OthelloState) -> None:
    """Returns the winning player, or None if tied"""
    black_score = othello.calculate_score("B")
    white_score = othello.calculate_score("W")
    if othello.winning_score() == ">":
        if black_score > white_score:
            print("WINNER: B")
        elif white_score > black_score:
            print("WINNER: W")
        else:
            print("NONE")
    else:
        if black_score < white_score:
            print("WINNER: B")
        elif white_score < black_score:
            print("WINNER: W")
        else:
            print("NONE")

def _winning_display(othello: othello_logic.OthelloState) -> None:
    """Prints the board and the winner"""
    _score_view(othello)
    _board_view(othello)
    _print_winner(othello)
    
### Moves
    
def _move_heading(othello: othello_logic.OthelloState, player: str) -> None:
    """Prints out the move heading: score, board, turn"""
    _score_view(othello)
    _board_view(othello)
    print("TURN: " + player)
    
def _move_input() -> (int, int):
    """Prompts the user for a move, returns the input in a tuple
    of form (int, int)"""
    move = input().strip().split()
    move_row = int(move[0]) - 1
    move_column = int(move[1]) - 1
    move_tuple = (move_row, move_column)
    return move_tuple

def _move_process(othello: othello_logic.OthelloState, player: str) -> None:
    """Executes the move, asks user for input until valid"""
    while True:
        try:
            move_tuple = _move_input()
            move_row, move_column = move_tuple
            if othello.player_move(player, (move_row, move_column)):
                print("VALID")
                break
            else:
               raise
        except:
            print("INVALID")

### Play Game

def run_othello() -> None:
    """The user interface for the game Othello"""
    print("FULL")
    rows = int(input())
    columns = int(input())
    first_player = input()
    left_center_player = input()
    winning_score = input()
    othello = othello_logic.OthelloState(rows, columns, first_player, left_center_player, winning_score)  # creates the Othello gamestate
    othello.make_new_board()
    current_player = othello._first_player
    while True:
        _move_heading(othello, current_player)
        _move_process(othello, current_player)
        if othello.check_if_winner():
            _winning_display(othello)
            break
        else:
            current_player = othello.next_turn(current_player)


if __name__ == "__main__":
    run_othello()
        
        
        
