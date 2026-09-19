import cmath
import json
import math


def pole_geometry(k):
    a=math.tan(math.pi/(2*k))
    rho=a+math.sqrt(1+a*a)
    logrho=math.log(rho)
    return {
        "k": k,
        "imaginary_pole_x": a,
        "rho_star": rho,
        "log_rho_star": logrho,
        "k_log_rho_star": k*logrho,
        "limit_pi_over_2": math.pi/2,
        "relative_to_pi_over_2": (k*logrho)/(math.pi/2),
    }


if __name__=="__main__":
    print(json.dumps([pole_geometry(k) for k in [2,4,8,16,32,64,128,256,512]],indent=2))
