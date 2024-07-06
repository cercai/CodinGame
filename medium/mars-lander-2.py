import sys
import math


def debug(x, y, h_speed, v_speed, fuel, rotate, power):
    print("coordinates: [" + str(x) + ", " + str(y) + "]", file=sys.stderr, flush=True)
    print("speed: [" + str(h_speed) + ", " + str(v_speed) + "]", file=sys.stderr, flush=True)
    print("fuel: " + str(fuel), file=sys.stderr, flush=True)
    print("rotate: " + str(rotate), file=sys.stderr, flush=True)
    print("power: " + str(power), file=sys.stderr, flush=True)


land_x = list()
land_y = list()
landing_site = list()
landing_height = 0

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # x: X coordinate of a surface point. (0 to 6999)
    # y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    x, y = [int(j) for j in input().split()]
    land_x.append(x)
    land_y.append(y)

# DEBUG - MARS LANDSCAPE
print(land_x, file=sys.stderr, flush=True)
print(land_y, file=sys.stderr, flush=True)

# FIND THE LANDING SITE
for x, y in enumerate(land_y):
    if x >= 1:
        if y == land_y[x-1] and land_x[x] - land_x[x-1] >= 1000:
            landing_height = land_y[x]
            landing_site = int(0.5 * (land_x[x-1] + land_x[x]))

# DEBUG - MARS LANDING SITE
print("landing site: " + str(landing_site), file=sys.stderr, flush=True)
print("landing height: " + str(landing_height), file=sys.stderr, flush=True)


def get_max_speed(x):
    DX = [-1500, -600, -200, 200, 600, 1500]
    MAX_SPEED = [40, 20, 5, -5, -20, -40]

    for i in range(len(DX) - 1):
        if DX[i] <= x < DX[i + 1]:
            return MAX_SPEED[i]

    if x < DX[0]:
        return MAX_SPEED[0]
    elif x >= DX[-1]:
        return MAX_SPEED[-1]
    

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    debug(x, y, h_speed, v_speed, fuel, rotate, power)

    dx = x - landing_site
    dh = y - landing_height

    print("dx: " + str(dx), file=sys.stderr, flush=True)
    print("dh: " + str(dh), file=sys.stderr, flush=True)

    rotation = 0
    power = 4

    DX_LIM = [-2000, -600, 600, 2000]
    DX_ROT = [-60, -25, 25, 60]

    if dx < DX_LIM[0]:
        rotation = DX_ROT[0]
    elif dx < DX_LIM[1]:
        rotation = DX_ROT[1]
    elif dx > DX_LIM[-1]:
        rotation = DX_ROT[-1]
    elif dx > DX_LIM[-2]:
        rotation = DX_ROT[-2]


    DH_LIM = [2000, 1500, 1000, 500]
    DH_POW = [3, 3, 4, 4]

    if dh > DH_LIM[0]:
        power = DH_POW[0]
    elif dh > DH_LIM[1]:
        power = DH_POW[1]
    elif dh > DH_LIM[2]:
        power = DH_POW[2]
    else:
        power = DH_POW[3]

    # dx < 0 if landing site on the right of the shuttle
    # h_speed > 0 when the shuttle is going on the right

    vmax = get_max_speed(dx)
    print("vmax: " + str(vmax), file=sys.stderr, flush=True)
    
    # SPEED LIMITS
    if h_speed > vmax:
            rotation = 20
    if h_speed < vmax:
            rotation = -20

    if dh < 100:
        rotation = 0


    # ALT
    DH_LIM = [2000, 1500, 1000, 500]
    ROT_ = [3, 4, 4, 4]

    if abs(v_speed) > 25:
        power = 4
        if abs(rotation) > 20:
            if rotation > 0:
                rotation = 20
            else:
                rotation = -20

    print(str(rotation) + " " + str(power))
