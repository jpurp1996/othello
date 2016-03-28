# James Purpura 

# othello_logic 


class OthelloState:
    def __init__(self, rows: int, columns: int, first_player: str, left_center_player: str, winning_score: str):
        self._rows = rows
        self._columns = columns
        self._first_player = first_player
        self._left_center_player = left_center_player
        self._winning_score = winning_score
        self._board = []

##### Foundations

    def rows(self) -> int:
        """Return the number of rows in the board"""
        return self._rows

    def columns(self) -> int:
        """Return the number of columns in the board"""
        return self._columns

    def first_player(self) -> str:
        """Return the first player"""
        return self._first_player

    def left_center_player(self) -> str:
        """Return the left center player"""
        return self._left_center_player

    def board(self) -> [list]:
        """Return the game board"""
        return self._board


    def winning_score(self) -> str:
        """Return the winning score: > or <"""
        return self._winning_score


    
    def _switch_player(self, player: str) -> str:
        """Return the player other than the player given"""
        if player == "B":
            return "W"
        else:
            return "B"
        
    def make_new_board(self) -> [[str]]:
        """Return a new board for the start of the game"""
        for row in range(self._rows):
            this_row = []
            for column in range(self._columns):
                this_row.append(0)
            self._board.append(this_row)
        self._board[int(self._rows/2)-1][int(self._columns/2)-1] = self._left_center_player
        self._board[int(self._rows/2)-1][int((self._columns/2))] = self._switch_player(self._left_center_player)
        self._board[int((self._rows/2))][int(self._columns/2)-1] = self._switch_player(self._left_center_player)
        self._board[int((self._rows/2))][int((self._columns/2))] = self._left_center_player
        return self._board
    
    def _other_player(self, player: str, location: str) -> bool:
        """Return True if the other player holds the given location"""
        return (location != 0 and location != player)
        
    def calculate_score(self, player: str) -> int:
        """Return the number of disks on the board of the given player on the board"""
        score = 0
        for row in range(self._rows):
            for column in range(self._columns):
                if self._board[row][column] == player:
                    score += 1
        return score

    def _calculate_total_score(self) -> int:
        """Return the total number of disks on the board"""
        black_score = self.calculate_score("B")
        white_score = self.calculate_score("W")
        return black_score + white_score

### Flipping Tuples (Creates a line in the form of [tuples] for flipping)
        
    def _horizontal_flipping_tuples(self, row: int, start_column: int, stop_column: int) -> [tuple]:
        """Return a list containing the horizontal spaces to be flipped"""
        list_of_flipping_tuples = []
        current_column = start_column
        if start_column < stop_column:
            while current_column <= stop_column:
                list_of_flipping_tuples.append((row, current_column))
                current_column = current_column + 1
        if start_column > stop_column:
            while current_column >= stop_column:
                list_of_flipping_tuples.append((row, current_column))
                current_column = current_column - 1
        return list_of_flipping_tuples

    def _vertical_flipping_tuples(self, start_row: int, column: int, stop_row: int) -> [tuple]:
        """Return a list containing the vertical spaces to be flipped"""
        list_of_flipping_tuples = []
        current_row = start_row
        if start_row < stop_row:
            while current_row <= stop_row:
                list_of_flipping_tuples.append((current_row, column))
                current_row = current_row + 1
        if start_row > stop_row:
            while current_row >= stop_row:
                list_of_flipping_tuples.append((current_row, column))
                current_row = current_row - 1
        return list_of_flipping_tuples

    def _diagonal_flipping_tuples(self, start_row: int, start_column: int, stop_row: int, stop_column: int) -> [tuple]:
        """Return a list containing thevertical spaces to be flipped"""
        list_of_flipping_tuples = []
        current_row = start_row
        current_column = start_column
        if start_row < stop_row and current_column < stop_column: # down right
            while current_row <= stop_row:
                list_of_flipping_tuples.append((current_row, current_column))
                current_row = current_row + 1
                current_column = current_column + 1
        if start_row < stop_row and current_column > stop_column:
            while current_row <= stop_row:
                list_of_flipping_tuples.append((current_row, current_column))
                current_row = current_row + 1
                current_column = current_column - 1
        if start_row > stop_row and current_column < stop_column:
            while current_row >= stop_row:
                list_of_flipping_tuples.append((current_row, current_column))
                current_row = current_row - 1
                current_column = current_column + 1
        if start_row > stop_row and current_column > stop_column:
            while current_row >= stop_row:
                list_of_flipping_tuples.append((current_row, current_column))
                current_row = current_row - 1
                current_column = current_column - 1
        return list_of_flipping_tuples
                       
