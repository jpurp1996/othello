# James Purpura 88625456

# othello_gui.py


import tkinter
import othello_logic

DIALOG_FONT = ("Helvetica", 20)
LINE_COLOR = "#003B46"
DEFAULT_FONT = ("Helvetica", 30)

class OthelloDialog:
    def __init__(self):
        self._dialog_window = tkinter.Tk()
        self._dialog_window.wm_title("OTHELLO FULL OPTIONS")

        heading_label = tkinter.Label(
            master = self._dialog_window, text = "OTHELLO FULL OPTIONS",
            font = DEFAULT_FONT)

        heading_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        
### Rows 
        
        row_label = tkinter.Label(
            master = self._dialog_window, text = "Number of Rows:",
            font = DIALOG_FONT)

        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_label_spinbox = tkinter.Spinbox(
            master  = self._dialog_window, font = DIALOG_FONT,
            from_ = 4, to = 16, width = 3,
            increment = 2, state = "readonly")

        self._row_label_spinbox.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W)

        
### Columns 
        
        column_label = tkinter.Label(
            master = self._dialog_window, text = "Number of Columns:",
            font = DIALOG_FONT)

        column_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._column_label_spinbox = tkinter.Spinbox(
            master  = self._dialog_window, font = DIALOG_FONT,
            from_ = 4, to = 16, width = 3,
            increment = 2, state = "readonly")

        self._column_label_spinbox.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W)

### First Player

        first_player_label = tkinter.Label(
            master = self._dialog_window, text = "First Player:",
            font = DIALOG_FONT)

        first_player_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        first_player_frame = tkinter.Frame(master = self._dialog_window)
        
        first_player_frame.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.S)

        self._first_player_var = tkinter.StringVar()
        self._first_player_var.set("B")

        self._first_player_b_radiobutton = tkinter.Radiobutton(
            master = first_player_frame, value = "B", variable = self._first_player_var,
            text = "B", font = DIALOG_FONT)

        self._first_player_b_radiobutton.grid(row = 0, column = 0, padx = 10, pady = 10)

        self._first_player_w_radiobutton = tkinter.Radiobutton(
            master = first_player_frame, value = "W", variable = self._first_player_var,
            text = "W", font = DIALOG_FONT)

        self._first_player_w_radiobutton.grid(row = 0, column = 1, padx = 10, pady = 10)

### Center Left Player

        center_left_player_label = tkinter.Label(
            master = self._dialog_window, text = "Center Left Player:",
            font = DIALOG_FONT)

        center_left_player_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        center_left_player_frame = tkinter.Frame(master = self._dialog_window)
        
        center_left_player_frame.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.S)

        self._center_left_var = tkinter.StringVar()
        self._center_left_var.set("B")
        
        self._center_left_player_b_radiobutton = tkinter.Radiobutton(
            master = center_left_player_frame, value = "B", variable = self._center_left_var,
            text = "B", font = DIALOG_FONT)

        self._center_left_player_b_radiobutton.grid(
            row = 0, column = 0, padx = 10, pady = 10)

        self._center_left_player_w_radiobutton = tkinter.Radiobutton(
            master = center_left_player_frame, value = "W", variable = self._center_left_var,
            text = "W", font = DIALOG_FONT)

        self._center_left_player_w_radiobutton.grid(
            row = 0, column = 1, padx = 10, pady = 10)

### Winning Score
        
        winning_score_label = tkinter.Label(
            master = self._dialog_window, text = "Winning Number of Disks:",
            font = DIALOG_FONT)

        winning_score_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        winning_score_frame = tkinter.Frame(master = self._dialog_window)
        
        winning_score_frame.grid(
            row = 5, column = 1, padx = 10, pady = 1,
            sticky = tkinter.S)

        self._winning_score_var = tkinter.StringVar()
        self._winning_score_var.set(">")
        
        self.winning_score_greater_radiobutton = tkinter.Radiobutton(
            master = winning_score_frame, value = ">", variable = self._winning_score_var,
            text = ">", font = DIALOG_FONT)

        self.winning_score_greater_radiobutton.grid(
            row = 0, column = 0, padx = 10, pady = 10)

        self.winning_score_fewer_radiobutton = tkinter.Radiobutton(
            master = winning_score_frame, value = "<", variable = self._winning_score_var,
            text = "<", font = DIALOG_FONT)

        self.winning_score_fewer_radiobutton.grid(
            row = 0, column = 1, padx = 10, pady = 10)

