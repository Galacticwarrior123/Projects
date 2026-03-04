tuplex = ("tuple",False,3.2,1)
print(tuplex)

tuplex = (4,7,8,3,9,0)
print(tuplex)
tuplex=tuplex + (1,)
print(tuplex)

tuplex = (50,30,20,10,60,70,50,50)
print(tuplex.count(50))

tuplex =(2,3,4,5,7,9,6,7,3,4)
print("Original tuple:", tuplex)

_slice = tuplex [3:5]
print("Sliced tuple:", _slice)

_slice = tuplex [:6]
print("Sliced tuple:", _slice)
    