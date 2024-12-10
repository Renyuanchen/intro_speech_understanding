import numpy as np

def voiced_excitation(duration, F0, Fs):
    excitation = np.zeros(duration)
    period = int(np.round(Fs / F0))
    excitation[::period] = -1
    return excitation

def resonator(x, F, BW, Fs):
    r = np.exp(-np.pi * BW / Fs)
    omega = 2 * np.pi * F / Fs
    b = [1]
    a = [1, -2 * r * np.cos(omega), r**2]
    y = np.zeros_like(x)
    for n in range(2, len(x)):
        y[n] = b[0] * x[n] - a[1] * y[n - 1] - a[2] * y[n - 2]
    return y

def synthesize_vowel(duration, F0, F1, F2, F3, F4, BW1, BW2, BW3, BW4, Fs):
    excitation = voiced_excitation(duration, F0, Fs)
    formant1 = resonator(excitation, F1, BW1, Fs)
    formant2 = resonator(formant1, F2, BW2, Fs)
    formant3 = resonator(formant2, F3, BW3, Fs)
    speech = resonator(formant3, F4, BW4, Fs)
    return speech

