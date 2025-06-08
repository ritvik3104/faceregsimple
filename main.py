import tkinter as tk
from tkinter import filedialog, messagebox
import face_recognition
import numpy as np
from PIL import Image, ImageTk

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Similarity")
        self.root.geometry("500x300")

        self.label = tk.Label(root, text="Face Similarity Checker", font=("Arial", 16))
        self.label.pack(pady=10)

        self.image1_path = None
        self.image2_path = None

        self.select1_button = tk.Button(root, text="Select First Image", command=self.load_image1)
        self.select1_button.pack(pady=5)

        self.select2_button = tk.Button(root, text="Select Second Image", command=self.load_image2)
        self.select2_button.pack(pady=5)

        self.compare_button = tk.Button(root, text="Compare Faces", command=self.compare_faces)
        self.compare_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def load_image1(self):
        self.image1_path = filedialog.askopenfilename()
        if self.image1_path:
            messagebox.showinfo("Selected", f"Image 1 loaded: {self.image1_path}")

    def load_image2(self):
        self.image2_path = filedialog.askopenfilename()
        if self.image2_path:
            messagebox.showinfo("Selected", f"Image 2 loaded: {self.image2_path}")

    def compare_faces(self):
        if not self.image1_path or not self.image2_path:
            messagebox.showerror("Error", "Please select both images.")
            return

        try:
            img1 = face_recognition.load_image_file(self.image1_path)
            img2 = face_recognition.load_image_file(self.image2_path)

            enc1 = face_recognition.face_encodings(img1)
            enc2 = face_recognition.face_encodings(img2)

            if not enc1 or not enc2:
                raise ValueError("Face not found in one of the images.")

            distance = np.linalg.norm(enc1[0] - enc2[0])
            similarity = max(0, 100 - distance * 100)

            self.result_label.config(text=f"Similarity: {similarity:.2f}%")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
