import streamlit as st
import numpy as np
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt

st.title('Image Processing')

# Load the original image
original_image = Image.open("image4.jpg")

# Function to resize image
def resize_image(image, width, height):
    return image.resize((width, height))

# Function to convert to grayscale
def grayscale(image):
    return ImageOps.grayscale(image)

# Function to crop image
def crop_image(image, x, y, w, h):
    return image.crop((x, y, x+w, y+h))

# Function to rotate image
def rotate_image(image, angle):
    return image.rotate(angle, expand=True)

# Function to blur image
def blur_image(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

# Processing
resized_image = resize_image(original_image, 400, 400)
grayscale_image = grayscale(resized_image)
cropped_image = crop_image(grayscale_image, 0, 0, 200, 200)
rotated_image = rotate_image(cropped_image, 45)
blurred_image = blur_image(rotated_image, 5)

# Plot all images in a single plot
plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(232)
plt.imshow(resized_image, cmap='gray')
plt.title('Resized Image')
plt.axis('off')

plt.subplot(233)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(234)
plt.imshow(cropped_image, cmap='gray')
plt.title('Cropped Image')
plt.axis('off')

plt.subplot(235)
plt.imshow(rotated_image, cmap='gray')
plt.title('Rotated Image')
plt.axis('off')

plt.subplot(236)
plt.imshow(blurred_image, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')

plt.tight_layout()
st.pyplot(plt)
