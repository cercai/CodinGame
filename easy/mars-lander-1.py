import sys
import math


def debug(x, y, h_speed, v_speed, fuel, rotate, power):
    print("coordinates: [" + str(x) + ", " + str(y) + "]", file=sys.stderr, flush=True)
    print("speed: [" + str(h_speed) + ", " + str(v_speed) + "]", file=sys.stderr, flush=True)
    print("fuel: " + str(fuel), file=sys.stderr, flush=True)
    print("rotate: " + str(rotate), file=sys.stderr, flush=True)
    print("power: " + str(power), file=sys.stderr, flush=True)


surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    debug(x, y, h_speed, v_speed, fuel, rotate, power)

    if y < 1800:
        print("0 4")
    else:
        print("0 3")
