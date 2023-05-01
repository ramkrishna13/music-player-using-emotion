from keras.preprocessing.image import img_to_array
import imutils
import cv2
from tensorflow.keras.models import load_model
import numpy as np
import pause
import playsound
import random
c=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0


# parameters for loading data and images
detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'


face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised", "neutral"]

#cv2.namedWindow('your_face')
camera = cv2.VideoCapture(0)
while True:
    c=c+1
    frame = camera.read()[1]
    # reading the frame
    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                            flags=cv2.CASCADE_SCALE_IMAGE)

    cv2.imshow("Face",frame)
    cv2.waitKey(1)
    canvas = np.zeros((250, 300, 3), dtype="uint8")
    frameClone = frame.copy()
    if len(faces) > 0:
        faces = sorted(faces, reverse=True,
                       key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
        # the ROI for classification via the CNN
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        #print("emotion_probability",emotion_probability)
        label = EMOTIONS[preds.argmax()]
        print("label",label)

        if label=="happy":
            count1=count1+1
            L = ['happy1.mp3', 'happy2.mp3','happy3.mp3']
            S = random.randint(0, 2)
            print("S", S)
            playsound.playsound(L[S], True)
        elif label=="angry":
            count2 = count2 + 1
            L = ['angry1.mp3', 'angry2.mp3','angry3.mp3']
            S = random.randint(0, 2)
            print("S", S)
            playsound.playsound(L[S], True)
        elif label == "surprised":
            count3 = count3 + 1
            L = ['surprise1.mp3', 'surprise2.mp3']
            S = random.randint(0, 1)
            print("S", S)
            playsound.playsound(L[S], True)
        elif label=="disgust":
            count4 = count4 + 1
            L = ['disguist1.mp3', 'disguist2.mp3']
            S = random.randint(0, 1)
            print("S", S)
            playsound.playsound(L[S], True)
        elif label=="sad":
            count5 = count5 + 1
            L = ['sad1.mp3', 'sad2.mp3','sad3.mp3']
            S = random.randint(0, 1)
            print("S", S)
            playsound.playsound(L[S], True)
        elif label=="scared":
            count6 = count6 + 1
            L = ['scared1.mp3', 'scared2.mp3']
            S = random.randint(0, 1)
            print("S", S)
            playsound.playsound(L[S], True)
        elif label=="neutral":
            count7 = count7 + 1
            L = ['neutral1.mp3', 'neutral2.mp3','neutral3.mp3']
            S = random.randint(0, 1)
            print("S", S)
            playsound.playsound(L[S], True)

    else:
        continue

    for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
        # construct the label text
        text = "{}: {:.2f}%".format(emotion, prob * 100)

        # draw the label + probability bar on the canvas
        # emoji_face = feelings_faces[np.argmax(preds)]


        w = int(prob * 300)
        cv2.rectangle(canvas, (7, (i * 35) + 5),
                      (w, (i * 35) + 35), (0, 0, 255), -1)
        cv2.putText(canvas, text, (10, (i * 35) + 23),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                    (255, 255, 255), 2)
        cv2.putText(frameClone, label, (fX, fY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                      (0, 0, 255), 2)
    # for c in range(0, 3):
    #        frame[200:320, 10:130, c] = emoji_face[:, :, c] * \
    #        (emoji_face[:, :, 3] / 255.0) + frame[200:320,
    #        10:130, c] * (1.0 - emoji_face[:, :, 3] / 255.0)



    cv2.imshow('your_face', frameClone)
    cv2.imshow("Probabilities", canvas)
    cv2.waitKey(1)

#Add your songs in here in if statements
    if label == "happy":
        print('Hi')
        #pause.seconds(3)
    #if c > 8:
     #   break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
