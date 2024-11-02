import tkinter as tk

from tkinter import filedialog
from utils import extract_text_from_webpage
from utils import recognize_speech
from utils import translate_text


class MyGUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Translation App")

        # Create menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # File menu
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)

        # Language menu
        language_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Language", menu=language_menu)
        self.language_var = tk.StringVar(self)
        self.language_var.set("English")  # Default language
        language_menu.add_radiobutton(
            label="English", variable=self.language_var, value="en")
        language_menu.add_radiobutton(
            label="Afrikaans", variable=self.language_var, value="af`")
        language_menu.add_radiobutton(
            label="English", variable=self.language_var, value="en")
        language_menu.add_radiobutton(
            label="French", variable=self.language_var, value="fr")
        language_menu.add_radiobutton(
            label="English", variable=self.language_var, value="en")
        language_menu.add_radiobutton(
            label="French", variable=self.language_var, value="fr")
        # Add more languages as needed

        # Create widgets
        self.input_label = tk.Label(self, text="Enter text:")
        self.input_text = tk.Entry(self)
        self.translate_button = tk.Button(self, text="Translate")
        self.output_label = tk.Label(self, text="Translated text:")
        self.voice_input_button = tk.Button(self, text="Voice Input")
        self.toggle_translate_button = tk.Button(
            self, text="Toggle Translation")

        # Grid layout
        self.input_label.grid(row=0, column=0, sticky="w")
        self.input_text.grid(row=0, column=1)
        self.translate_button.grid(row=1, column=0, columnspan=2)
        self.output_label.grid(row=2, column=0, columnspan=2)
        self.voice_input_button.grid(row=0, column=2)
        self.toggle_translate_button.grid(row=1, column=2)

        # Bind events
        self.input_text.bind("<Return>", self.translate)
        self.translate_button.bind("<Button-1>", self.translate)
        self.voice_input_button.bind("<Button-1>", self.voice_input)
        self.toggle_translate_button.bind("<Button-1>", self.toggle_translate)

        # Start the main loop
        self.mainloop()

    def translate(self, event=None):
        if self.translate_button['state'] == tk.NORMAL:
            user_input = self.input_text.get()
            if user_input == 'quit' or user_input == 'exit':
                self.quit()
            if user_input:
                target_language = self.language_var.get()
                translated_text = translate_text(
                    user_input, target_language=target_language)
                self.output_label.config(
                    text=f"Translated text: {translated_text}")
                read_text_aloud(translated_text)

    def voice_input(self, event=None):
        if self.translate_button['state'] == tk.NORMAL:
            user_input = recognize_speech()
            if user_input:
                translated_text = translate_text(
                    user_input, target_language=self.language_var.get())
                self.input_text.insert(tk.END, translated_text)
                self.output_label.config(
                    text=f"Translated text: {translated_text}")
                read_text_aloud(translated_text)

    def toggle_translate(self, event=None):
        if self.translate_button['state'] == tk.NORMAL:
            self.translate_button['state'] = tk.DISABLED
        else:
            self.translate_button['state'] = tk.NORMAL


if __name__ == "__main__":
    app = MyGUIApp()
    app.mainloop()
