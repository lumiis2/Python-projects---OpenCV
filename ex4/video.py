import cv2
import os
import numpy as np


# funcoes
def saveimg():
    global ultimonome
    global boolsave
    print('qual seu nome?')
    name = input()
    ultimonome = name
    boolsave = True

def traindata():
    global treined
    global persons
    treined = True
    persons = os.listdir('train')
    ids = []
    faces = []

    for i, p in enumerate(persons):
        for f in os.listdir(f'train/{p}'):
            img = cv2.imread(f'train/{p}/{f}', 0)
            faces.append(img)
            ids.append(i)
    recognizer.train(faces, np.array(ids))

def save(img):
    global ultimonome
    if not os.path.exists('train'):
        os.makedirs('train')
    if not os.path.exists(f'train/{ultimonome}'):
        os.makedirs(f'train/{ultimonome}')
    files = os.listdir(f'train/{ultimonome}')
    cv2.imwrite(f'train/{ultimonome}/{str(len(files))}.jpg', img)




ultimonome = ''
boolsave = False
savecount = 0
recognizer = cv2.face.LBPHFaceRecognizer_create()
treined = False
persons= ''

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

        #cria um roi
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (50,50))
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
        
        if treined:
            idf, conf = recognizer.predict(roi)
            nameP = persons[idf]
            cv2.putText(frame, nameP, (x,y), 3, 2, (0, 0, 0), 1, cv2.LINE_AA)

        if boolsave == True:
            save(roi)
            savecount +=1

        if savecount > 50:
            boolsave = False
            savecount = 0

    #mostra frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    

    #recura botao apertado
    key = cv2.waitKey(30) #delay do video

    if key == ord('s'):
        saveimg()

    if key == ord('t'):
        traindata()

    if key == ord('q'):
        break

#libera o cache do cap
cap.release()

#destroi as janelas
cv2.destroyAllWindows()