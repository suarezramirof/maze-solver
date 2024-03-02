from window import Window
from geometry import Line, Point

def main():
    win = Window(800, 600)
    line1 = Line(Point(10, 10), Point(200, 250))
    line2 = Line(Point(500, 50), Point(200, 750))
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()

main()