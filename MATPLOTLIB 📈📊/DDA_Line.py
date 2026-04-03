import matplotlib.pyplot as plt

def Round(a):
    return int(a + 0.5)

def DDAline(xa, ya, xb, yb):
    dx = xb - xa
    dy = yb - ya

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xinc = dx / float(steps)
    yinc = dy / float(steps)

    x = xa
    y = ya

    print("X\tY\txplot\typlot")
    print(f"{x}\t{y}\t{Round(x)}\t{Round(y)}")

    x_points = [Round(x)]
    y_points = [Round(y)]

    for i in range(steps):
        x += xinc
        y += yinc
        print(f"{x:.2f}\t{y:.2f}\t{Round(x)}\t{Round(y)}")

        x_points.append(Round(x))
        y_points.append(Round(y))

    return x_points, y_points

xa = int(input("Enter Xa: "))
ya = int(input("Enter Ya: "))
xb = int(input("Enter Xb: "))
yb = int(input("Enter Yb: "))

x_pts, y_pts = DDAline(xa, ya, xb, yb)

plt.figure(figsize=(6, 6))
plt.plot(x_pts, y_pts, marker='o', color='blue', label="DDA Line")
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()

plt.axis('equal')

plt.show()