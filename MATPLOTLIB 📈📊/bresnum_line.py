import matplotlib.pyplot as plt

def bresenham_line(xa, ya, xb, yb):
    x_points = []
    y_points = []

    dx = xb - xa
    dy = yb - ya

    flag = 0

    if abs(dx) < abs(dy):
        xa, ya = ya, xa
        xb, yb = yb, xb
        dx = xb - xa
        dy = yb - ya
        flag = 1

    d = 2 * abs(dy) - abs(dx)

    if dx > 0:
        c, r, end = xa, ya, xb
    else:
        c, r, end = xb, yb, xa

    if flag == 0:
        x_points.append(c)
        y_points.append(r)
    else:
        x_points.append(r)
        y_points.append(c)

    while c < end:
        if d < 0:
            c += 1
            d += 2 * abs(dy)
        else:
            c += 1
            if dx * dy > 0:
                r += 1
            else:
                r -= 1
            d += 2 * abs(dy) - 2 * abs(dx)

        if flag == 0:
            x_points.append(c)
            y_points.append(r)
        else:
            x_points.append(r)
            y_points.append(c)

    return x_points, y_points

xa = int(input("Enter xa: "))
ya = int(input("Enter ya: "))
xb = int(input("Enter xb: "))
yb = int(input("Enter yb: "))

x_pts, y_pts = bresenham_line(xa, ya, xb, yb)

plt.figure(figsize=(6,6))
plt.plot(x_pts, y_pts, marker='o', color='green', markersize=4)

plt.title("Bresenham Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')

plt.show()