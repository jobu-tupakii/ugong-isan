tuples = [(1,2),(1,1),(5,7),(7,5)]
sorted_t = sorted(tuples)
print(sorted_t)
sorted_t = sorted(tuples, key=lambda x:x[1])
print(sorted_t)