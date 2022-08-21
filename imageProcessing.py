from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage


def blur_img(blur_level):
    face = misc.face(gray=True)
    kernel = np.outer(signal.windows.gaussian(70, int(blur_level)),signal.windows.gaussian(70, int(blur_level)))
    blurred = signal.fftconvolve(face, kernel, mode='same')

    fig, (ax_orig, ax_kernel, ax_blurred) = plt.subplots(3, 1,figsize=(6, 15))

    #Original Image
    ax_orig.imshow(face, cmap='gray')
    ax_orig.set_title('Original')
    ax_orig.set_axis_off()

    #Gaussian kernel
    ax_kernel.imshow(kernel, cmap='gray')
    ax_kernel.set_title('Gaussian kernel')
    ax_kernel.set_axis_off()

    #Blurred image
    ax_blurred.imshow(blurred, cmap='gray')
    ax_blurred.set_title('Blurred')
    ax_blurred.set_axis_off()
    plt.show()

def edge_finder(sharp_level):

    im =  misc.face(gray=True)
    data = np.array(im, dtype=float)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    ax1.imshow(data, cmap='gray')
    ax1.set_title('Original')

    lowpass = ndimage.gaussian_filter(data, int(sharp_level))
    gauss_highpass = data - lowpass
    
    ax2.imshow(gauss_highpass, cmap='gray')
    ax2.set_title(r'Gaussian Highpass, $\sigma = ' + str(sharp_level) + '  pixels$')

    plt.show()

