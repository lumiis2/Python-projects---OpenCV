import cv2

#capturar video
cap =cv2.VideoCapture(0) #captura a webcam

#carrega o har cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#criar loop infinito

while(True):

    #recupera frame
    ret, frame = cap.read()

    #cria um gray
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detecta as faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #checa as faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)

    #mostra frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    #recura botao apertado
    key = cv2.waitKey(30) #delay do video

    if key == ord('q'):
        break

#libera o cache do cap
cap.release()

#destroi as janelas
cv2.destroyAllWindows()