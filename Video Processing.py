import cv2

# Opens the Video file
cap = cv2.VideoCapture('Videos/hh.mp4')
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.imshow('test',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

    cv2.imwrite( str(i) + '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()