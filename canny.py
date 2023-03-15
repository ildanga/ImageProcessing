import cv2

def cannyEdge(src) :

    dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    dst = cv2.Canny(dst, 100, 200, apertureSize=3, L2gradient=True)

    return dst
