from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

def generate_graph_low_high(filter_type,filter_order,cutoff_freq, signal_filter_value):

    b, a = signal.butter(int(filter_order), int(cutoff_freq), filter_type, analog=True)
    w, h = signal.freqs(b, a)

    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title('Frequency Response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    #cutoff frequency
    plt.axvline(int(cutoff_freq), color='green') 

    #Generate a signal made up of 10 Hz and 50 Hz, sampled at 1 kHz
    t = np.linspace(0, 1, 1000, False)  # 1 second
    sig = 0
    for i in range(0,5):
        sig = sig + np.sin(2*np.pi*(i*10)*t)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.plot(t, sig)
    ax1.set_title('10 Hz and 50 Hz sinusoids')
    ax1.axis([0, 1, -5, 5])
    
    #Signal Filtering at custom value
    sos = signal.butter(10, int(signal_filter_value), filter_type, fs=1000, output='sos')
    filtered = signal.sosfilt(sos, sig)
    ax2.plot(t, filtered)
    ax2.set_title('After ' + str(signal_filter_value) + ' Hz ' + str(filter_type) + ' filter')
    ax2.axis([0, 1, -5, 5])
    ax2.set_xlabel('Time [seconds]')
    plt.tight_layout()
    plt.show()
    plt.show()

def low_high_pass(filter_type,filter_order,cutoff_freq,signal_filter_value):
    if filter_type == 'Lowpass':
       generate_graph_low_high('lowpass',filter_order,cutoff_freq,signal_filter_value)
    elif filter_type == 'Highpass':
       generate_graph_low_high('highpass',filter_order,cutoff_freq,signal_filter_value)
    