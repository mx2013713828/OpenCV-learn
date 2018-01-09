# encoding:utf-8

import cv2
import numpy as np

image = cv2.imread('girl.jpg')
cv2.namedWindow("Image")
image = cv2.Canny(image,250,350)

#
# kernel_x = np.array([[-1, 0, 1],
#                    [-2, 0, 2],
#                    [-1, 0, 1]])
#
# kernel_y = np.array([[1, 2, 1],
#                 [0, 0, 0],
#                 [-1, -2, -1]])
#
# # Step2. 初始化中间结果矩阵
# gx = np.zeros(image.shape, dtype = np.uint8)
# gy = np.zeros(image.shape, dtype = np.uint8)
#
# # Step3. 使用自定义的卷积核进行卷积
# cv2.filter2D(image, -1, kernel_x, gx)
# cv2.filter2D(image, -1, kernel_y, gy)
# # 显示卷积的中间结果
# cv2.imshow("gx", gx)
# cv2.imshow("gy", gy)
#
# # Step4. 合并两个图像
# gx = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)
# cv2.imshow("gx2", gx)
#
# # Step5. 阈值抑制处理
# thresh = 50 #阈值设置为50
# ret, dst = cv2.threshold(gx, thresh, 255, cv2.THRESH_BINARY)
# cv2.imshow("ss", dst)
cv2.imshow("Image",image)
cv2.waitKey(0)