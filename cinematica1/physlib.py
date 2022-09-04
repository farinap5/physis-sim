import math
import numpy as np

# Particle speed on the x axis.
def Vx(ang=0, vi=0.0):
    a = math.radians(ang)
    return vi * math.cos(a)

# Particle speed on the y axis.
def Vy(ang=0, vi=0.0, g=9.81, t=0.0):
    a = math.radians(ang)
    return vi * math.sin(a) - g*t

def Px(xi=0.0, vx=0.0, t=0.0):
    return xi + vx * t

def Py(yi=0.0, vy=0.0, g=9.81, t=0.0):
    return yi + vy * t - 0.5 * g * t**2

def Vt(vx=0.0, vy=0.0):
    s = (vx**2) + (vy**2)
    return math.sqrt(s)

def Ang(vx=0.0, vy=0.0):
    return math.atan(vy/vx)