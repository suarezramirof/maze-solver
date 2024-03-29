from window import Window
from geometry import Line, Point, Cell
from maze import Maze

def main():
    window_width = 800
    window_height = 500
    win = Window(window_width, window_height)

    num_cols = 30
    num_rows = 20
    margin = 50
    cell_width = (window_width - margin * 2) / num_cols
    cell_height = (window_height - margin * 2) / num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_width, cell_height, win)
    maze.solve()

    win.wait_for_close()

main()