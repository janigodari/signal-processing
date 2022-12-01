from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def correlation(nr_pulses):
    sig = 0
    rng = np.random.default_rng()

    if len(nr_pulses) == 0:
        default_pattern = [1. if i % 2 == 0 else 0. for i in range(10)]
        sig = np.repeat(default_pattern, 128)
    else:
        pulses = [int(nr_pulses[i]) for i in range(10)]
        sig = np.repeat(pulses, 128)

    sig_noise = sig + rng.standard_normal(len(sig))
    corr = signal.correlate(sig_noise, np.ones(128), mode='same') / 128

    clock = np.arange(64, len(sig), 128)
    fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, sharex=True)
    ax_orig.plot(sig)
    ax_orig.plot(clock, sig[clock], 'ro')
    ax_orig.set_title('Original signal')
    ax_noise.plot(sig_noise)

    ax_noise.set_title('Signal with noise')
    ax_corr.plot(corr)
    ax_corr.plot(clock, corr[clock], 'ro')
    ax_corr.axhline(0.5, ls=':')
    
    ax_corr.set_title('Cross-correlated with rectangular pulse')
    ax_orig.margins(0, 0.1)
    fig.tight_layout()
    plt.show()
