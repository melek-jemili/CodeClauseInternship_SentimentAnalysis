import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter your text.")
        return

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    result_label.config(text=f"Sentiment: {sentiment}")


window = tk.Tk()
window.title("Sentiment Analyzer")
window.geometry("400x300")


instruction = tk.Label(window, text="Enter text to analyze sentiment:", font=("Arial", 12))
instruction.pack(pady=10)


text_entry = tk.Text(window, height=5, width=40, font=("Arial", 10))
text_entry.pack(pady=5)


analyze_button = tk.Button(window, text="Analyze", command=analyze_sentiment, font=("Arial", 11), bg="lightblue")
analyze_button.pack(pady=10)


result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)


window.mainloop()
