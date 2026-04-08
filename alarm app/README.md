# ⏰ Python Alarm Clock using Pygame

A simple alarm clock built using Python that plays a sound at a specified time. This project demonstrates working with date-time handling and audio playback using the `pygame` library.

---

## 🚀 Features

* Set alarm in **HH:MM:SS AM/PM** format
* Real-time clock checking using `datetime`
* Plays alarm sound using `pygame`
* Lightweight and beginner-friendly

---

## 🛠️ Technologies Used

* Python
* `datetime` module
* `pygame` library

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-alarm-clock.git
cd python-alarm-clock
```

2. Install required library:

```bash
pip install pygame
```

---

## ▶️ How to Run

```bash
python alarm.py
```

Then enter time in the format:

```
HH:MM:SS AM/PM
```

Example:

```
07:30:00 AM
```

---

## 📁 Project Structure

```
python-alarm-clock/
│
├── alarm.py
├── alarm.mp3
└── README.md
```

---

## ⚠️ Important Notes

* Ensure `alarm.mp3` is in the same directory as the script
* For better compatibility, you can use `.wav` format instead of `.mp3`
* The program continuously checks time, so keep it running

---

## 🧠 How It Works

* User inputs alarm time
* Program continuously checks current system time
* When input time matches system time:

  * Alarm sound is played
  * Program waits until sound finishes

---

## 🔧 Future Improvements

* Add GUI using Tkinter
* Multiple alarm support
* Snooze functionality
* Voice-based alarm system

---

## 📌 Author

* Your Name
* GitHub: https://github.com/your-username

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!
