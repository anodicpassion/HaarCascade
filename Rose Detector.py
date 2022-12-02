import cv2


def null(e=None):
    pass


rose_img = cv2.imread("rose image.jpg")

scale_factor = 50
minimum_neighbour = 35

cv2.namedWindow("Rose Detector")
cv2.createTrackbar("Scale Factor", "Rose Detector", scale_factor, 100, null)
cv2.createTrackbar("Minimum Neighbour", "Rose Detector", minimum_neighbour, 100, null)

rose_detector = cv2.CascadeClassifier("rose_classifier.xml")

while 1:
    img = rose_img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    scale_factor, minimum_neighbour = cv2.getTrackbarPos("Scale Factor", "Rose Detector") / 10, \
                                      cv2.getTrackbarPos("Minimum Neighbour", "Rose Detector")
    if scale_factor <= 1:
        scale_factor = 1.1

    print(scale_factor, minimum_neighbour)
    roses = rose_detector.detectMultiScale(img_gray, scaleFactor=scale_factor, minNeighbors=minimum_neighbour)
    for rose in roses:
        x, y, w, h = rose
        x, y, w, h = x-50, y-50, w+50, h+50
        cv2.rectangle(img, (x, y), (x + w, y + h), (50, 255, 50), 2)

    cv2.imshow("Rose Detector", img)

    key_stroke = cv2.waitKey(1000)
    if key_stroke in [13, 27]:
        cv2.destroyAllWindows()
        break
