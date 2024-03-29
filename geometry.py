class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack(fill="both", expand=1)

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        color = "black"
        if not self.has_left_wall:
            color = "#d9d9d9"
        line_left = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line_left, color)
        
        if self.has_right_wall:
            color = "black"
        else:
            color = "#d9d9d9"
        line_right = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line_right, color)

        if self.has_top_wall:
            color = "black"
        else:
            color = "#d9d9d9"
        line_top = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line_top, color)

        if self.has_bottom_wall:
            color = "black"
        else:
            color = "#d9d9d9"
        line_bottom = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line_bottom, color)

    def draw_move(self, to_cell, undo=False):
        if self._win == None:
            return
        if not undo:
            line_color = "red"
        else:
            line_color = "gray"
        first_center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        second_center = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        line = Line(first_center, second_center)
        self._win.draw_line(line, line_color)

    