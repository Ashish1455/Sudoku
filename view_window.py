import tkinter as tk
from idlelib import editor
from rules import normal_rules
from Sudoku_solver import solveSudoku
from color_theme import *



selected = None
position = (0, 0)
labels = {}
mode = 'play'



''' Highlight cells '''
def move(e):
    global selected
    global position
    if e.keysym == 'Left':
        if position[1] > 0:
            cell_no = position[0]*9 + position[1]
            highlight(cell_no)
        else:
            cell_no = position[0]*9 + 9
            highlight(cell_no)
    if e.keysym == 'Right':
        if position[1] < 8:
            cell_no = position[0]*9 + position[1] + 2
            highlight(cell_no)
        else:
            cell_no = position[0]*9 + 1
            highlight(cell_no)
    if e.keysym == 'Up':
        if position[0] > 0:
            cell_no = position[0]*9 + position[1] - 8
            highlight(cell_no)
        else:
            cell_no = 8*9 + position[1] + 1
            highlight(cell_no)
    if e.keysym == 'Down':
        if position[0] < 8:
            cell_no = position[0]*9 + position[1] + 10
            highlight(cell_no)
        else:
            cell_no = position[1] + 1
            highlight(cell_no)



def highlight(name):
    global selected
    global position

    # Deselect previous
    if selected:
        labels[selected].config(bg=CELL_BG if (position[0]//3 + position[1]//3)%2 == 0 else CELL_BG_ALT)

    # Highlight clicked one
    position = ((name-1)//9, (name-1)%9)
    selected = name
    labels[name].config(bg=CELL_SELECTED)



def on_click(event):
    name = next(k for k, v in labels.items() if v == event.widget)    # find which label was clicked
    highlight(name)



def enter_digit(d, board):
    global selected
    global position
    try:
        if d.keysym.isdigit():
            d = int(d.keysym)
        else:
            move(d)
            return
    except AttributeError:
        pass
    if selected and labels[selected].cget('state') == 'normal':
        if labels[selected].cget('text') == d:
            labels[selected].config(text='')
            board[position[0]][position[1]] = 0
        elif normal_rules(board, position[0], position[1], d):
            board[position[0]][position[1]] = d
            labels[selected].config(text=d, fg=INPUT_FG)
        else:
            labels[selected].config(text=d, fg=ERROR_FG, bg=CEEL_ERROR_BG)
            board[position[0]][position[1]] = d



def check(root, board):
    b = [row[:] for row in board]
    x = solveSudoku(b)
    mess = tk.Toplevel(root)
    mess.geometry(f'200x50+{(root.winfo_screenwidth()-300)//2}+{(root.winfo_screenheight()-300)//2}')
    mess.title('')
    mess.config(bg=FRAME_BG)
    if board == x:
        text = "SOLVED"
        fg = INPUT_FG
        bg = CELL_BG
    else:
        text = "UNSOLVED"
        fg = ERROR_FG
        bg = "#F5DDD8"
    label = tk.Label(mess, text=text, font=('Arial', 24), bg='white', background=bg, fg=fg, padx=16, pady=8)
    label.pack()



def keypad(root, board):
    frame = tk.LabelFrame(root, text='KeyPad', bg=KEYPAD_BG, fg=KEYPAD_FG, font=("Consolas", 14, "bold"), labelanchor='n')
    frame.pack(side='bottom', anchor='sw', padx=10, pady=31)

    digits = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    for row_idx, row in enumerate(digits):
        for col_idx, digit in enumerate(row):
            btn = tk.Button(frame, text=str(digit), width=3, bg=KEYPAD_BTN_BG, fg=KEYPAD_BTN_FG, activebackground=KEYPAD_BTN_ACTIVE, activeforeground=KEYPAD_BTN_ACTIVE_FG, font=('Consolas', 40), cursor="hand2", command=lambda d=digit: enter_digit(d, board))
            btn.grid(row=2*row_idx, column=col_idx, rowspan=2)

    btn = tk.Button(frame, text="🗸", font=('Consolas', 18), width=5, bg=KEYPAD_CHECK_BG, fg=KEYPAD_CHECK_FG, command=lambda b=board: check(root, b))
    btn.grid(row=0, column=3, rowspan=1, ipady=3)

    editor_btn = tk.Button(frame, text='Edit Mode', font=('Consolas', 20), width=24, bg=KEYPAD_CHECK_BG, fg=KEYPAD_CHECK_FG)
    editor_btn.config(command=lambda : editor(editor_btn))
    editor_btn.grid(row=7, column=0, columnspan=4)



def board_view(root, cell_size, board):
    board_display = tk.Canvas(root, width=9 * cell_size + 4, height=9 * cell_size + 4, highlightbackground=FRAME_BORDER, highlightthickness=2)
    board_display.pack(side='left', padx=20)

    for i in range(9):
        for j in range(9):
            cell_no = i * 9 + j + 1
            board_display.create_rectangle(i * cell_size+4, j * cell_size+4, (i+1) * cell_size+4, (j+1) * cell_size+4, tags=f'cell_{cell_no}', outline=GRID_LINE_THIN, width=2)
    # border
    for k in range(4):
        pos = k * 3 * cell_size
        board_display.create_line(pos+4, 4, pos+4, 9 * cell_size+4, width=4, fill=GRID_LINE_THICK)
        board_display.create_line(4, pos+4, 9 * cell_size+4, pos+4, width=4, fill=GRID_LINE_THICK)
    # Label on rectangle
    label_name = [i for i in range(1, 82)]
    global labels
    for i in range(9):
        for j in range(9):
            name = label_name[i*9 + j]
            labels[name] = tk.Label(root, text=board[i][j] if board[i][j] != 0 else ' ', bg=CELL_BG if (i//3 + j//3)%2 == 0 else CELL_BG_ALT, disabledforeground=INPUT_FG, justify='center', state='disabled' if board[i][j] != 0 else 'normal', font=('Consolas', (3*cell_size)//4))
            board_display.create_window((j * cell_size)+6, (i * cell_size)+6, window=labels[name], anchor='nw', width=cell_size-4, height=cell_size-4)
            labels[name].bind("<Button-1>", lambda e: on_click(e))

    root.bind("<Key>", lambda d: enter_digit(d, board))




def editor(btn):
    global mode
    if mode == 'play':
        for i in range(1, 82):
            labels[i].config(state='normal')
        mode = 'edit'
        btn.config(relief='sunken')
    elif mode == 'edit':
        for i in range(1, 82):
            labels[i].config(state='disabled' if labels[i].cget('text') != '' else 'normal')
            mode = 'play'
            btn.config(relief='raised')

def run_window(board):
    root = tk.Tk()
    root.title('Sudoku')
    root.state('zoomed')
    root.configure(bg=ROOT_BG)
    cell_size = 110
    board_view(root, cell_size, board)
    keypad(root, board)
    root.mainloop()



if __name__ == '__main__':
    board1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    run_window(board1)