def sq_num(n):
    sq = []
    for i in range(1,n+1):
        sq.append(i*i)
    return sq

print(sq_num(10))


# using generators              To handle huge volume of data Generators are very helpful | saves memory
def sq_num_gen(n):
    for i in range(1,n+1):
        yield i*i

a = sq_num_gen(10)
print(a)            # it wil give <generator object sq_num_gen at 0x000002037E6710E0> as result

for i in a:
    print(i)
