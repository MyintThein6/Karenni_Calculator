import tkinter as tk
from tkinter import messagebox

# Mapping dictionary for English to Kayah Li
KARENNI_NUMS = {
    '0': '꤀', '1': '꤁', '2': '꤂', '3': '꤃', '4': '꤄',
    '5': '꤅', '6': '꤆', '7': '꤇', '8': '꤈', '9': '꤉'
}

# Reverse mapping for calculation
ENGLISH_NUMS = {v: k for k, v in KARENNI_NUMS.items()}


class KarenniCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("ꤊꤢꤛꤢ꤭ ꤜꤟꤤ꤬ Calculator")
        self.root.geometry("550x800")

        # Set Background Image (Ensure you have a 'flag.png' in the directory)
        try:
            self.bg_image = tk.PhotoImage(file="flag.png")
            self.bg_label = tk.Label(root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)
        except:
            # Fallback to Flag Colors if image is missing
            self.root.configure(bg='skyblue')  # Karenni Red

        self.expression = ""

        # Display Screen
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        # Button Labels (using Karenni numbers)
        buttons = [
            '꤇', '꤈', '꤉', '/',
            '꤄', '꤅', '꤆', '*',
            '꤁', '꤂', '꤃', '-',
            'Clear', '꤀', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_click(x)
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 14, "bold"),
                      command=action, bg="#FFFFFF", fg="#000000").grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def convert_to_english(self, kn_str):
        for kn, en in ENGLISH_NUMS.items():
            kn_str = kn_str.replace(kn, en)
        return kn_str

    def convert_to_karenni(self, en_str):
        for en, kn in KARENNI_NUMS.items():
            en_str = en_str.replace(en, kn)
        return en_str

    def on_click(self, char):
        if char == '=':
            try:
                # Convert Karenni input to English for Python's eval()
                english_expr = self.convert_to_english(self.expression)
                result = str(eval(english_expr))
                # Convert result back to Karenni
                self.expression = self.convert_to_karenni(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        elif char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    obj = KarenniCalculator(root)
    root.mainloop()