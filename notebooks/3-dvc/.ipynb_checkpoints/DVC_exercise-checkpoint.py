import fire
import cv2
import json


def preprocess(inputpath,outputpath,X_SIZE,Y_SIZE):
    img = cv2.imread(inputpath, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(X_SIZE,Y_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(outputpath, img)
    
def classify(inputpath, outputpath):
    img = cv2.imread(inputpath, cv2.IMREAD_GRAYSCALE)
    circles = cv2.HoughCircles(img, 
                        cv2.HOUGH_GRADIENT,
                        dp=2, 
                        minDist=15, 
                        param1=100, 
                        param2=70)
        
    classes = dict()
    if circles is None:
        classes['class']='banana'
    else:
        classes['class']='lemon'
    with open(outputpath, 'w') as fp:
            json.dump(classes, fp)
    
if __name__ == '__main__':
  fire.Fire()