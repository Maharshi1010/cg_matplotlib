import matplotlib.pyplot as plt

TOP, BOTTOM, RIGHT, LEFT = 0, 1, 2, 3

def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    code = [0, 0, 0, 0]

    if y > ymax:
        code[TOP] = 1
    if y < ymin:
        code[BOTTOM] = 1
    if x > xmax:
        code[RIGHT] = 1
    if x < xmin:
        code[LEFT] = 1

    return code


def cohen_sutherland_clip(xa, ya, xb, yb, xmin, ymin, xmax, ymax):
    outa = compute_outcode(xa, ya, xmin, ymin, xmax, ymax)
    outb = compute_outcode(xb, yb, xmin, ymin, xmax, ymax)

    print("Outcode A:", "".join(map(str, outa)))
    print("Outcode B:", "".join(map(str, outb)))

    accept = False

    while True:
        # Case 1: Both inside
        if all(bit == 0 for bit in outa) and all(bit == 0 for bit in outb):
            accept = True
            break

        # Case 2: Both share outside region → reject
        elif any(outa[i] == 1 and outb[i] == 1 for i in range(4)):
            break

        else:
            # Pick outside point
            out = outa if any(outa) else outb

            if out[TOP]:
                x = xa + (xb - xa) * (ymax - ya) / (yb - ya)
                y = ymax
            elif out[BOTTOM]:
                x = xa + (xb - xa) * (ymin - ya) / (yb - ya)
                y = ymin
            elif out[RIGHT]:
                y = ya + (yb - ya) * (xmax - xa) / (xb - xa)
                x = xmax
            elif out[LEFT]:
                y = ya + (yb - ya) * (xmin - xa) / (xb - xa)
                x = xmin

            # Replace outside point
            if out == outa:
                xa, ya = x, y
                outa = compute_outcode(xa, ya, xmin, ymin, xmax, ymax)
            else:
                xb, yb = x, y
                outb = compute_outcode(xb, yb, xmin, ymin, xmax, ymax)

    if accept:
        print("Line accepted after clipping")
        return xa, ya, xb, yb
    else:
        print("Line rejected")
        return None

xmin = int(input("Enter xmin: "))
ymin = int(input("Enter ymin: "))
xmax = int(input("Enter xmax: "))
ymax = int(input("Enter ymax: "))

xa = int(input("Enter xa: "))
ya = int(input("Enter ya: "))
xb = int(input("Enter xb: "))
yb = int(input("Enter yb: "))

clipped = cohen_sutherland_clip(xa, ya, xb, yb, xmin, ymin, xmax, ymax)

plt.figure(figsize=(6,6))

rect_x = [xmin, xmax, xmax, xmin, xmin]
rect_y = [ymin, ymin, ymax, ymax, ymin]
plt.plot(rect_x, rect_y, color='black', label="Clipping Window")

plt.plot([xa, xb], [ya, yb], 'r--', label="Original Line")

if clipped:
    x1, y1, x2, y2 = clipped
    plt.plot([x1, x2], [y1, y2], 'g', linewidth=2, label="Clipped Line")

plt.title("Cohen-Sutherland Line Clipping")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.show()