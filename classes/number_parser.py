import pickle
import cv2

class Number_Parser:    
    def __init__(self):
        self.number_contours = pickle.load(open('number_images.dump', 'rb'))

    def get_digit(self, digit_img):
        digit_img = cv2.threshold(digit_img, 127, 255, cv2.THRESH_BINARY)[1]
        #digit_contours, _ = cv2.findContours(digit_img, cv2.RETR_CCOMP , cv2.CHAIN_APPROX_NONE)

        digit = 0
        match = 0.0
        for i in range(len(self.number_contours)):
            ret = cv2.matchShapes(self.number_contours[i], digit_img, 1, 0.0)
            #print(f"%s -> %s" % (i, ret))
            if i == 0:
                digit = 0
                match = ret
            elif ret < match:
                digit = i
                match = ret
    
        return digit
    
    def get_number(self, digit_images):
        total = 0
        position = length = len(digit_images)
        for i in range(length):
            position -= 1
            digit = self.get_digit(digit_images[i])
            total += digit * (10 ** position)
            
        
        return total