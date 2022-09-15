# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from collections import namedtuple
Predicat = namedtuple("predicat", "x y z")
predicat = {Predicat(0,0,0), Predicat(0,1,0), Predicat(0,1,1), Predicat(1,0,0), Predicat(1,0,1), Predicat(1,1,0), Predicat(1,1,1)}
for i in predicat:
    x = Predicat[i].x
    y = Predicat[i].y
    z = Predicat[i].z
if (not (x or y or z)) == (not x and not y and not z):
    print("Истинно")
else:
    print("Ложно")