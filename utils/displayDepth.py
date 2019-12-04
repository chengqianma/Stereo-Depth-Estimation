import cv2
"""
path = "D:/Picture/User.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)
"""

def display_depth(path, depth):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h = len(img)
    w = len(img[0])
    baseline = 0.54
    focal = 0.006
    pixel_size = 4.65 * 0.000001
    disparity = (baseline * focal)/(depth * 2 * pixel_size)
    for i in range(h):
        for j in range(w):
            if abs(img[i][j] - disparity) < 2:
                img[i][j] = 255

    cv2.imwrite("depth_temp.png", img)

# display_depth(gray, 5)
# cv2.imshow("demo", img)
# cv2.waitKey(delay=0)
