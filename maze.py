from geometry import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            dir = random.choice(to_visit)
            if i == dir[0]:
                if j < dir[1]:
                    self._cells[i][j].has_bottom_wall = False
                else:
                    self._cells[i][j].has_top_wall = False
            elif j == dir[1]:
                if i < dir[0]:
                    self._cells[i][j].has_right_wall = False
                else:
                    self._cells[i][j].has_left_wall = False
            self._draw_cell(i, j)
            self._break_walls_r(dir[0], dir[1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if i + 1 < self._num_cols and not self._cells[i][j].has_right_wall:
            if not self._cells[i + 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                result = self._solve_r(i + 1, j)
                if result:
                    return True
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if i > 0 and not self._cells[i][j].has_left_wall:
            if not self._cells[i - 1][j].visited:
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                result = self._solve_r(i - 1, j)
                if result:
                    return True
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if j + 1 < self._num_rows and not self._cells[i][j].has_bottom_wall:
            if not self._cells[i][j + 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                result = self._solve_r(i, j + 1)
                if result:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        if j > 0 and not self._cells[i][j].has_top_wall:
            if not self._cells[i][j - 1].visited:
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                result = self._solve_r(i, j - 1)
                if result:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        
        return False

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
        time.sleep(0.01)