### OK Button

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.S + tkinter.E)

        ok_button = tkinter.Button(
            master = button_frame, text = "OK", font = DIALOG_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = "Cancel", font = DIALOG_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._ok_clicked = False
        self._rows = 0
        self._columns = ""
        self._first_player = ""
        self._center_left_player = ""
        self._winning_score = ""

    def show(self) -> None:
        """Hands over control to the dialog window"""
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_rows(self) -> str:
        return self._rows

    def get_columns(self) -> str:
        return self._columns

    def get_first_player(self) -> str:
        return self._first_player

    def get_center_left_player(self) -> str:
        return self._center_left_player

    def get_winning_score(self) -> str:
        return self._winning_score

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._rows = self._row_label_spinbox.get()
        self._columns = self._column_label_spinbox.get()
        self._first_player = self._first_player_var.get()
        self._center_left_player = self._center_left_var.get()
        self._winning_score = self._winning_score_var.get()
        self._dialog_window.destroy()

    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()
        

                
class OthelloApp:
    def __init__(self, othello: othello_logic.OthelloState):
        self._othello = othello
        self._columns = self._othello.columns()
        self._rows = self._othello.rows()
        self._height = 600
        self._width = 600
        self._column_width = self._width/self._columns
        self._row_height = self._height/self._rows

        self._current_player = self._othello.first_player()
        self._board = self._othello.make_new_board()

        self._root_window = tkinter.Tk()
        self._root_window.wm_title("OTHELLO FULL")

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = self._width, height = self._height,
            background = "#C4DFE6")

        self._canvas_border = self._draw_border()
        self._row_border = self._draw_rows()
        self._column_border = self._draw_columns()

        
        self._canvas.bind("<Button-1>", self._on_canvas_clicked)
        self._canvas.bind("<Configure>", self._on_canvas_resized)

        self._heading_text = tkinter.StringVar()
        self._heading_text.set("OTHELLO FULL")

        heading_label = tkinter.Label(
            master = self._root_window, textvariable = self._heading_text,
            font = DEFAULT_FONT)
        
        heading_label.grid(
            row = 0, column = 0, padx = 1, pady = 1,
            sticky = tkinter.S)

        self._canvas.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._boxscore_text = tkinter.StringVar()
        self._boxscore_text.set("Turn: " + self._current_player +  "\n B: 2 \t W: 2")

        move_label = tkinter.Label(
            master = self._root_window, textvariable = self._boxscore_text,
            font = DEFAULT_FONT)

        move_label.grid(
            row = 2, column = 0, padx = 2, pady = 2,
            sticky = tkinter.N)

        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 0)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        self._root_window.mainloop()

### Drawing Borders (Rows, Columns)
        
    def _line_thickness(self) -> float:
        """Return a desired thickness for lines (based on average of board
        width and height"""
        height_width_average = (self._column_width+self._row_height)/2
        thickness = (height_width_average/25)
        return thickness
        
    
    def _draw_border(self) -> None:
        """Draws the border around the canvas"""
        thickness = self._line_thickness()
        self._canvas.create_rectangle(      
            thickness, thickness, self._width-thickness, self._height-thickness,
            outline = LINE_COLOR,
            width = thickness)

    def _draw_rows(self) -> None:
        """Draws the rows"""
        thickness = self._line_thickness()
        for row in range(self._rows):       
            multiplier = row + 1
            self._canvas.create_line(
                0, multiplier * self._row_height,
                self._width, multiplier * self._row_height,
                fill = LINE_COLOR,
                width = thickness)

    def _draw_columns(self) -> None:
        """Draws the columns"""
        thickness = self._line_thickness()
        for column in range(self._columns):
            multiplier = column + 1
            self._canvas.create_line(
                multiplier * self._column_width, 0,
                multiplier * self._column_width, self._height,
                fill = LINE_COLOR,
                width = thickness)

### Finding Boundaries

    def _row_boundaries(self) -> [float]:
        """Return a list representing the bottom boundary for each row.
        Essentially returns the y-coordinate of the rows"""
        row_boundaries = []
        for row in range(self._rows):
            multiplier = row + 1
            row_boundaries.append(multiplier*self._row_height)
        return row_boundaries

    def _column_boundaries(self) -> [float]:
        """Return a list representing the right boundary for each column.
        Essentially returns the x-coordinate of the columns"""
        column_boundaries = []
        for column in range(self._columns):
            multiplier = column + 1
            column_boundaries.append(multiplier*self._column_width)
        return column_boundaries

    def _find_nearest_rows(self, pixel_y: int) -> (float,float):
        """Given a point, return the pixel coordinates of the rows in which
        this point lies"""
        bounds = self._row_boundaries()
        for bound in bounds:
            if pixel_y - bound <= 0:
                return (bound - self._row_height, bound)

    def _find_nearest_columns(self, pixel_x: int) -> (float, float):
        """Given a point, return the pixel coordinates of the columns in which
        this point lies"""
        bounds = self._column_boundaries()
        for bound in bounds:
            if pixel_x - bound <= 0:
                return (bound - self._column_width, bound)

            
