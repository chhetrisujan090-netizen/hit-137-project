# base_model.py

import tkinter as tk


class BaseModel:
    """Simple base model class."""
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"BaseModel: {self.name}"




