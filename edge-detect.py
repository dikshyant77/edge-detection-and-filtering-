import cv2
import numpy as np
import matplotlib.pyplot as plt

def show(title, img):
    if len(img.shape) ==2:
        plt.imshow(img, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    plt.title(title)
    plt.axis("off")
    plt.show()


img = cv2.imread("Unknown.jpeg")
if img is None:
    print("Image not found! ")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
show("Original Image", gray)

print("Pick an option: ")
print("1. Canny Edge Detection")
print("2. Sobel Edge Detection")
print("3. Laplacian Edge Detection")
print("4. Gaussion Blur")
print("5. Median Blur")

choice = input("Enter 1-5:")

if choice =="1":
    edges = cv2.Canny(gray,100,200)
    show("Canny Edges", edges)

elif choice == "2":
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0,ksize=3)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1,ksize=3)
    sobel = cv2.convertScaleAbs(sx) + cv2.convertScaleAbs(sy)
    show("Sobel Edges", sobel)

elif choice == "3":
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = np.abs(lap).astype(np.uint8)
    show("Laplacian Edges", lap)

elif choice =="4":
    blur = cv2.GaussianBlur(gray, (15,15),0)
    show("Gaussian Blur", blur)

elif choice =="5":
    med = cv2.medianBlur(gray, 35)
    show("Medin Blur", med)

else:
    print("Invalid option!")