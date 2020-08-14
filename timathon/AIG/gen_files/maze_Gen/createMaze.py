from PIL import Image
from PIL import ImageDraw
import mazeGen


def createMaze(x: int, y: int):
    instance = mazeGen.MazeGen(x, y)
    return instance.generate()


def createImage(maze: list, *, px=30, width=4):
    rows, cols = len(maze), len(maze[0])

    image = Image.new("RGB", (cols * px, rows * px), color=(255, 255, 255))
    drawer = ImageDraw.Draw(image)
    filler = (255, 0, 0)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j]["N"] in [1, -1]:
                drawer.line([(px*j, px*i), (px*j+px-1, px*i)], fill=filler, width=width)
            if maze[i][j]["E"] in [1, -1]:
                drawer.line([(px*j+px-1, px*i), (px*j+px-1, px*i+px-1)], fill=filler, width=width)
            if maze[i][j]["S"] in [1, -1]:
                drawer.line([(px*j, px*i+px-1), (px*j+px-1, px*i+px-1)], fill=filler, width=width)
            if maze[i][j]["W"] in [1, -1]:
                drawer.line([(px*j, px*i), (px*j, px*i+px-1)], fill=filler, width=width)
            if maze[i][j]["N"] in [2]:
                drawer.line([(px*j, px*i), (px*j+px-1, px*i)], fill=(0, 0, 255), width=width)
            if maze[i][j]["S"] in [2]:
                drawer.line([(px*j, px*i+px-1), (px*j+px-1, px*i+px-1)], fill=(0, 0, 255), width=width)

    image.save("maze.png")


def run(x: int, y: int, px=30):
    maze = createMaze(x, y)
    createImage(maze, px=px)


if __name__ == "__main__":
    run(20, 20)
