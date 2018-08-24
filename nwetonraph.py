from sympy import *
init_printing(use_unicode = True)
x, y =symbols('x y')
f, g = Function('f'), Function('g')
f = y*cos(x*y) + 1
g = sin(x*y) + x -y
j = Matrix([[diff(f,x), diff(f, y)], [diff(g,x), diff(g, y)]])**(-1)
mf = Matrix([[f], [g]])
x1, y1 = 1 , 2
for _ in range(2):
    [x1, y1] = Matrix([[x1],[y1]]) - (j*mf).subs([(x, x1),(y,y1)]).evalf()
print([x1,y1])
print(g.subs([(x, x1), (y,y1)]).evalf())
print(f.subs([(x, x1), (y,y1)]).evalf())
