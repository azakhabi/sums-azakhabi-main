def sums(array: list) -> int:
    f = set()
    b = [0,array[0]]
    f.update(b)
    for i in range(1,len(array)):
        for j in f:
            b.append(array[i]+j)
        f.update(b)
        b.clear()
    return len(f)
