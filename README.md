# Dutch Sign Language Letter Detection

This program uses your webcam to detect hand signs from the **Dutch Sign Language (NGT)** alphabet. A word is generated for you to spell out — one letter at a time — using your hands.

---

## Getting Started

### 1. Download the Environment

Clone or download this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
```

Then install the required dependencies. It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 2. Navigate to the Scripts Folder

```bash
cd scripts
```

---

### 3. Run the Program

```bash
python Practice.py
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
- Dependencies listed in `requirements.txt`

---

## Tips

- Make sure your hand is clearly visible and well-lit in front of the camera.
- Hold the sign steady for best detection results.
- Press the correct letter key on your keyboard **before** showing the sign.
