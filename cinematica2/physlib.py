import math
import numpy as np

# Particle speed on the x axis.
def Vx(ang=0, vi=0.0):
    a = math.radians(ang)
    return vi * math.cos(a)

# Particle speed on the y axis.
def Vy(ang=0, vi=0.0, g=9.81, t=0.0, var=True):
    a = math.radians(ang)
    v = vi * math.sin(a)
    if var:
        return v - g*t
    else:
        return v

def Px(xi=0.0, vx=0.0, t=0.0):
    return xi + vx * t

def Py(yi=0.0, vy=0.0, g=9.81, t=0.0):
    return yi + vy * t - 0.5 * g * t**2

def Vt(vx=0.0, vy=0.0):
    s = (vx**2) + (vy**2)
    return math.sqrt(s)

def Ang(vx=0.0, vy=0.0):
    return math.atan(vy/vx)

def Resis(d=0.47, p=1.21, a=0.8, v=0.0):
    r = 0.5 * d * p * a * (v ** 2)
    return r

def Ax(R=0.0, m=5, ang=0.0):
    a = math.radians(ang)
    return -(R * np.cos(ang))/m

def Ay(R=0.0, m=5, ang=0.0, g=9.81):
    a = math.radians(ang)
    return -g-(R * np.sin(ang))/m