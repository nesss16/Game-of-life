import tkinter as tk
class Interface :
    def __init__(self, grid, cell_size=30):
        self.grid = grid
        self.cell_size = cell_size
        self.window = tk.Tk()
        self.window.title("Game of life")
        self.canvas = tk.Canvas(self.window, width=self.grid.size * self.cell_size, height=self.grid.size * self.cell_size)
        self.canvas.pack()
        self.window.after(1000, self.update_and_draw)
        self.window.mainloop()

    def draw_grid(self):
        self.canvas.delete("all")
        for row in range(self.grid.size):
            for col in range(self.grid.size):
                x0, y0 = col * self.cell_size, row * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                color = "black" if self.grid.cells[row][col].is_alive() else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="grey")

    def update_and_draw(self):
        self.grid.update()
        self.draw_grid()
        self.window.after(1000, self.update_and_draw)
