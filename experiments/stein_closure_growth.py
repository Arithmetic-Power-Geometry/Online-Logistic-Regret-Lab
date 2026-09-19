import json


def closure_counts(r, rounds):
    # Symbolic lower-bound counting model.
    # Start with r singleton sigmoid expectations.
    # Multiplication by the logistic score can create products indexed by
    # multisets of directions. After k multiplication rounds, monomials of
    # sigmoid factors up to degree k+1 can appear.
    #
    # Number of degree-m commutative monomials in r generators:
    # C(r+m-1,m).
    import math

    out = []
    total = 0
    for degree in range(1, rounds + 2):
        count = math.comb(r + degree - 1, degree)
        total += count
        out.append({
            "degree": degree,
            "new_sigmoid_monomials_upper_model": count,
            "cumulative": total,
        })
    return out


if __name__ == "__main__":
    result = {}
    for r in [2, 4, 8, 16, 32]:
        result[str(r)] = closure_counts(r, 5)
    print(json.dumps(result, indent=2))
