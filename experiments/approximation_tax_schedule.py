import json
import math


def tax_bound(T, c_alpha=0.25, c_delta=0.05):
    total=0.0
    simple=0.0
    worst_ratio=0.0
    for t in range(1,T+1):
        alpha=c_alpha/t
        delta=c_delta/(t*t)
        if delta >= alpha:
            raise ValueError("schedule violates delta<alpha")
        bound=delta/(alpha-delta)
        total += bound
        simple += 2*delta/alpha if delta <= alpha/2 else float("nan")
        worst_ratio=max(worst_ratio,delta/alpha)
    return {
        "T":T,
        "exact_mvt_tax_bound":total,
        "two_delta_over_alpha_bound":simple,
        "log1pT":math.log1p(T),
        "bound_over_log1pT":total/math.log1p(T),
        "max_delta_over_alpha":worst_ratio,
    }


if __name__=="__main__":
    print(json.dumps([tax_bound(T) for T in [32,64,128,256,512,1024,4096,16384]],indent=2))
