#!/usr/bin/python3

"""Write a function protein_energy)temp) with an inner function
calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0)."""


def protein_energy(temp, enthalpy, entropy):
    def calculate_free_energy(H, S):
        return H - temp * S

    gfe = calculate_free_energy(enthalpy, entropy)

    if gfe < 0:
        return "stable"
    else:
        return "unstable"

temp=float(input("Enter the temperature: "))
enthalpy=float(input("Enter the enthalpy: "))
entropy=float(input("Enter the entropy: "))
print(protein_energy(temp, enthalpy, entropy))
