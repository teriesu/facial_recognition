import cv2

captureVideo = cv2.VideoCapture(0)
if not captureVideo.isOpened():
    print("Keine Camera gefunden")
    exit()

while True:
    _, frame = captureVideo.read() #La primera variable recibe el timpo de camara
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

captureVideo.release()
cv2.destroyAllWindows()
