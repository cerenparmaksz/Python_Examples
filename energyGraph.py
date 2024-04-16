import numpy as np
import matplotlib.pyplot as plt

m = 0.5  
k = 100  
g = 9.8 
initialdisp = 0.1  #initial displacement from equilibrium (m)

def position_as_function_of_time(t):
    omega = np.sqrt(k / m)  # angular frequency of the harmonic oscillator
    x = initialdisp * np.cos(omega * t)
    return x

timearr = np.linspace(0, 2 * np.pi * np.sqrt(m / k), num=1000)

positions = position_as_function_of_time(timearr)

def kinetic_energy(t):
    omega = np.sqrt(k / m) 
    v = -initialdisp * omega * np.sin(omega * t) #velocityy
    ke = 0.5 * m * v**2  # kinetic energy
    return ke


def potential_energy(t):
    omega = np.sqrt(k / m)  
    x = initialdisp * np.cos(omega * t) 
    pe = 0.5 * k * x**2  # potential energy
    return pe


def total_mechanical_energy(t):
    ke = kinetic_energy(t) 
    pe = potential_energy(t)
    tme = ke + pe  # total mechanical energy
    return tme

kinetic_energy_values = [kinetic_energy(t) for t in timearr]
potential_energy_values = [potential_energy(t) for t in timearr]
total_mechanical_energy_values = [total_mechanical_energy(t) for t in timearr]


plt.plot(timearr, positions, label='Position')
plt.plot(timearr, kinetic_energy_values, label='Kinetic Energy')
plt.plot(timearr, potential_energy_values, label='Potential Energy')
plt.plot(timearr, total_mechanical_energy_values, label='Total Mechanical Energy')
plt.title('Energy Conservation')
plt.xlabel('seconds')
plt.ylabel('Energy-Joule')
plt.legend()
plt.grid(True)
plt.show()

