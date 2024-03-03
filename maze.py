from geometry import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                cell = Cell(self._win)
                self._cells[i].append(cell)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1 + i * self._cell_width
        x2 = x1 + self._cell_width
        y1 = self._y1 + j * self._cell_height
        y2 = y1 + self._cell_height

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.001)