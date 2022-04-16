import cv2

path = 'images/000638587.jpg'

center = (815, 347)

img = cv2.imread(path)

cv2.circle(img, center, 5,  (0,255,0), 3)

cv2.imshow("plot", img)

if cv2.waitKey(0) == 'q':
    cv2.destroyAllWindows()
