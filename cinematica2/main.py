import math
import numpy as np
import physlib as ph

if __name__ == "__main__":
    ang = 70
    vi  = 13

    print("   Time       X       Y      Vx      Vy  VTotal  VtR    Ang")
    print("----------------------------------------------------------")
    for i in np.linspace(0.0, 0.8301,dtype=float, num=10):
        ## Aplicando a força resistiva
        tmp = vi
        vi = ph.Resis(v=tmp)
        ## ###########################

        vx = ph.Vx(ang=ang,vi=vi)
        vy = ph.Vy(ang=ang,vi=vi,t=i)
        vt = ph.Vt(vx=vx,vy=vy)

        px = ph.Px(vx=vx,t=i)
        py = ph.Py(vy=ph.Vy(ang=ang,vi=vi,t=i, var=False),t=i)
        ag = ph.Ang(vx=vx, vy=vy)

        print("{t:7.3f} {x:7.3f} {y:7.3f} {vx:7.3f} {vy:7.3f} {vt:7.3f} {vr:7.3f} {a:7.3f}".format(
            t = i,
            x = px,
            y = py,
            vx = vx,
            vy = vy,
            vt = vt,
            vr = 222,
            a = np.degrees(ag)
        ))
