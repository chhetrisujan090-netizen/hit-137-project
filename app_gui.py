import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox


class AIGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter AI GUI")
        self.geometry("750x600")

        # Create Menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        model_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Models", menu=model_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Model Selection Section
        frame_top = ttk.LabelFrame(self, text="Model Selection")
        frame_top.pack(fill="x", padx=10, pady=5)

        self.model_choice = ttk.Combobox(frame_top, values=["Text-to-Image", "Text-to-Text", "Image-to-Text"])
        self.model_choice.current(0)
        self.model_choice.pack(side="left", padx=5, pady=5)

        load_button = ttk.Button(frame_top, text="Load Model", command=self.load_model)
        load_button.pack(side="left", padx=5)

        # User Input Section
        frame_input = ttk.LabelFrame(self, text="User Input Section")
        frame_input.pack(fill="x", padx=10, pady=5)

        self.input_type = tk.StringVar(value="Text")
        tk.Radiobutton(frame_input, text="Text", variable=self.input_type, value="Text").pack(side="left", padx=5)
        tk.Radiobutton(frame_input, text="Image", variable=self.input_type, value="Image").pack(side="left", padx=5)

        browse_button = ttk.Button(frame_input, text="Browse", command=self.browse_file)
        browse_button.pack(side="left", padx=5)

        self.input_text = tk.Entry(frame_input, width=40)
        self.input_text.pack(side="left", padx=5)

        # Model Output Section
        frame_output = ttk.LabelFrame(self, text="Model Output Section")
        frame_output.pack(fill="both", expand=True, padx=10, pady=5)

        tk.Label(frame_output, text="Output Display:").pack(anchor="w")
        self.output_display = scrolledtext.ScrolledText(frame_output, height=6)
        self.output_display.pack(fill="both", expand=True, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        ttk.Button(button_frame, text="Run Model 1", command=self.run_model1).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Run Model 2", command=self.run_model2).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_output).pack(side="left", padx=5)

        # Model Information & Explanation Section
        frame_info = ttk.LabelFrame(self, text="Model Information & Explanation")
        frame_info.pack(fill="both", expand=True, padx=10, pady=5)

        # Left side: Selected Model Info
        tk.Label(frame_info, text="Selected Model Info:").grid(row=0, column=0, sticky="w", padx=5)
        self.model_info = scrolledtext.ScrolledText(frame_info, height=6, width=40)
        self.model_info.grid(row=1, column=0, padx=10, pady=5)
        self.model_info.insert(tk.END,
            "• Model Name: Text-to-Image\n"
            "• Category: Vision (AI Model)\n"
            "• Short Description: This model takes text as input and generates an image output.\n"
        )
        self.model_info.config(state="disabled")  # make it read-only

        # Right side: OOP Concepts Explanation
        tk.Label(frame_info, text="OOP Concepts Explanation:").grid(row=0, column=1, sticky="w", padx=5)
        self.oop_explanation = scrolledtext.ScrolledText(frame_info, height=6, width=40)
        self.oop_explanation.grid(row=1, column=1, padx=10, pady=5)
        self.oop_explanation.insert(tk.END,
            "• Multiple Inheritance: Used in model classes that inherit from both BaseModel and Mixins.\n"
            "• Encapsulation: Applied by keeping internal helper methods private (using _method).\n"
            "• Polymorphism & Overriding: run_model() is overridden in each child class to process differently.\n"
            "• Decorators: Applied to functions for error handling and performance measurement.\n"
        )
        self.oop_explanation.config(state="disabled")  # make it read-only

        # Notes Section
        notes_label = tk.Label(self, text="Notes: This project demonstrates Tkinter GUI + OOP concepts with simple AI model structure.")
        notes_label.pack(pady=5)

    # ==== Functions ====
    def show_about(self):
        messagebox.showinfo("About", "Tkinter AI GUI Example\nAssignment 03")

    def load_model(self):
        self.output_display.insert(tk.END, "Model Loaded: {}\n".format(self.model_choice.get()))

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.input_text.delete(0, tk.END)
            self.input_text.insert(0, file_path)

    def run_model1(self):
        self.output_display.insert(tk.END, "Running Model 1...\n")

    def run_model2(self):
        self.output_display.insert(tk.END, "Running Model 2...\n")

    def clear_output(self):
        self.output_display.delete(1.0, tk.END)


if __name__ == "__main__":
    app = AIGUI()
    app.mainloop()
