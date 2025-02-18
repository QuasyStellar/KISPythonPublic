import tkinter as tk
import math


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p : p + 3] = [
                max(min(int(c * 255), 255), 0) for c in func(x / w, y / h)
            ]
    return bytes("P6\n%d %d\n255\n" % (w, h), "ascii") + scr


# Ваш код здесь:
# 4.1
# def func(x, y):
#     return 0, 0, 0

# 4.2
# def func(x, y):
#     cx_g, cy_g = 0.45, 0.45
#     r_g = 0.3

#     cx_r, cy_r = 0.5, 0.5
#     r_r = 0.3

#     d_r = ((x - cx_r) ** 2 + (y - cy_r) ** 2) ** 0.5
#     d_g = ((x - cx_g) ** 2 + (y - cy_g) ** 2) ** 0.5

#     intensity_red = 1 - (d_r / r_r)**2
#     intensity_green = 1 - (d_g / r_g)**2

#     return intensity_red, intensity_green, 0


# 4.3
# def func(x, y):
#     cx, cy = 0.5, 0.5
#     ex, ey = 0.6, 0.25
#     radius = 0.4
#     eye_radius = 0.05
#     angle_start = 35
#     angle_end = 325
#
#     dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
#
#     if dist < radius:
#         eye = math.sqrt((x - ex) ** 2 + (y - ey) ** 2)
#         angle = math.degrees(math.atan2(y - cy, x - cx))
#         if angle < 0:
#             angle += 360
#
#         if angle >= angle_start and angle <= angle_end and eye > eye_radius:
#             return (1, 1, 0)
#         else:
#             return (0, 0, 0)
#     else:
#         return (0, 0, 0)

# 4.4
# def noise(x, y):
#     n = math.sin(x * 19.191919 + y * 78.7878787) * 12345.678912
#     return n - math.floor(n)
#
#
# def func(x, y):
#     n = noise(x, y)
#     return (n, n, n)

# 4.5
# def noise(x, y):
#     n = math.sin(x * 19.191919 + y * 78.7878787) * 12345.678912
#     return n - math.floor(n)
#
#
# def fade(t):
#     return t * t * t * (t * (t * 6 - 15) + 10)
#
#
# def lerp(a, b, t):
#     return a + t * (b - a)
#
#
# def val_noise(x, y):
#     x0 = math.floor(x)
#     x1 = x0 + 1
#     y0 = math.floor(y)
#     y1 = y0 + 1
#     n00 = noise(x0, y0)
#     n01 = noise(x0, y1)
#     n10 = noise(x1, y0)
#     n11 = noise(x1, y1)
#     sx = fade(x - x0)
#     nx0 = lerp(n00, n10, sx)
#     nx1 = lerp(n01, n11, sx)
#     sy = fade(y - y0)
#     return lerp(nx0, nx1, sy)
#
#
# def func(x, y):
#     noise_value = val_noise(x * 5, y * 5)
#     return (noise_value, noise_value, noise_value)


# 4.6
def noise(x, y):
    n = math.sin(x * 19.191919 + y * 78.7878787) * 12345.678912
    return n - math.floor(n)


def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)


def lerp(a, b, t):
    return a + t * (b - a)


def val_noise(x, y):
    x0 = math.floor(x)
    x1 = x0 + 1
    y0 = math.floor(y)
    y1 = y0 + 1
    n00 = noise(x0, y0)
    n01 = noise(x0, y1)
    n10 = noise(x1, y0)
    n11 = noise(x1, y1)
    sx = fade(x - x0)
    nx0 = lerp(n00, n10, sx)
    nx1 = lerp(n01, n11, sx)
    sy = fade(y - y0)
    return lerp(nx0, nx1, sy)


def fBm(x, y, octaves=6, persistence=0.6):
    value = 0
    amplitude = 0.3
    frequency = 3
    max_value = 0
    for i in range(octaves):
        value += val_noise(x * frequency, y * frequency) * amplitude
        max_value += amplitude
        amplitude *= persistence
        frequency *= 2
    return value / max_value


def func(x, y):
    noise_value = fBm(x, y, octaves=6, persistence=0.5)
    brightness = 0.5 + noise_value * 0.5
    sky_blue = (0.53, 0.81, 0.98)
    cloud_white = (1, 1, 1)
    cloud_color = tuple(c * brightness for c in cloud_white)
    r = sky_blue[0] * (1 - brightness) + cloud_color[0] * brightness
    g = sky_blue[1] * (1 - brightness) + cloud_color[1] * brightness
    b = sky_blue[2] * (1 - brightness) + cloud_color[2] * brightness
    return (r, g, b)


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
