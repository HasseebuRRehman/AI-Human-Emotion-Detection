
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from deepface import DeepFace

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Images", "*.jpg *.jpeg *.png")]
    )

    if not file_path:
        return

    try:
        image = Image.open(file_path)
        image.thumbnail((350, 300))

        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

        result_label.config(text="Analyzing...")

        result = DeepFace.analyze(
            img_path=file_path,
            actions=['emotion'],
            enforce_detection=False
        )

        if isinstance(result, list):
            result = result[0]

        scores = result['emotion']

        emotions = {
            "Happy": scores['happy'],
            "Sad": scores['sad'],
            "Angry": scores['angry'],
            "Fear": scores['fear'],
            "Surprise": scores['surprise'],
            "Disgust": scores['disgust'],
            "Neutral": scores['neutral'],
            "Excited": scores['happy'],
            "Confused": scores['surprise'],
            "Worried": scores['fear'],
            "Tired": scores['neutral'],
            "Bored": scores['neutral'],
            "Calm": scores['neutral'],
            "Shy": scores['happy'],
            "Curious": scores['surprise'],
            "Frustrated": scores['angry'],
            "Proud": scores['happy'],
            "Embarrassed": scores['sad'],
            "Crying": scores['sad'],
            "Laughing": scores['happy']
        }

        emotion = max(emotions, key=emotions.get)

        result_text = (
            f"Detected Expression: {emotion}\n\n"
            f"Matching Score: {emotions[emotion]:.2f}%\n\n"
            "Note: This is an estimated label."
        )

        result_label.config(text=result_text)

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("AI Human Emotion Detection")
root.geometry("550x650")
root.configure(bg="#202b3c")

title = tk.Label(
    root,
    text="AI Human Emotion Detection",
    font=("Arial", 20, "bold"),
    bg="#202b3c",
    fg="white"
)
title.pack(pady=25)

upload_button = tk.Button(
    root,
    text="Upload Human Picture",
    font=("Arial", 14, "bold"),
    bg="#2196F3",
    fg="white",
    command=upload_image
)
upload_button.pack(pady=15)

image_label = tk.Label(root, bg="#202b3c")
image_label.pack(pady=15)

result_label = tk.Label(
    root,
    text="Upload a picture",
    font=("Arial", 14),
    bg="#202b3c",
    fg="white",
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()
