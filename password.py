import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# --- BRANDED THEME COLORS ---
CLR_BG = "#0f172a"  # Deep Navy
CLR_CARD = "#1e293b"  # Slate Blue
CLR_ACCENT = "#38bdf8"  # Bright Cyan
CLR_TEXT = "#f8fafc"  # Off-White
CLR_MUTED = "#94a3b8"  # Muted Grey
CLR_STRENGTH_LOW = "#ef4444"
CLR_STRENGTH_MED = "#f59e0b"
CLR_STRENGTH_HIGH = "#10b981"


class ProfessionalGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("SecurePass Pro")
        self.root.geometry("460x600")
        self.root.configure(bg=CLR_BG)

        # Variables
        self.length = tk.IntVar(value=14)
        self.upper = tk.BooleanVar(value=True)
        self.nums = tk.BooleanVar(value=True)
        self.syms = tk.BooleanVar(value=True)

        self._build_ui()

    def _build_ui(self):
        # 1. HEADER
        header = tk.Frame(self.root, bg=CLR_BG, pady=30)
        header.pack(fill="x")
        # Change this line:
        tk.Label(header, text="SECUREPASS PRO", font=("Inter", 18, "bold"),
                 bg=CLR_BG, fg=CLR_ACCENT).pack()  # Removed letterspace=2
        tk.Label(header, text="Military-grade encryption patterns",
                 font=("Inter", 9), bg=CLR_BG, fg=CLR_MUTED).pack()

        # 2. MAIN CARD
        card = tk.Frame(self.root, bg=CLR_CARD, padx=30, pady=30, highlightthickness=1, highlightbackground="#334155")
        card.pack(padx=25, fill="both", expand=True)

        # Password Output Box
        self.out_var = tk.StringVar(value="Click Generate")
        out_entry = tk.Entry(card, textvariable=self.out_var, font=("JetBrains Mono", 18),
                             bg="#0f172a", fg=CLR_TEXT, bd=0, justify="center", insertbackground="white")
        out_entry.pack(fill="x", pady=(0, 10), ipady=15)

        # Strength Meter Bar
        self.strength_bar = tk.Frame(card, height=4, bg="#334155")
        self.strength_bar.pack(fill="x", pady=(0, 20))

        # 3. CONTROLS
        # Length Slider
        tk.Label(card, text="PASSWORD LENGTH", font=("Inter", 9, "bold"), bg=CLR_CARD, fg=CLR_MUTED).pack(anchor="w")

        len_frame = tk.Frame(card, bg=CLR_CARD)
        len_frame.pack(fill="x", pady=(5, 20))

        tk.Scale(len_frame, from_=8, to=32, orient="horizontal", variable=self.length,
                 bg=CLR_CARD, fg=CLR_ACCENT, highlightthickness=0, troughcolor="#0f172a",
                 activebackground=CLR_ACCENT, showvalue=0, command=lambda x: self.update_strength()).pack(side="left",
                                                                                                          expand=True,
                                                                                                          fill="x")

        tk.Label(len_frame, textvariable=self.length, font=("Inter", 12, "bold"),
                 bg=CLR_CARD, fg=CLR_TEXT, width=3).pack(side="right")

        # Options
        tk.Label(card, text="SECURITY OPTIONS", font=("Inter", 9, "bold"), bg=CLR_CARD, fg=CLR_MUTED).pack(anchor="w")

        opts_frame = tk.Frame(card, bg=CLR_CARD, pady=10)
        opts_frame.pack(fill="x")

        self._create_check(opts_frame, "Uppercase Letters", self.upper)
        self._create_check(opts_frame, "Include Numbers", self.nums)
        self._create_check(opts_frame, "Special Characters", self.syms)

        # 4. ACTION BUTTONS
        gen_btn = tk.Button(self.root, text="GENERATE SECURE KEY", font=("Inter", 11, "bold"),
                            bg=CLR_ACCENT, fg=CLR_BG, activebackground="#7dd3fc",
                            relief="flat", pady=15, cursor="hand2", command=self.generate)
        gen_btn.pack(fill="x", padx=25, pady=(20, 10))

        copy_btn = tk.Button(self.root, text="COPY TO CLIPBOARD", font=("Inter", 9),
                             bg=CLR_BG, fg=CLR_MUTED, activebackground=CLR_BG,
                             activeforeground=CLR_TEXT, relief="flat", command=self.copy)
        copy_btn.pack()

    def _create_check(self, parent, text, var):
        cb = tk.Checkbutton(parent, text=text, variable=var, bg=CLR_CARD, fg=CLR_TEXT,
                            activebackground=CLR_CARD, activeforeground=CLR_ACCENT,
                            selectcolor=CLR_BG, font=("Inter", 10), pady=5, command=self.update_strength)
        cb.pack(anchor="w")

    def update_strength(self):
        # Calculate visual strength
        score = 0
        if self.length.get() > 12: score += 1
        if self.length.get() > 20: score += 1
        if self.upper.get(): score += 1
        if self.nums.get(): score += 1
        if self.syms.get(): score += 1

        colors = [CLR_STRENGTH_LOW, CLR_STRENGTH_MED, CLR_STRENGTH_HIGH]
        idx = 0 if score < 3 else (1 if score < 5 else 2)
        self.strength_bar.configure(bg=colors[idx])

    def generate(self):
        pool = string.ascii_lowercase
        if self.upper.get(): pool += string.ascii_uppercase
        if self.nums.get(): pool += string.digits
        if self.syms.get(): pool += string.punctuation

        pwd = "".join(random.choice(pool) for _ in range(self.length.get()))
        self.out_var.set(pwd)
        self.update_strength()

    def copy(self):
        pyperclip.copy(self.out_var.get())
        # Brief visual feedback on button could go here


if __name__ == "__main__":
    root = tk.Tk()
    app = ProfessionalGenerator(root)
    root.mainloop()