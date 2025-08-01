# CodeClauseInternship_SentimentAnalysis
A sentiment analysis tool that determines the sentiment (positive, negative, neutral) of a given text.


## Project Overview
This project is a simple **Sentiment Analysis Tool** that determines the sentiment of a given text as **Positive**, **Negative**, or **Neutral** using the Python library **TextBlob**.

The tool allows users to input sentences or reviews and get an immediate sentiment classification based on polarity analysis.

---

## Features
- Analyze sentiment of user-provided text input.
- Classify text into **Positive**, **Negative**, or **Neutral**.
- Easy-to-use command-line interface (or can be extended with GUI).
- Uses pre-built NLP models from TextBlob for quick sentiment detection.

---

## Technologies Used
- Python 3.x
- TextBlob (Python library for processing textual data)
- NLTK corpora (downloaded automatically by TextBlob)

---

## Installation Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/melek-jemili/CodeClauseInternship_SentimentAnalysis
cd CodeClauseInternship_SentimentAnalysis

2. **Create and activate a Python virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. **Install dependencies:

```bash
pip install -r requirements.txt

4. **Download TextBlob corpora:

```bash
python -m textblob.download_corpora

---
## Usage
  .Run the main script to analyze sentiment:

```bash
python sentiment_analysis.py
  .Enter any sentence or review when prompted, and the tool will output the sentiment classification.

---
## How It Works
.The tool uses TextBlob’s polarity score, which ranges from -1 (very negative) to 1 (very positive).
.Based on the polarity:
  Polarity > 0 → Positive sentiment
  
  Polarity < 0 → Negative sentiment
  
  Polarity = 0 → Neutral sentiment

---
## Future Improvements
    Add GUI with Tkinter or Streamlit.
    
    Support batch analysis of multiple sentences or files.
    
    Use more advanced models like BERT or VADER for better accuracy.
    
    Add sentiment score output and confidence levels.
---
**License**
This project is licensed under the MIT License. See the LICENSE file for details.
