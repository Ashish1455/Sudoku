import tkinter as tk
from tkinter import ttk

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
    b1 = ttk.Button(frame, text='6')
    b1.grid(row=1, column=0)
    b = ttk.Button(frame, text='5')
    b.grid(row=1, column=1)
    b1 = ttk.Button(frame, text='4')
    b1.grid(row=1, column=2)
    b = ttk.Button(frame, text='3')
    b.grid(row=2, column=0)
    b1 = ttk.Button(frame, text='2')
    b1.grid(row=2, column=1)
    b = ttk.Button(frame, text='1')
    b.grid(row=2, column=2)

def board_view(cell_size):
    board = tk.Canvas(root, width=9 * cell_size, height=9 * cell_size)
    board.pack(side='left', padx=20)

    board.create_line(2, 0, 2, 9 * cell_size)
    board.create_line(0, 2, 9 * cell_size, 2)

    for i in range(1, 10):
        board.create_line(i * cell_size, 0, i * cell_size, 9 * cell_size)
        board.create_line(0, i * cell_size, 9 * cell_size, i * cell_size)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sudoku')
    root.state('zoomed')
    root.configure(background='skyblue')
    cell_size = 110
    board_view(cell_size)
    keypad(cell_size)
    root.mainloop()