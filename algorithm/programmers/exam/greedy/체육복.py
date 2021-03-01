def solution(n, lost, reserve):
    rv = [r for r in reserve if r not in lost]
    lst = [l for l in lost if l not in reserve]

    for l in rv:
        if l-1 in lst:
            lst.remove(l-1)

        elif l+1 in lst:
            lst.remove(l+1)

    return n-len(lst)