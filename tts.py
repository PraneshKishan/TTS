import tkinter as tk
from tkinter import ttk
from gtts import gTTS

class TextToAudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Audio Converter")

        self.input_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
        self.input_text.pack()

        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()

        self.output_filename_label = tk.Label(root, text="Output Filename:")
        self.output_filename_label.pack()

        self.output_filename = tk.StringVar()
        self.output_filename.set("output_audio.mp3")  # Default output filename

        self.output_filename_entry = ttk.Entry(root, textvariable=self.output_filename)
        self.output_filename_entry.pack()

        self.audio_button = ttk.Button(root, text="Generate Audio", command=self.generate_audio)
        self.audio_button.pack()

    def generate_audio(self):
        text = self.input_text.get("1.0", "end-1c")
        output_filename = self.output_filename.get()

        if not text.strip():
            self.show_output_message("Please enter some text.")
            return

        if not output_filename:
            self.show_output_message("Please enter an output filename.")
            return

        tts = gTTS(text=text, lang='en')
        tts.save(output_filename)
        self.show_output_message(f"Audio generated: {output_filename}")

    def show_output_message(self, message):
        self.output_label.config(text=message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToAudioApp(root)
    root.mainloop()
