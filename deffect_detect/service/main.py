import cv2
import numpy
import imutils
from skimage.metrics import structural_similarity
#files

def detect(imageA, imageB):
    imageA = cv2.resize(imageA, (1200, 600), interpolation=cv2.INTER_LINEAR)
    imageB = cv2.resize(imageB, (1200, 600), interpolation=cv2.INTER_LINEAR)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    p = 0
    for c in cnts:
        p = p + 1
        (x, y, w, h) = cv2.boundingRect(c)
        # cv2.rectangle(imageA, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 5)


    kernel = numpy.ones((5, 5), numpy.uint8)

    dilation = cv2.dilate(thresh, kernel, iterations=1)

    erosion = cv2.erode(thresh, kernel, iterations=1)

    gradient = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)

    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return imageB


