import numpy as np
import matplotlib.pyplot as plt

def main():
    files = (
        'ic_vce_2.8.out',
        'ic_vce_2.9.out',
        'ic_vce_3.0.out',
        'ic_vce_3.1.out',
        'ic_vce_3.2.out',
        #'ic_vce_0.6.out',
        #'ic_vce_0.7.out',
        #'ic_vce_0.8.out',
        #'ic_vce_0.9.out',
        #'ic_vce_1.0.out',
    )
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta']

    for filename, color in zip(files, colors):
        data = np.loadtxt(filename)
        vce = data[:,1] - data[:,2]
        ic = data[:,4]
        plt.plot(vce, ic, color=color, label=filename)

    plt.xlabel(r"$V_{ce}$ (V)")
    plt.ylabel(r"$I_c$ (A/cm)")
    plt.legend()
    plt.savefig('raser/field/ic_vce.pdf')
