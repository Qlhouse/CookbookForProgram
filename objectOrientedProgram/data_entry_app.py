from datetime import datetime
from pathlib import Path
import csv
import tkinter as tk
from tkinter import ttk

class BoundText(tk.Text):
    """A Text widget with a bound variable"""
    def __init__(self, *args, textvariable=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._variable = textvariable
