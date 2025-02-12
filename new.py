# thi is to represen tthe whole data as a set
import numpy as np
import matplotlib.pyplot as plt

# Load data from the .txt file
data = np.loadtxt("C:\Users\Rushikesh\Desktop\EXP LABS/dataA.txt")  # Replace "data.txt" with the path to your file

# Separate the data into two variables: wavelength and aberration shift
wavelengths = data[:, 0]
aberration_shift = data[:, 1]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(wavelengths, aberration_shift, color='blue', label="Aberration Shift")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Shift of Total Aberration (arbitrary units)")
plt.title("Graph between Wavelength and Shift of Total Aberration")
plt.legend()
plt.grid(True)
plt.show()








