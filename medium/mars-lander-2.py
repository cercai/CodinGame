import sys
import math


def debug(x, y, Vx, Vy, fuel, rotate, power):
    print("coordinates: [" + str(x) + ", " + str(y) + "]", file=sys.stderr, flush=True)
    print("speed: [" + str(Vx) + ", " + str(Vy) + "]", file=sys.stderr, flush=True)
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

def radio_altitude(x, y, land_x, land_y):
    for i, j in enumerate(land_x):
        if i >= 1:
            if  land_x[i-1] <= x and x <= land_x[i]:
                a = (land_y[i] - land_y[i - 1]) / (land_x[i] - land_x[i-1])
                b = land_y[i-1]
                alt =  y - (a * (x-land_x[i-1]) + b)

                return alt

def ground_proctection(x, y, Vx, Vy, land_x, land_y):
    # if dh and dh < 500:
    future_x = x + 5*Vx
    future_y = y + 5*Vy

    future_x = max(0, future_x)
    future_y = max(0, future_y)

    print("x" + str(x), file=sys.stderr, flush=True)
    print("future_x" + str(future_x), file=sys.stderr, flush=True)

    print("y" + str(y), file=sys.stderr, flush=True)
    print("future_y" + str(future_y), file=sys.stderr, flush=True)

    if radio_altitude(future_x, future_y, land_x, land_y) < 700:
        for i, j in enumerate(land_x):
            if i >= 1:
                if  land_x[i-1] <= future_x and future_x <= land_x[i]:
                    a = (land_y[i] - land_y[i - 1]) / (land_x[i] - land_x[i-1])
                    return 90 * math.sin(a)
                    print("ground_proctection", file=sys.stderr, flush=True)
                    print("a " + str(a), file=sys.stderr, flush=True)
                    print("90 * math.sin(a) " + str(90 * math.sin(a)), file=sys.stderr, flush=True)
                    # 90 * math.sin(a)
                    # b = land_y[i-1]
                    # alt =  y - (a * (future_x-land_x[i-1]) + b)

                    # return alt
            
        


    # print("land_y[i]" + str(land_y[i]), file=sys.stderr, flush=True)
    # print("land_y[i-1]" + str(land_y[i-1]), file=sys.stderr, flush=True)
    # print("land_y[i]-land_y[i-1]" + str(land_y[i]-land_y[i-1]), file=sys.stderr, flush=True)
    # rotation = 90 * math.sin(Vx/speed)
    # power = 4

    # for i, j in enumerate(land_x):
    #     if i >= 1:
    #         if  land_x[i-1] <= x and x <= land_x[i]:
    #             a = (land_y[i] - land_y[i - 1]) / (land_x[i] - land_x[i-1])
    #             b = land_y[i-1]
    #             alt =  y - (a * (x-land_x[i-1]) + b)

    #             return alt

# game loop
while True:
    # Vx: the horizontal speed (in m/s), can be negative.
    # Vy: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, Vx, Vy, fuel, rotate, power = [int(i) for i in input().split()]

    dh = radio_altitude(x, y, land_x, land_y)
    debug(x, y, Vx, Vy, fuel, rotate, power)

    dx = x - landing_site
    dy = y - landing_height

    # print("alt: " + str(alt), file=sys.stderr, flush=True)
    print("dx: " + str(dx), file=sys.stderr, flush=True)
    print("dy: " + str(dy), file=sys.stderr, flush=True)

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


    DY_LIM = [2000, 1500, 1000, 500]
    DY_POW = [2, 3, 4, 4]

    if dy > DY_LIM[0]:
        power = DY_POW[0]
    elif dy > DY_LIM[1]:
        power = DY_POW[1]
    elif dy > DY_LIM[2]:
        power = DY_POW[2]
    else:
        power = DY_POW[3]

    # dx < 0 if landing site on the right of the shuttle
    # Vx > 0 when the shuttle is going on the right
    Vx_max = 0
    Vy_max = 0

    vmax = get_max_speed(dx)
    print("vmax: " + str(vmax), file=sys.stderr, flush=True)
    
    # SPEED LIMITS
    if Vx > vmax:
            rotation = 40
    if Vx < vmax:
            rotation = -40

    if dy < 100:
        rotation = 0


    # ALT
    # DY_LIM = [2000, 1500, 1000, 500]
    # ROT_ = [3, 4, 4, 4]

    if abs(Vy) > 45:
        power = 4
        if abs(rotation) > 10:
            if rotation > 0:
                rotation = 10
            else:
                rotation = -10
    elif abs(Vy) > 25:
        power = 4
        if abs(rotation) > 20:
            if rotation > 0:
                rotation = 20
            else:
                rotation = -20

    print("dh", str(dh), file=sys.stderr, flush=True)
    # print("Vy/dh", str(Vy / dh), file=sys.stderr, flush=True)

    speed = math.sqrt(Vx*Vx + Vy*Vy)

    print("speed", str(speed), file=sys.stderr, flush=True)
    if dh and abs(speed) > dh / 10:
        print("GROUND_PROTECTION", file=sys.stderr, flush=True)


    # SPEED PROTECTION
    if speed > 50:
        rotation = 90 * math.sin(Vx/speed)
        power = 4

    if rotation > 60:
        rotation = 60
    elif rotation < -60:
        rotation = -60

    # GROUND PROTECTION
    gp = ground_proctection(x, y, Vx, Vy, land_x, land_y)
    if gp:
        rotation = gp
        power = 4

    print(str(int(rotation)) + " " + str(power))
