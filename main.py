from window import Window
from geometry import Line, Point, Cell

def main():
    win = Window(800, 600)
    line1 = Line(Point(10, 10), Point(200, 250))
    line2 = Line(Point(500, 50), Point(200, 750))
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    cell1 = Cell(win)
    cell1.draw(200,200,250,250)

    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(100,200,150,250)

    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.draw(100, 250, 150, 300)

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    win.wait_for_close()

main()