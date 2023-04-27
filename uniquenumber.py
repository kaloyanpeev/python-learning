def find_uniq(arr):
    counts = {}
    uniq_numbs = list(set(arr))
    for item in arr:
        if item in counts:
            counts[item] += 1
            if counts[item] == 2:
              uniq_numbs.remove(item)
              break
        else:
            counts[item] = 1
    return uniq_numbs[0]



print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
