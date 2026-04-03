import matplotlib.pyplot as plt

def Round(a):
    return int(a + 0.5)

def DDA(xa, ya, xb, yb):
    dx = xb - xa
    dy = yb - ya

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xinc = dx / float(steps)
    yinc = dy / float(steps)

    x = xa
    y = ya

    x_points = [Round(x)]
    y_points = [Round(y)]

    for i in range(steps):
        x += xinc
        y += yinc
        x_points.append(Round(x))
        y_points.append(Round(y))

    return x_points, y_points


def draw_line(ax, xa, ya, xb, yb, color):
    x_pts, y_pts = DDA(xa, ya, xb, yb)
    ax.plot(x_pts, y_pts, marker='o', markersize=2, color=color)


def shape(xa, ya, xb, yb):
    fig, ax = plt.subplots()

    draw_line(ax, xa, ya, xa, yb, 'black')
    draw_line(ax, xa, yb, xb, yb, 'black')
    draw_line(ax, xb, yb, xb, ya, 'black')
    draw_line(ax, xb, ya, xa, ya, 'black')

    draw_line(ax, xa, (ya+yb)//2, (xa+xb)//2, yb, 'red')
    draw_line(ax, (xa+xb)//2, yb, xb, (ya+yb)//2, 'red')
    draw_line(ax, xb, (ya+yb)//2, (xa+xb)//2, ya, 'red')
    draw_line(ax, (xa+xb)//2, ya, xa, (ya+yb)//2, 'red')

    x1, y1 = xa, (ya+yb)//2
    x2, y2 = (xa+xb)//2, yb
    x3, y3 = xb, (ya+yb)//2
    x4, y4 = (xa+xb)//2, ya

    draw_line(ax, (x1+x2)//2, (y1+y2)//2, (x2+x3)//2, (y2+y3)//2, 'blue')
    draw_line(ax, (x2+x3)//2, (y2+y3)//2, (x3+x4)//2, (y3+y4)//2, 'blue')
    draw_line(ax, (x3+x4)//2, (y3+y4)//2, (x4+x1)//2, (y4+y1)//2, 'blue')
    draw_line(ax, (x4+x1)//2, (y4+y1)//2, (x1+x2)//2, (y1+y2)//2, 'blue')

    ax.set_title("DDA Shape Drawing (Matplotlib)")
    ax.set_aspect('equal')
    ax.grid(True)

    plt.show()

xa = int(input("Enter Xa: "))
ya = int(input("Enter Ya: "))
xb = int(input("Enter Xb: "))
yb = int(input("Enter Yb: "))

shape(xa, ya, xb, yb)