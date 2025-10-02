import os
import shutil
import tkinter as tk
from tkinter import simpledialog, filedialog
from PIL import Image, ImageTk
from transformers import pipeline

# ---------------------------
# OOP Model Layer
# ---------------------------

class BaseModel:
    """Base model class (Parent)"""
    def __init__(self, name):
        self.name = name
    
    def run_model(self, data):
        return f"[BaseModel] {self.name} processed: {data}"

class HFTextModel(BaseModel):
    """Child class: Hugging Face Sentiment Model"""
    def __init__(self, name, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        super().__init__(name)
        self._model = pipeline("sentiment-analysis", model=model_name)  # encapsulation
    
    def run_model(self, text):   # method overriding
        result = self._model(text)
        return result

# ---------------------------
# Directory & File Manager
# ---------------------------

class Directory:
    def __init__(self, name):
        self.name = name

    def create(self):
        if not os.path.exists(self.name):
            os.makedirs(self.name)

    def add_file(self, file_name, content=None, image_path=None):
        path = os.path.join(self.name, file_name)
        if content is not None:
            with open(path, "w") as f:
                f.write(content)
        elif image_path is not None:
            shutil.copy(image_path, path)

# ---------------------------
# GUI Frames
# ---------------------------

class DirectoryFrame(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Directory & File Manager", padx=10, pady=10)
        self.pack(fill="x", padx=10, pady=5)

        self.dir_name_var = tk.StringVar()
        tk.Label(self, text="Directory Name:").pack(anchor="w")
        tk.Entry(self, textvariable=self.dir_name_var).pack(fill="x", pady=5)

        tk.Button(self, text="Create Directory", command=self.create_directory).pack(pady=2)
        tk.Button(self, text="Add Text File", command=self.add_text_file).pack(pady=2)
        tk.Button(self, text="Add Image File", command=self.add_image_file).pack(pady=2)
        tk.Button(self, text="List Files", command=self.list_files).pack(pady=2)

        self.file_listbox = tk.Listbox(self)
        self.file_listbox.pack(fill="both", pady=5)
        self.file_listbox.bind("<<ListboxSelect>>", self.show_file)

        self.dir_obj = None
        self.file_frame = None

    def create_directory(self):
        name = self.dir_name_var.get()
        if not name:
            return
        self.dir_obj = Directory(name)
        self.dir_obj.create()
        self.list_files()

    def add_text_file(self):
        if not self.dir_obj:
            return
        file_name = simpledialog.askstring("Text File Name", "Enter file name (with .txt):")
        content = simpledialog.askstring("Content", "Enter file content:")
        if file_name and content is not None:
            self.dir_obj.add_file(file_name, content=content)
        self.list_files()

    def add_image_file(self):
        if not self.dir_obj:
            return
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
        if file_path:
            file_name = os.path.basename(file_path)
            self.dir_obj.add_file(file_name, image_path=file_path)
        self.list_files()

    def list_files(self):
        self.file_listbox.delete(0, tk.END)
        if self.dir_obj and os.path.exists(self.dir_obj.name):
            for f in os.listdir(self.dir_obj.name):
                self.file_listbox.insert(tk.END, f)

    def show_file(self, event):
        if not self.dir_obj:
            return
        selection = self.file_listbox.curselection()
        if not selection:
            return
        file_name = self.file_listbox.get(selection[0])
        path = os.path.join(self.dir_obj.name, file_name)

        # Clear previous content
        if self.file_frame:
            self.file_frame.destroy()

        if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            img = Image.open(path)
            img = img.resize((200, 200))
            photo = ImageTk.PhotoImage(img)
            self.file_frame = tk.Label(self, image=photo)
            self.file_frame.image = photo
            self.file_frame.pack(pady=5)

        elif file_name.lower().endswith(".txt"):
            with open(path, "r") as f:
                content = f.read()
            self.file_frame = tk.Text(self, height=10)
            self.file_frame.insert(tk.END, content)
            self.file_frame.pack(fill="both", pady=5)

class ModelFrame(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Run Hugging Face Model", padx=10, pady=10)
        self.pack(fill="x", padx=10, pady=5)

        tk.Label(self, text="Enter text for analysis:").pack(anchor="w")
        self.text_input = tk.Text(self, height=5)
        self.text_input.pack(fill="both", pady=5)

        tk.Button(self, text="Run Sentiment Model", command=self.run_model).pack(pady=2)

        self.result_text = tk.Text(self, height=5)
        self.result_text.pack(fill="both", pady=5)

        # Polymorphism: BaseModel type can hold HFTextModel
        self.model: BaseModel = HFTextModel("Sentiment Model")

    def run_model(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            result = self.model.run_model(text)  # overridden method in HFTextModel
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, str(result))

# ---------------------------
# Main App
# ---------------------------

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Manager + Hugging Face Model")
        self.geometry("650x700")

        self.dir_frame = DirectoryFrame(self)
        self.model_frame = ModelFrame(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
