import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

# Generation subplots
fig, ax = plt.subplots()

# Définition du signal
f0 = 440    # Fréquence du signal
a0 = 1.0    # Amplitude
fs = 520    # Fréquence d'échantillonnage
phi0 = 2 * np.pi / 3  # Phase initiale

fc = f0 * 100  # Échantillonnage pour le signal continu

start = -20e-3  # Temps de départererrerfeff
stop = 20e-3    # Temps d'arrêt

# Signal échantillonné
t = np.arange(start, stop + 1/fs, 1/fs)
x = a0 * np.sin(2 * np.pi * f0 * t + phi0)

# Signal continu
tc = np.arange(start, stop + 1/fc, 1/fc)
xc = a0 * np.sin(2 * np.pi * f0 * tc + phi0)

# Affichage du graphique
ax.plot(t, x, 'o', label="Sampled Signal")
ax.plot(tc, xc, '--', label="Continuous Signal")

# Ajout des légendes
ax.set_xlabel('Time (s)', fontsize=10)
ax.set_ylabel('Amplitude', fontsize=10)
ax.set_title('Signal continuous et échantillonné à %d Hz (échantillonné à %d Hz)' % (f0, fs))

# Affichage de la légende
ax.legend()

# Affichage du graphique
plt.show()
