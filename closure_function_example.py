def myclosure():
    val = 0
    def add(x):
        nonlocal val 
        val += x
        return val
    return add

pos = myclosure()

print(pos(1), pos(1), pos(8))


