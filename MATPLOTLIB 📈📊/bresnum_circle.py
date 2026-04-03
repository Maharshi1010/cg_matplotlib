import matplotlib.pyplot as plt

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    x_points = []
    y_points = []

    while x <= y:
        x_points.extend([xc + x, xc - x, xc + x, xc - x,
                         xc + y, xc - y, xc + y, xc - y])
        
        y_points.extend([yc + y, yc + y, yc - y, yc - y,
                         yc + x, yc + x, yc - x, yc - x])

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1

        x += 1

    return x_points, y_points


xc = int(input("Enter xC: "))
yc = int(input("Enter yC: "))
r = int(input("Enter Radius: "))

x_pts, y_pts = bresenham_circle(xc, yc, r)

plt.figure(figsize=(6,6))
plt.scatter(x_pts, y_pts, color='blue', s=10)

plt.title("Bresenham Circle Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')

plt.show()