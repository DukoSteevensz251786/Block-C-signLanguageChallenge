import cv2
import mediapipe as mp
import pickle
import numpy as np


import sys
import os

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)




mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


hands = mp_hands.Hands(
    max_num_hands=1,              
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)




with open(resource_path("models/sign_model_rf.pkl"), "rb") as f:
    model = pickle.load(f)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    predicted_label = "No hand"

    if results.multi_hand_landmarks:
  
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS) #DEBUGGING, SHOW CONNECTIONS
        
    
        landmarks = []
        for lm in hand_landmarks.landmark:
            landmarks.extend([lm.x, lm.y, lm.z])

        X = np.array(landmarks).reshape(1, -1)  

        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0].max()

        if prob > 0.7:  
            predicted_label = f'{pred}'
            #predicted_label = f"{pred} ({prob:.2f})"
        elif prob > 0.3 and prob < 0.7:
            predicted_label = f"? ({pred}) ({prob:.2f})"
        else:
            predicted_label = "Not recognised"
        

 
    cv2.putText(frame, predicted_label, (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,188,255), 3)
    

    cv2.imshow("Sign Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()