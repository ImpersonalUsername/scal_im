from PIL import Image, ImageFilter
import cv2
import numpy as np

# Открыть изображение
input_image_path = "resized_lanczos.png"
original_image = Image.open(input_image_path)

# Задать новый размер
new_size = (512, 384)

# Масштабирование с использованием ближайшего соседа
resized_nearest = original_image.resize(new_size, Image.NEAREST)
resized_nearest.save("resized_nearest.png")

# Масштабирование с использованием билинейной интерполяции
resized_bilinear = original_image.resize(new_size, Image.BILINEAR)
resized_bilinear.save("resized_bilinear.png")

# Масштабирование с использованием бикубической интерполяции
resized_bicubic = original_image.resize(new_size, Image.BICUBIC)
resized_bicubic.save("resized_bicubic.png")

# Масштабирование с использованием сглаживания по Гауссу
resized_gaussian = original_image.filter(ImageFilter.GaussianBlur(radius=2))
resized_gaussian = resized_gaussian.resize(new_size, Image.BICUBIC)  # Используем бикубическую интерполяцию
resized_gaussian.save("resized_gaussian.png")

# Масштабирование с использованием фильтра Ланцоша
resized_lanczos = original_image.resize(new_size, Image.LANCZOS)
resized_lanczos.save("resized_lanczos.png")

# Открыть изображения с использованием OpenCV и отобразить их
original_cv2 = cv2.imread(input_image_path)
resized_nearest_cv2 = cv2.imread("resized_nearest.png")
resized_bilinear_cv2 = cv2.imread("resized_bilinear.png")
resized_bicubic_cv2 = cv2.imread("resized_bicubic.png")
resized_gaussian_cv2 = cv2.imread("resized_gaussian.png")
resized_lanczos_cv2 = cv2.imread("resized_lanczos.png")
# cv2.namedWindow('Resized Lanczos1')
# cv2.resizeWindow('Resized Lanczos1', 700, 700)
cv2.imshow("Original Image", original_cv2)
cv2.imshow("Resized Nearest", resized_nearest_cv2)
cv2.imshow("Resized Bilinear", resized_bilinear_cv2)
cv2.imshow("Resized Bicubic", resized_bicubic_cv2)
cv2.imshow("Resized Gaussian", resized_gaussian_cv2)
cv2.imshow("Resized Lanczos", resized_lanczos_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()
