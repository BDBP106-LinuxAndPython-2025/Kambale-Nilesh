"""(9) Plot the function
f1(x) = ln(1/cos^2(x)) and f2(x) = ln(1/sin^2(x)) (1)
on 1000 points across the range −20 ≤ x ≤ 20. What happens to these functions at
x = nπ/2(n = 0, ±1, ±2, . . .)? What happens in your plot of them?"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-20,20,1000)

f1=np.log(1/(np.cos(x)**2))
f2=np.log(1/(np.sin(x)**2))

plt.plot(x,f1,label="f1(x)=ln(1/cos^2x")
plt.plot(x,f2,label="f1(x)=ln(1/sin^2x")

plt.ylim(-10,10)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()