import tkinter as tk
from tkinter import filedialog, messagebox
import threading

from pdf_reader import extract_text_from_pdf
from utils import clean_text
from tts_engine import speak_offline, save_mp3


# ---------- WINDOW ----------
root = tk.Tk()
root.title("PDF to Audiobook Converter")
root.geometry("600x420")
root.resizable(False, False)
root.configure(bg="#f4f6f8")

pdf_path = tk.StringVar(value="No file selected")
status = tk.StringVar(value="Ready")

# ---------- FUNCTIONS ----------
def browse_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file:
        pdf_path.set(file)
        status.set("PDF loaded")

def play_audio():
    if "No file" in pdf_path.get():
        messagebox.showwarning("Warning", "Select a PDF first")
        return

    raw = extract_text_from_pdf(pdf_path.get())
    text = clean_text(raw)

    if not text:
        messagebox.showerror("Error", "PDF contains no readable text")
        return

    rate = speed.get()
    volume = vol.get() / 100

    status.set(f"Playing (Speed={rate}, Volume={vol.get()}%)")

    threading.Thread(
        target=speak_offline,
        args=(text, rate, volume)
    ).start()

def export_audio():
    if "No file" in pdf_path.get():
        messagebox.showwarning("Warning", "Select a PDF first")
        return

    raw = extract_text_from_pdf(pdf_path.get())
    text = clean_text(raw)

    if not text:
        messagebox.showerror("Error", "PDF contains no readable text")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 Files", "*.mp3")]
    )

    if save_path:
        save_mp3(text, save_path)
        status.set("MP3 exported successfully")


# ---------- MAIN FRAME ----------
frame = tk.Frame(root, bg="white", padx=25, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------- TITLE ----------
tk.Label(
    frame,
    text="PDF to Audiobook Converter",
    font=("Segoe UI", 18, "bold"),
    bg="white"
).grid(row=0, column=0, columnspan=3, pady=(0, 10))

tk.Label(
    frame,
    text="Convert PDF documents into spoken audio",
    fg="gray",
    bg="white"
).grid(row=1, column=0, columnspan=3, pady=(0, 15))

# ---------- FILE ----------
tk.Button(
    frame, text="Upload PDF", width=15,
    command=browse_pdf
).grid(row=2, column=0, pady=5)

tk.Label(
    frame, textvariable=pdf_path,
    wraplength=380, fg="blue", bg="white"
).grid(row=2, column=1, columnspan=2, padx=10)

# ---------- SPEED ----------
tk.Label(frame, text="Speed", bg="white").grid(row=3, column=0, pady=10)
speed = tk.Scale(frame, from_=100, to=250, orient="horizontal", length=220)
speed.set(150)
speed.grid(row=3, column=1, columnspan=2)

# ---------- VOLUME ----------
tk.Label(frame, text="Volume", bg="white").grid(row=4, column=0)
vol = tk.Scale(frame, from_=0, to=100, orient="horizontal", length=220)
vol.set(100)
vol.grid(row=4, column=1, columnspan=2)

# ---------- BUTTONS ----------
tk.Button(
    frame, text="Play Audio", width=18,
    bg="#2196F3", fg="white",
    command=play_audio
).grid(row=5, column=0, columnspan=3, pady=(15, 5))

tk.Button(
    frame, text="Save as MP3", width=18,
    bg="#4CAF50", fg="white",
    command=export_audio
).grid(row=6, column=0, columnspan=3)

# ---------- STATUS ----------
tk.Label(
    root, textvariable=status,
    bg="#f4f6f8", fg="gray"
).pack(side="bottom", pady=8)

root.mainloop()
