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

if __name__ == "__main__":
    ang = 70
    vi  = 13

    print("   Time       X       Y      Vx      Vy  VTotal     Ang")
    print("-------------------------------------------------------")
    for i in np.linspace(0.0, 0.8301,dtype=float, num=10):
        vx = Vx(ang=ang,vi=vi)
        vy = Vy(ang=ang,vi=vi,t=i)
        vt = Vt(vx=vx,vy=vy)

        px = Px(vx=vx,t=i)
        py = Py(vy=vy,t=i)
        ag = Ang(vx=vx, vy=vy)

        print("{t:7.3f} {x:7.3f} {y:7.3f} {vx:7.3f} {vy:7.3f} {vt:7.3f} {a:7.3f}".format(
            t = i,
            x = px,
            y = py,
            vx = vx,
            vy = vy,
            vt = vt,
            a = np.degrees(ag)
        ))
