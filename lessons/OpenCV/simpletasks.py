import cv2
import numpy as np

candy = cv2.imread("images/cotton-candy.png", cv2.IMREAD_COLOR)
print(candy.shape[:3])
obsidian = cv2.imread("images/obsidian.jpeg", cv2.IMREAD_COLOR)
print(obsidian.shape[:3])

#show the image as is
#cv2.imshow("image", obsidian)
#cv2.waitKey(0)


#turn the image into a grayscale
gray_image = cv2.cvtColor(candy, cv2.COLOR_BGR2GRAY)
cv2.imwrite('images/candy-gray.jpg', gray_image)
#cv2.imshow('Grayscale', gray_image)
#cv2.waitKey(0)


edges = cv2.Canny(gray_image, 100, 200)

#cv2.imwrite('images/obsidian-edges.jpg', edges)
