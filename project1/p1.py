print('Solve: SLAYER + SLAYER + SLAYER = LAYERS')
print('')
slayer = input('What is your guess? ')
slayer = int(slayer)
#gets the user's input
real_layers = int(slayer * 3)
#multiplies input by 3


r = slayer % 10
e = (slayer // 10) % 10
y = (slayer // 100) % 10
a = (slayer // 1000) % 10
l = (slayer // 10000) % 10
s = (slayer // 100000) % 10
# each letter is every individual number in the 6 digit number: SLAYER
tested_layers = ((l * 100000) + (a * 10000) + (y* 1000) + (e * 100) + (r* 10) + (s * 1))
# tested_layers is the SLAYER number with the numbers switched around to form LAYERS
print(f"{tested_layers} == {real_layers} -> {bool(tested_layers == real_layers)}")