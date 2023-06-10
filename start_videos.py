import cv2
#0 for default camera, 1 for 2nd camera or video file name
cap = cv2.VideoCapture('vtest.avi')
#fourcc codec for video formats
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#20fps
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()