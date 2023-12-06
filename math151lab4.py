from symp import *
from symp.plotting import (plot_parametric,plot3d_parametric_surface, plot3d_parametric_line,plot3d)
x = symbols('x')
x1 = 0
y1 = 2
fun = x**4+2*E**x
dfun = diff(fun, x)
m = dfun.subs(x, 0)
print('The derivative of f(x) ', fun)
print('The derivative of f(0) ', m)
y = m*(x-x1)+y1
nfun = y.subs(m, 2)
print('The equation for the tangent line at the point, y =', nfun)
iy = (-1*m)*(x-x1)+y1
infun = iy.subs(im, 2)
print('This is the invert equation of the tangent line, y =', infun)
fplot = plot(y,iy,fun,(x,-1,1))
