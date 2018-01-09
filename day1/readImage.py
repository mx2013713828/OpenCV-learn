#encoding:utf-8
import cv2

image = cv2.imread('log.jpg')

# print image.item(150,120,0)
# image.itemset((150,120,0),255)
# print image.item(150,120,0)
image[:,:,0]= 0
# cv2.imshow("Image",image)
# cv2.imwrite("log1.jpg",image)
# cv2.waitKey(0)
#
# cv2.imshow("Image",image)#显示图片，第一个参数窗口名，第二个参数图片名
# cv2.destroyWindow("Image")#关闭窗口


#复制感兴趣位置到其它区域~
# image[400:500,400:500]=roi
# cv2.imshow("Image",image)
# cv2.waitKey(0)
