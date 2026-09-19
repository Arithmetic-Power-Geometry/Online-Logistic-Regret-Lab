import json, math

def symdim(d,k):
    return math.comb(d+k-1,k)

def total_even(d,m):
    return sum(symdim(d,2*j) for j in range(1,m+1))

rows=[]
for d in [2,4,8,16,32,64]:
    for m in [2,4,8,12,16]:
        rows.append({"d":d,"m":m,"max_order":2*m,
                     "explicit_symmetric_tensor_state":total_even(d,m)})
print(json.dumps(rows,indent=2))
