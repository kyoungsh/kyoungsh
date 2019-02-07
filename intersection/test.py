class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

# that's it!  Now, you can create a Bunch
# whenever you want to group a few variables:

x = 1
y = 2

point = Bunch(datum=y, squared=y*y, coord=x)

# and of course you can read/write the named
# attributes you just created, add others, del
# some of them, etc, etc:

threshold = 1

if point.squared > threshold:
    point.isok = 1