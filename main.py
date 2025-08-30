import cv2

face_cap = cv2.CascadeClassifier("C:/Users/Abhinav/appdata/local/programs/python/python313/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")


#To enable Camera
video_cap = cv2.VideoCapture(0)
while True:
    ret , video_data = video_cap.read()
    col = cv2.cvtColor(video_data, )
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("a"):
        break   
video_cap.release()