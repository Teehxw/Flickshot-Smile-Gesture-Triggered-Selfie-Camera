# Flickshot

## Smile Gesture Triggered Selfie Camera

Flickshot is a Python computer vision project that uses a webcam to detect a user's face and smile in real time. When a smile is detected, the program starts a countdown and automatically captures a selfie.

The program can also save a selfie manually, making it a simple gesture-controlled camera application built with Python and OpenCV.

---

## Project Overview

| Category | Details |
| --- | --- |
| Project type | Webcam computer vision app |
| Main language | Python |
| Main library | OpenCV |
| Detection method | Haar cascade classifiers |
| Input | Computer webcam |
| Output | Saved selfie images |
| Main feature | Smile-triggered photo capture |

---

## Features

- Real-time webcam video feed
- Face detection using OpenCV
- Smile detection inside the detected face area
- 3-second countdown before taking a selfie
- Automatic selfie capture when a smile is detected
- Manual selfie capture using the keyboard
- White flash effect after a photo is taken
- 5-second cooldown between automatic selfies
- Clean saved images without detection boxes
- Simple keyboard controls for saving and quitting

---

## Languages and Libraries

### Python

Python is used as the main programming language for the full application.

### OpenCV

OpenCV, imported as `cv2`, is used for:

- Opening and reading from the webcam
- Flipping and displaying video frames
- Converting images to grayscale
- Detecting faces and smiles
- Drawing detection rectangles
- Saving selfie images

### time

The built-in Python `time` library is used for:

- The smile countdown timer
- The cooldown timer after a selfie is taken
- Creating unique selfie filenames using timestamps

---

## Computer Vision Files

This project uses Haar cascade XML files for object detection.

| File | Purpose |
| --- | --- |
| `haarcascade_frontalface_alt2.xml` | Detects faces |
| `haarcascade_smile.xml` | Detects smiles |

The cascade files are stored in:

```text
haar_cascades/gpreda__haar-cascades-for-face-detection/
```

---

## Project Structure

```text
Flickshot-Smile-Gesture-Triggered-Selfie-Camera/
├── main.py
├── face_detect.py
├── README.md
├── selfies/
└── haar_cascades/
    └── gpreda__haar-cascades-for-face-detection/
        ├── haarcascade_frontalface_alt2.xml
        └── haarcascade_smile.xml
```

| File or Folder | Description |
| --- | --- |
| `main.py` | Runs the webcam loop, countdown, selfie saving, flash effect, cooldown, and keyboard controls. |
| `face_detect.py` | Contains helper functions for detecting faces, detecting smiles, cropping faces, and drawing detection boxes. |
| `haar_cascades/` | Stores the XML cascade files used by OpenCV. |
| `selfies/` | Stores photos captured by the program. |

---

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install OpenCV

```bash
pip install opencv-python
```

### 3. Run the Program

```bash
python main.py
```

After running the program, a webcam window should open. Smile at the camera to trigger the countdown and take a selfie.

---

## Keyboard Controls

| Key | Action |
| --- | --- |
| `s` | Manually save a selfie |
| `q` | Quit the webcam window |

---

## How It Works

1. The webcam opens using OpenCV.
2. Each frame is flipped horizontally so the camera feels like a mirror.
3. The program searches the frame for faces.
4. For each detected face, it checks the lower half of the face for smiles.
5. If a smile is found, a 3-second countdown starts.
6. When the countdown finishes, the program saves a clean selfie.
7. A short flash effect appears, then the program waits through a cooldown before taking another automatic selfie.

---

## Important Notes

- The program needs webcam permission to work.
- Selfies are saved in the `selfies/` folder.
- The program works best with good lighting and a clearly visible face.
- The cascade paths in `face_detect.py` currently use an absolute path from the original computer. If this project is moved to another folder or computer, those paths may need to be updated.

---

## Summary

Flickshot is a gesture-based selfie camera built with Python and OpenCV. Instead of pressing a camera button, the user can smile to automatically trigger a photo. The project combines webcam input, face detection, smile detection, countdown timing, image saving, and keyboard controls into one simple computer vision application.