### Move/Win Checks, Flipping, 

    def _horizontal_moves(self, player: str, check: bool) -> [tuple]:
        """If check is True, return a list of all possible moves in the horizontal direction in the form
        (row, column) for the given player
        If check is False, returns a list of the spaces to be flipped"""
        possible_moves = []
        for row in range(self._rows):
            for column in range(self._columns):
                if self._board[row][column] == player:
                    check_column = column
                    while (check_column-2) >= 0 and self._other_player(player, self._board[row][check_column-1]): #checks left 
                        if self._board[row][check_column-2] == 0:
                            if check:
                                possible_moves.append((row, check_column-2)) 
                            else:
                                possible_moves.append(self._horizontal_flipping_tuples(row, column, check_column-2))
                        check_column = check_column - 1
                if self._board[row][column] == player:
                    check_column = column
                    while (check_column+2) <= (self._columns-1) and self._other_player(player, self._board[row][check_column+1]): #checks right 
                        if self._board[row][check_column+2] == 0:
                            if check:
                                possible_moves.append((row, check_column+2)) 
                            else:
                                possible_moves.append(self._horizontal_flipping_tuples(row, column, check_column+2))
                        check_column = check_column + 1
        return possible_moves
       
    def _vertical_moves(self, player: str, check: bool) -> [tuple]:
        """If check is true, returns a list of all possible moves in the vertical direction in the form
         (row, column) for the given player
        If check is False, return a list of the spaces to be flipped"""
        possible_moves = []
        for row in range(self._rows):
            for column in range(self._columns):
                if self._board[row][column] == player:
                    check_row = row
                    while (check_row-2) >= 0 and self._other_player(player, self._board[check_row-1][column]): #checks up
                        if self._board[check_row-2][column] == 0:
                            if check:
                                possible_moves.append((check_row-2, column)) 
                            else:
                                possible_moves.append(self._vertical_flipping_tuples(row, column, check_row-2))
                        check_row = check_row - 1
                if self._board[row][column] == player:
                    check_row = row
                    while(check_row+2) <= (self._rows-1) and self._other_player(player, self._board[check_row+1][column]): #checks down
                        if self._board[check_row+2][column] == 0:
                            if check:
                                possible_moves.append((check_row+2, column)) 
                            else:
                                possible_moves.append(self._vertical_flipping_tuples(row, column, check_row+2))
                        check_row = check_row + 1
        return possible_moves


    def _diagonal_moves(self, player: str, check: bool) -> [tuple]:
        """If check is true, return a list of all possible moves in the diagonal direction in the form
        (row, column) for the given player
        If check is False, return a list of the spaces to be flipped"""
        possible_moves = []
        for row in range(self._rows):
            for column in range(self._columns):
                if self._board[row][column] == player:
                    check_row = row
                    check_column = column
                    while (check_row-2) >= 0 and (check_column-2) >= 0 and self._other_player(player, self._board[check_row-1][check_column-1]): #checks up and left
                        if self._board[check_row-2][check_column-2] == 0:
                            if check:
                                possible_moves.append((check_row-2, check_column-2)) 
                            else:
                                possible_moves.append(self._diagonal_flipping_tuples(row, column, check_row-2, check_column-2))
                        check_row = check_row - 1
                        check_column = check_column - 1
                if self._board[row][column] == player:
                    check_row = row
                    check_column = column
                    while (check_row+2) <= (self._rows-1) and (check_column+2) <= (self._columns-1) and self._other_player(player, self._board[check_row+1][check_column+1]):  #checks down and right
                        if self._board[check_row+2][check_column+2] == 0:
                            if check:
                                possible_moves.append((check_row+2, check_column+2))
                            else:
                                possible_moves.append(self._diagonal_flipping_tuples(row, column, check_row+2, check_column+2))
                        check_row = check_row + 1
                        check_column = check_column + 1
                if self._board[row][column] == player:
                    check_row = row
                    check_column = column
                    while (check_row+2) <= (self._rows-1) and (check_column-2) >= 0 and self._other_player(player, self._board[check_row+1][check_column-1]): #checks down and left
                        if self._board[check_row+2][check_column-2] == 0:
                            if check:
                                possible_moves.append((check_row+2, check_column-2))
                            else:
                                possible_moves.append(self._diagonal_flipping_tuples(row, column, check_row+2, check_column-2))
                        check_row = check_row + 1
                        check_column = check_column - 1
                if self._board[row][column] == player:
                    check_row = row
                    check_column = column
                    while (check_row-2) >= 0 and (check_column+2) <= (self._columns-1) and self._other_player(player, self._board[check_row-1][check_column+1]): #checks diagonal up and right
                        if self._board[check_row-2][check_column+2] == 0:
                            if check:
                                possible_moves.append((check_row-2, check_column+2))
                            else:
                                possible_moves.append(self._diagonal_flipping_tuples(row, column, check_row-2, check_column+2))
                        check_row = check_row - 1
                        check_column = check_column + 1
                
        return possible_moves

    def _player_has_valid_moves(self, player: str) -> bool:
        """Return True if the given player has any valid moves"""
        list_of_possible_moves = self._horizontal_moves(player, True) + self._vertical_moves(player, True) + self._diagonal_moves(player,True)
        return len(list_of_possible_moves) > 0

    def _flip(self, player: str, move: tuple) -> [list]:
        """Return a new game board with flipped disks"""
        all_possible_flips = self._horizontal_moves(player, False) + self._vertical_moves(player, False) + self._diagonal_moves(player, False)
        places_to_flip = []
        
        for line_of_flips in all_possible_flips:
            if len(line_of_flips) >0 and line_of_flips[-1] == move:
                places_to_flip.append(line_of_flips)

        for line_of_flip in places_to_flip:
            for flip in line_of_flip:
                row = flip[0]
                column = flip[1]
                self._board[row][column] = player
                
        
    def check_if_winner(self) -> bool:
        """Return True the game has a winner"""
        total_spaces = self._rows * self._columns
        if self._calculate_total_score == total_spaces:
            return True
        elif not self._player_has_valid_moves("B") and not self._player_has_valid_moves("W"):
            return True
        else:
            return False

    def winner(self) -> str:
        black_score = self.calculate_score("B")
        white_score = self.calculate_score("W")
        if self.winning_score() == ">":
            if black_score > white_score:
                return "B"
            elif white_score > black_score:
                return "W"
            else:
                return "TIE"
        else:
            if black_score < white_score:
                return "B"
            elif white_score < black_score:
                return "W"
            else:
                return "TIE"
### Moves
        
    def next_turn(self, player) -> str:
        """Return the opposing player if that player has valid moves.
        Else, returns current player"""
        other_player = self._switch_player(player)
        if self._player_has_valid_moves(other_player):
            return other_player
        else:
            return player
        


    def player_move(self, player: str, move_tuple: (int, int)) -> bool:
        """If move_tuple parameter is valid, changes board accordingly.
        Else, return False"""
        possible_moves = self._horizontal_moves(player, True) + self._vertical_moves(player, True) + self._diagonal_moves(player, True)
        if move_tuple in possible_moves:
            self._flip(player, move_tuple)
            return True
        else:
            return False

                
            
            
            
        
                        



   




