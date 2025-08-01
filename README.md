# CodeClauseInternship_SentimentAnalysis

A simple sentiment analysis tool that determines whether a given text is **Positive**, **Negative**, or **Neutral** using the TextBlob library.

---

## 📌 Project Overview

This project is a basic **Sentiment Analysis Tool** built with Python. It allows users to input sentences or reviews and get an instant sentiment classification using TextBlob’s polarity score.

---

## 🚀 Features

- Analyze sentiment of user-provided text input.
- Classify text into **Positive**, **Negative**, or **Neutral**.
- Easy-to-use command-line interface.
- Uses pre-built NLP models from TextBlob.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **TextBlob** (for natural language processing)
- **NLTK** corpora (automatically downloaded via TextBlob)

---

## ⚙️ Installation Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/melek-jemili/CodeClauseInternship_SentimentAnalysis
cd CodeClauseInternship_SentimentAnalysis
Step 2: Create and activate a virtual environment (optional but recommended)
bash
Copier
Modifier
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
Step 3: Install dependencies
bash
Copier
Modifier
pip install textblob
Step 4: Download TextBlob corpora
bash
Copier
Modifier
python -m textblob.download_corpora
▶️ Usage
Run the script to start analyzing text:

bash
Copier
Modifier
python sentiment_analysis.py
You'll be prompted to enter a sentence or review. The tool will output the sentiment result.

Example:

mathematica
Copier
Modifier
Enter a sentence or review: I love this project!
Sentiment: Positive 😊
⚙️ How It Works
The tool uses TextBlob’s polarity score, which ranges from -1 to 1:

Polarity > 0 → Positive

Polarity < 0 → Negative

Polarity = 0 → Neutral

🌟 Future Improvements
Add GUI using Tkinter or Streamlit.

Support batch analysis from CSV or text files.

Integrate advanced models like BERT or VADER.

Display sentiment confidence scores.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.
