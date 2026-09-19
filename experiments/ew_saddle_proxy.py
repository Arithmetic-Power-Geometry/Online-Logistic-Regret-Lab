import json
import math

def lambertw_newton(x, iters=50):
    # positive branch W_0(x), sufficient for x>0
    w = math.log1p(x)
    for _ in range(iters):
        ew = math.exp(w)
        f = w * ew - x
        denom = ew * (w + 1.0) - (w + 2.0) * f / (2.0 * w + 2.0)
        step = f / denom
        w -= step
        if abs(step) < 1e-14 * max(1.0, abs(w)):
            break
    return w

def ew_tail_proxy(t, prior_var):
    w = lambertw_newton(prior_var * t)
    return w / (prior_var * t)

if __name__ == "__main__":
    out = {}
    for s2 in [1.0, 4.0, 9.0, 25.0, 100.0]:
        rows = []
        for t in [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]:
            proxy = ew_tail_proxy(t, s2)
            rows.append({
                "t": t,
                "proxy": proxy,
                "scaled_t_over_logt": proxy * t / math.log(t),
            })
        out[str(s2)] = rows
    print(json.dumps(out, indent=2))
