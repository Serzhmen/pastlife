import cv2
import numpy as np
# import scipy

#Read the image
image = cv2.imread('seamlessclone.jpg')

#greyscale filter
def greyscale(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return greyscale

    #making the greyscale image
a1 = greyscale(image)

filename = 'greyscale.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a1)

# brightness adjustment
def bright(img, beta_value ):
    img_bright = cv2.convertScaleAbs(img, beta=beta_value)
    return img_bright

#making the  more bright image
#positive beta value
a2 = bright(image, 60)

filename = 'more_bright.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a2)

#making the  less bright image
#negative beta value
a3 = bright(image, -60)

filename = 'less_bright.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a3)

#sharp effect
def sharpen(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    img_sharpen = cv2.filter2D(img, -1, kernel)
    return img_sharpen

#making the sharp image
a4 = sharpen(image)
filename = 'sharpen.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a4)

#sepia effect
def sepia(img):
    img_sepia = np.array(img, dtype=np.float64) # converting to float to prevent loss
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    img_sepia[np.where(img_sepia > 255)] = 255 # normalizing values greater than 255 to 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return img_sepia

#making the sepia image
a5 = sepia(image)
filename = 'sepia.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a5)

#grey pencil sketch effect
def pencil_sketch_grey(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_gray

#making the grey pencil sketch
a6 = pencil_sketch_grey(image)

filename = 'pencil_grey.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a6)

#colour pencil sketch effect
def pencil_sketch_col(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_color

#making the colour pencil sketch
a7 = pencil_sketch_col(image)
filename = 'pencil_col.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a7)

#HDR effect
def HDR(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return  hdr

#making the hdr img
a8 = HDR(image)

filename = 'HDR.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a8)

# invert filter
def invert(img):
    inv = cv2.bitwise_not(img)
    return inv

#making the invert img
a9 = invert(image)
filename = 'invert.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a9)

