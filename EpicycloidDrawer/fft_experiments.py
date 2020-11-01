#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:01:57 2020

@author: qd
"""
import numpy as np
import matplotlib.pyplot as plt

# array init
a = np.zeros(20)
a[1] = 1
# plot array
plt.subplot(2, 2, 1)
plt.plot(a)
# compute transform
transform = np.fft.fft(a)
# plot real part of the transform
plt.subplot(2, 2, 3)
plt.plot(np.real(transform))
plt.ylabel("real")
# plot imaginary part
plt.subplot(2, 2, 4)
plt.plot(np.imag(transform))
plt.ylabel("imaginary")
plt.show()

def fourier_series_coeff_numpy(f, T, N, return_complex=True):
       """Calculates the first 2*N+1 Fourier series coeff. of a periodic function.       """
       # From Shanon theoreom we must use a sampling freq. larger than the maximum
       # frequency you want to catch in the signal.
       f_sample = 2 * N
       # we also need to use an integer sampling frequency, or the
       # points will not be equispaced between 0 and 1. We then add +2 to f_sample
       t, dt = np.linspace(0, T, f_sample + 2, endpoint=False, retstep=True)

       y = np.fft.rfft(f(t)) / t.size

       if return_complex:
           return y
       else:
           y *= 2
           return y[0].real, y[1:-1].real, -y[1:-1].imag

def f(t):
    return np.cos(t)

N_chosen = 10
c = fourier_series_coeff_numpy(f, np.pi*2, N_chosen)

T = np.pi*2
# #### test similarly that it works with complex coefficients:

def series_complex_coeff(c, t, T):
       """calculates the Fourier series with period T at times t,
          from the complex coeff. c"""
       tmp = np.zeros((t.size), dtype=np.complex64)
       for k, ck in enumerate(c):
           # sum from 0 to +N
           tmp += ck * np.exp(2j * np.pi * k * t / T)
           # sum from -N to -1
           if k != 0:
               tmp += ck.conjugate() * np.exp(-2j * np.pi * k * t / T)
       return tmp.real

t = np.linspace(0, T, 100)
f_values = f(t)
c = fourier_series_coeff_numpy(f, T, 7, return_complex=True)
f_series_values = series_complex_coeff(c, t, T)
assert allclose(f_series_values, f_values, atol=1e-6)
