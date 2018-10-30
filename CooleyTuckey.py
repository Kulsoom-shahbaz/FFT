# -*- coding: utf-8 -*-
"""
Reference Citation
- Author: Darko Lukic
- Date: 05 Apr 2014
- Title of program: Cooley-Tukey FFT step using Map Reduce
- Code version: 
- Type: lukicdarkoo/fft.py Computer program
- Web address: http://pythonexample.com/code/cooley%20tukey/
"""

 #libararies 
import numpy as np #for data structures arrays 
import matplotlib.pyplot as plt #for plotting graph
import random #for random integers
 
SAMPLE_RATE = 8192 #sample rate globally defined
N = 128 # Windowing globally defined
 
 
def fft(x): #function that takes 
    X = list() #list created ~ object declared 
    for k in range(0, N): # from 0 to 128
        window = 1 # np.sin(np.pi * (k+0.5)/N)**2
        X.append(np.complex(x[k] * window, 0)) # appending x with the kth index multiplied by 1 and populates the list in X
 
    fft_rec(X) # all the values of X passed to another function fft_rec
    return X
 
def fft_rec(X):
    N = len(X) #N includes the lenght of X
 
    if N <= 1: #if it is zero and return back to the fuction 
        return
 #else if N is greater than 1 then it divides the array in even and odd indices
    even = np.array(X[0:N:2]) #go from 0 to 2nd step by step for even indices 
    odd = np.array(X[1:N:2]) #go from 1 to 3rd step by step for odd indices
 
    #Now recursion is called, all the even and odd indices called by themselves recursively 
    fft_rec(even)
    fft_rec(odd)
    # this is keep on going until there is one single element in the list
    
    for k in range(0, N//2): #loop for all the indices coming from the fuction fft_rec
        t = np.exp(np.complex(0, -2 * np.pi * k / N)) * odd[k] #formula applied and multiplied by odd
        X[k] = even[k] + t #equated kth index with even element of array with t calculated above 
        X[N//2 + k] = even[k] - t
 
  
x_values = np.arange(0, N, 1) # program starts here and makes an array of N and N is defined globally
 
x = np.sin((2*np.pi*x_values / 4.0)) # 32 - 256Hz 
x += np.sin((2*np.pi*x_values / 8.0)) # 64 - 128Hz
 
X = fft(x) #fft ffunction called and the values of x passed
 
 
# Plotting 
_, plots = plt.subplots(2)

## Plot in time domain
plots[0].plot(x)
 
## Plot in frequent domain
powers_all = np.abs(np.divide(X, N//2))
powers = powers_all[0:N//2] #all the powers extracted
frequencies = np.divide(np.multiply(SAMPLE_RATE, np.arange(0, N//2)), N) #all the frequencies extracted
plots[1].plot(frequencies, powers) #plots frequencies and powers
## Show plots
plt.show()