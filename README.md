# Dutch Sign Language Letter Detection

This program uses your webcam to detect hand signs from the **Dutch Sign Language (NGT)** alphabet. A word is generated for you to spell out — one letter at a time — using your hands.

---

## Getting Started

### 1. Download the Repository

Clone or download this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
```

---

### 2. Set Up the Environment

Make sure you have **Python 3.8+** installed. Then create a virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Build the Executable

From the **project root folder**, run:

```bash
pyinstaller --onefile --collect-all mediapipe --collect-all sklearn --add-data "models/sign_model_rf.pkl;models" scripts/Practice.py
```

This will generate `Practice.exe` inside the `dist/` folder.

---

### 4. Run the Program

Navigate to the `dist/` folder and double-click **`Practice.exe`**, or run it via terminal:

```bash
cd dist
./Practice.exe
```

---

## How It Works

1. When the program starts, a **random word** is generated for you to spell out in Dutch Sign Language.
2. The program waits for you to **press the corresponding letter key** on your keyboard to indicate which letter you are signing.
3. Once a key is pressed, the webcam activates and begins **detecting your hand sign** for that letter.
4. Spell out the entire word correctly to complete the exercise.

---

## Requirements

- Python 3.8+
- A working webcam
- Windows OS

---

## Tips

- Make sure your hand is clearly visible and well-lit in front of the camera.
- Hold the sign steady for best detection results.
- Press the correct letter key on your keyboard **before** showing the sign.
