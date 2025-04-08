# 🎵 Basic-Soundboard Terminal - Python

A small and simple **soundboard script for the terminal**, written in Python. Press a key, and it plays a sound. Useful for streams, memes, or just having fun locally.

---

## ⚙️ Features

- ✅ Instant sound playback via keyboard
- 🔁 Easy to add your own files
- 🎧 Works entirely in the terminal
- ⏱️ Blocking playback (one sound at a time)
- 📁 All sounds must be placed inside the `Soundboard/` folder
- ❌ Clean exit with the `-` key

---

## 🎮 Keyboard Commands

| Key   | Action                         |
|-------|--------------------------------|
| `1`   | Play sound: `Welcome.mp3`      |
| `2`   | Play sound: `place_your_track_here.mp3` |
| `-`   | Exit the soundboard            |

> You can easily add more keys by duplicating a code block in `soundboard.py`.

---

## 🚀 Running the Script
 ``python soundboard.py``
 ### 📁 Files & Folders

- `soundboard.py` → the main script  
- `Soundboard/` → place your files here (e.g. `Welcome.mp3`)

---

## 🧪 Requirements

- Python 3.x
- Modules: `pygame`, `keyboard`

### Install the modules:

bash
```pip install pygame keyboard```

## ⚠️ Notes
Admin privileges may be required on some systems (especially Windows).

## Author & Credits
🛠️ Script developed by [DBZ-Z]

💬 Need extra features? Feel free to open an issue or make a pull request.

⚡ Disclaimer
This script is meant for local terminal use.
It may require elevated permissions to detect keyboard inputs.
Not compatible with Jupyter notebooks or online environments. 
