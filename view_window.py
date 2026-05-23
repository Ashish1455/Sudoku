import tkinter as tk
from tkinter import ttk
from main import board

selected = None
position = None
labels = {}

def highlight(name):
    global selected
    global position

    # Deselect previous
    if selected:
        labels[selected].config(bg="white", fg="black")

    # Highlight clicked one
    position = ((name-1)//9, (name-1)%9)
    selected = name
    labels[name].config(bg="skyblue", fg="white")

def on_click(event, label_name):
    name = next(k for k, v in labels.items() if v == event.widget)    # find which label was clicked
    highlight(name)

def keypad(cell_size):
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 24), padding=(0, cell_size // 2))
    frame = ttk.LabelFrame(root, text='KeyPad')
    frame.pack(side='bottom', anchor='sw', padx=10, pady=31)

    b = ttk.Button(frame, text='7')
    b.grid(row=0, column=0)
    b1 = ttk.Button(frame, text='8')
    b1.grid(row=0, column=1)
    b = ttk.Button(frame, text='9')
    b.grid(row=0, column=2)
    b1 = ttk.Button(frame, text='4')
    b1.grid(row=1, column=0)
    b = ttk.Button(frame, text='5')
    b.grid(row=1, column=1)
    b1 = ttk.Button(frame, text='6')
    b1.grid(row=1, column=2)
    b = ttk.Button(frame, text='1')
    b.grid(row=2, column=0)
    b1 = ttk.Button(frame, text='2')
    b1.grid(row=2, column=1)
    b = ttk.Button(frame, text='3')
    b.grid(row=2, column=2)

def board_view(cell_size, board):
    board_display = tk.Canvas(root, width=9 * cell_size, height=9 * cell_size)
    board_display.pack(side='left', padx=20)

    board_display.create_rectangle(2, 2, cell_size, cell_size, tags=f'cell_{1}', fill='white')
    # first row
    for i in range(1, 9):
        cell_no = i + 1
        board_display.create_rectangle(i * cell_size, 2, (i+1) * cell_size, cell_size, tags=f'cell_{cell_no}', fill='white')
    # first column
    for i in range(1, 9):
        cell_no = i*9 + 1
        board_display.create_rectangle(2, i * cell_size, cell_size, (i+1) * cell_size, tags=f'cell_{cell_no}', fill='white')
    # rest of board
    for i in range(1, 9):
        for j in range(1, 9):
            cell_no = i * 9 + j + 1
            board_display.create_rectangle(i * cell_size, j * cell_size, (i+1) * cell_size, (j+1) * cell_size, tags=f'cell_{cell_no}', fill='white')
    # Label on rectangle
    label_name = [i for i in range(1, 82)]
    global labels
    for i in range(9):
        for j in range(9):
            name = label_name[i*9 + j]
            labels[name] = tk.Label(root, text=board[i][j] if board[i][j] != 0 else ' ', justify='center', font=('Consolas', (3*cell_size)//4))
            board_display.create_window((j * cell_size)+4, (i * cell_size)+4, window=labels[name], anchor='nw', width=cell_size-6, height=cell_size-6)
            labels[name].bind("<Button-1>", lambda e: on_click(e, label_name))

    ''' Highlight cells '''
    def move(e):
        global selected
        global position
        if e.keysym == 'Left':
            if position[1] > 0:
                cell_no = position[0]*9 + position[1]
                highlight(cell_no)
        if e.keysym == 'Right':
            if position[1] < 8:
                cell_no = position[0]*9 + position[1] + 2
                highlight(cell_no)
        if e.keysym == 'Up':
            if position[0] > 0:
                cell_no = position[0]*9 + position[1] - 8
                highlight(cell_no)
        if e.keysym == 'Down':
            if position[0] < 8:
                cell_no = position[0]*9 + position[1] + 10
                highlight(cell_no)

    root.bind("<Key>", move)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sudoku')
    root.state('zoomed')
    root.configure(background='skyblue')
    cell_size = 110
    board_view(cell_size, board)
    keypad(cell_size)
    root.mainloop()