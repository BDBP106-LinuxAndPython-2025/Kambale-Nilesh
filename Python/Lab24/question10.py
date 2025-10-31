"""(10) The normalized Gaussian function centered at x = 0 is
g(x) = (1/σ√2π)exp(−x^2/2σ^2)
Plot and compare the shapes of these functions for standard deviations σ = 1, 1.5 and 2."""
import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(-10,10,1000)

def gaussfunc(x,sigma):
    return (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-x**2/(2*sigma**2))

plt.figure(figsize=(8,5))
for sigma in [1,1.5,2]:
    plt.plot(x,gaussfunc(x,sigma),label=f"sigma= {sigma}")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.show()