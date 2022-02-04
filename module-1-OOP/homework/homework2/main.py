from square import Square
from oval import Oval

# Squares
sq1 = Square('Square1')
sq1.side = 10
sq1.calculate_area()

sq2 = Square('Square2')
sq2.side = 130
sq2.calculate_area()

# Ovals
ov1 = Oval('Oval1')
ov1.radius = 5
ov1.calculate_area()

ov2 = Oval('Oval2')
ov2.radius = 22
ov2.calculate_area()

# Areas sum
lst = [sq1, sq2, ov1, ov2]
areas_sum = 0
for obj in lst:
    areas_sum += obj.area
print(f'Shape areas sum = {areas_sum}')
