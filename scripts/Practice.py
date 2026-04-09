import cv2
import mediapipe as mp
import pickle
import numpy as np
import sys
import os
import random

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
words = [
    "cat", "dog", "sun", "hat", "bat", "rat", "pen", "cup", "bed", "red",
    "blue", "green", "run", "jump", "sit", "top", "box", "fox", "tree", "bee",
    "car", "bus", "toy", "ball", "doll", "book", "page", "leaf", "wind", "rain",
    "snow", "ice", "fire", "rock", "sand", "sea", "fish", "bird", "duck", "frog",
    "cow", "pig", "goat", "sheep", "horse", "farm", "barn", "road", "path", "hill",
    "lake", "river", "pond", "boat", "ship", "map", "star", "moon", "sky", "cloud",
    "day", "night", "light", "dark", "warm", "cold", "hot", "cool", "fast", "slow",
    "big", "small", "tall", "short", "long", "wide", "thin", "fat", "old", "new",
    "good", "bad", "happy", "sad", "fun", "play", "game", "sing", "dance", "read",
    "write", "draw", "color", "paint", "build", "make", "fix", "help", "love", "like"
]


word = words[random.randint(0,99)]

hands = mp_hands.Hands(
    max_num_hands=1,               
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)
list_of_letters = []
def resource_path(relative_path):

    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


model_path = resource_path('models/sign_model_rf.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)


SELECTED_LETTER = 'A'


cap = cv2.VideoCapture(0)
dected = False
list_of_letters_str = 'Spelled: '
while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    predicted_label = "No hand"

    if results.multi_hand_landmarks:
    
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        

        landmarks = []
        for lm in hand_landmarks.landmark:
            landmarks.extend([lm.x, lm.y, lm.z])

        X = np.array(landmarks).reshape(1, -1) 

        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0].max()
        
        if pred == SELECTED_LETTER :
            if prob > 0.7 and dected == False:
                dected = True
                predicted_label = f'{pred} Done'
                list_of_letters.append(pred)
                for letter in list_of_letters:
                    list_of_letters_str = list_of_letters_str + letter
                
            elif prob > 0.3:
                predicted_label = f"? ({pred}) ({prob:.2f})"
        else:
            predicted_label = f"Looking for '{SELECTED_LETTER}'..."

    cv2.putText(frame, predicted_label, (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,188,255), 3)
    
    cv2.putText(frame, str(list_of_letters_str), (30, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,188,255), 3)
    cv2.putText(frame, f"Spell the word: {word}", (30, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (20,188,255), 3)
    
    cv2.putText(frame, f"Detecting: {SELECTED_LETTER}", (30, frame.shape[0] - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.putText(frame, "Press A-Z to change letter | ESC to quit", (30, frame.shape[0] - 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,200), 1)

    cv2.imshow("Sign Recognition", frame)

    key = cv2.waitKey(1) & 0xFF
    if word.lower() == list_of_letters_str.lower():
        break
    if key == 27:
        break

    elif key >= ord('a') and key <= ord('z'):
        SELECTED_LETTER = chr(key).upper()
        print(f"Now detecting: {SELECTED_LETTER}")
        dected = False
        list_of_letters = []
    elif key >= ord('A') and key <= ord('Z'):
        SELECTED_LETTER = chr(key)
        print(f"Now detecting: {SELECTED_LETTER}")
    

cap.release()
cv2.destroyAllWindows()