import cv2
import numpy as np
import pickle

def create_digit_pickle():
    number_contours = [None] * 10

    image_digit = cv2.imread("images/0.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[0] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[0], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[0] = contours[0]

    image_digit = cv2.imread("images/1.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[1] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[1], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[1] = contours[0]

    image_digit = cv2.imread("images/2.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[2] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[2], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[2] = contours[0]

    image_digit = cv2.imread("images/3.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[3] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[3], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[3] = contours[0]

    image_digit = cv2.imread("images/4.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[4] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[4], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[4] = contours[0]

    image_digit = cv2.imread("images/5.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[5] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[5], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[5] = contours[0]

    image_digit = cv2.imread("images/6.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[6] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[6], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[6] = contours[0]

    image_digit = cv2.imread("images/7.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[7] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[7], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[7] = contours[0]

    image_digit = cv2.imread("images/8.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[8] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[8], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[8] = contours[0]

    image_digit = cv2.imread("images/9.png")
    gray = cv2.cvtColor(np.array(cv2.bitwise_not(image_digit)), cv2.COLOR_BGR2GRAY)
    number_contours[9] = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(number_contours[9], cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)
    number_contours[9] = contours[0]

    pickle.dump(number_contours, open('number_contours.dump', 'wb'))