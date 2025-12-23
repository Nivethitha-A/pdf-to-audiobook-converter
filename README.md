# PDF to Audiobook Converter

## 📌 Overview
The PDF to Audiobook Converter is a Python-based application that converts PDF documents into spoken audio.  
It helps users listen to PDF content instead of reading, making it useful for students, visually impaired users, and audiobook creation.

The project is implemented as a **desktop GUI application using Tkinter**, following the tools and requirements specified in the problem statement.

---

## 🎯 Objective
To extract text from PDF files and convert it into speech with control options such as speed and volume.

---

## 🛠️ Technologies Used
- Python
- Tkinter (GUI)
- PyMuPDF (PDF text extraction)
- pyttsx3 (Offline Text-to-Speech)
- gTTS (MP3 export)

---

## ✨ Features
- Upload PDF files
- Extract and clean text from PDFs
- Convert text into speech
- Play audio directly
- Export audio as MP3
- Control speech speed and volume
- User-friendly GUI

---

## 📂 Project Structure
```
pdf_to_audiobook/
│
├── main.py # Tkinter GUI application
├── pdf_reader.py # PDF text extraction logic
├── tts_engine.py # Text-to-speech functionality
├── utils.py # Text cleaning utilities
├── requirements.txt # Required Python libraries
│
├── assets/
│ └── samples/ # Sample PDF files
│
├── output/
│ └── converted_audio/ # Generated MP3 files
│
└── README.md
```


---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
2️⃣ Run the Application
```
python main.py
```
---
📎 Sample Files
Sample PDF files are available in assets/samples/

Generated audio files are saved in output/converted_audio/
---

🎓 Academic Note
This project was developed as a mini-project following the given problem statement using Tkinter.
A web-based version using Flask can be considered as a future enhancement.
---

🚀 Future Enhancements
Pause and resume audio

Language selection

Chapter-wise audio generation

Web-based interface

Cloud deployment
