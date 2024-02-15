# as tuple are immutable we cannot perform operations like list. To do this we can cast a tuple into a list and 
# perform the operations once done again cast back it to tuple

tpl = (19,23,33,321)
print(tpl)
l = list(tpl)
lst = tuple(l)