### Drawing Ovals
            
    def _player_color(self, player: str) -> str:
        """Return the color of the player"""
        if player == "B":
            return "black"
        else:
            return "white"

    def _draw_oval_in_box(self, pixel_x: float, pixel_y: float, color: str) -> None:
        """Given a point, draw an oval within the box of this point"""
        column_boundaries = self._find_nearest_columns(pixel_x)
        row_boundaries = self._find_nearest_rows(pixel_y)
        thickness = self._line_thickness()
        padding = 3 * thickness

        x_start, x_stop = column_boundaries
        y_start, y_stop = row_boundaries

        self._canvas.create_oval(
            x_start+padding, y_start+padding, x_stop-padding, y_stop-padding,
            fill = color,
            outline = "black",
            width = thickness)    
        
### Handling Clicks, Resizing

    def _from_coordinates_to_box(self, pixel_x, pixel_y) -> (int, int):
        """Given pixel coordinates, return the (row, column)
        in which spot occurs"""
        x_end = self._find_nearest_columns(pixel_x)[1]
        y_end = self._find_nearest_rows(pixel_y)[1]

        column = int(x_end/self._column_width)
        row = int(y_end/self._row_height)

        return (row - 1, column - 1)

    def _from_box_to_coordinates(self, box_tuple: (int, int)) -> (float, float):
        """Given the (row, column) of a box, return the pixel in which this
        box occurs"""
        row, column = box_tuple
        row += 1
        column += 1

        x_end = self._column_width * column
        y_end = self._row_height * row

        return (x_end, y_end)

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        """When user resizes canvas, redraw all items on canvas"""

        self.board_view()
            
            
    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        """When user clicks canvas, user calls this method"""
        move_box = self._move_process(event.x, event.y, self._current_player)
        if self._othello.player_move(self._current_player, move_box):
            self.board_view()
            black_score = str(self._othello.calculate_score("B"))
            white_score = str(self._othello.calculate_score("W"))
            self._boxscore_text.set("Turn: " + self._current_player +
                                    "\n B: " + black_score +
                                    "\t W: " + white_score)

            if self._othello.check_if_winner():
                winner = self._othello.winner()
                self._boxscore_text.set("WINNER: " + winner +
                                        "\n B: " + black_score +
                                        "\t W: " + white_score)
                
            else:
                self._current_player = self._othello.next_turn(self._current_player)
                self._boxscore_text.set("Turn: " + self._current_player +
                                        "\n B: " + black_score +
                                        "\t W: " + white_score)

### Handling Board
                
    def board_view(self) -> None:
        """Displays the board"""
        self._canvas.delete(tkinter.ALL)
        self._height = self._canvas.winfo_height()
        self._width = self._canvas.winfo_width()
        self._canvas_border = self._draw_border()
        self._row_border = self._draw_rows()
        self._column_border = self._draw_columns()
        self._column_width = self._width/self._columns
        self._row_height = self._height/self._rows
        for row in range(self._rows):
            for column in range(self._columns):
                space = self._board[row][column]
                if space != 0:
                    color = self._player_color(space)
                    x_end, y_end = self._from_box_to_coordinates((row, column))
                    self._draw_oval_in_box(x_end, y_end, color)
               
    def _move_process(self, pixel_x, pixel_y, player: str) -> (float, float):
        """Print the board and return the box in which the player clicks"""
        self.board_view()
        move_box = self._from_coordinates_to_box(pixel_x, pixel_y)
        return move_box

def run_othello() -> None:
    """The game method"""
    dialog = OthelloDialog()
    dialog.show()
    if dialog.get_rows() != 0:
        rows = int(dialog.get_rows())
        columns = int(dialog.get_columns())
        first_player = dialog.get_first_player()
        center_left_player = dialog.get_center_left_player()
        winning_score = dialog.get_winning_score()
        
        othello = othello_logic.OthelloState(
            rows, columns, first_player, center_left_player, winning_score)
        game = OthelloApp(othello)
        game.start()
    
if __name__ == "__main__":
    run_othello()
