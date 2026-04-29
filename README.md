# AI Text Summarizer

A web app that summarizes long text using Facebook's BART-large-CNN model.
Built with Gradio and HuggingFace Transformers.

## Demo
Live demo: [Click here](https://vishnuvardhanreddy12-text-summarizer.hf.space)

## Features
- Paste any long text — news, articles, essays
- Adjust summary length using sliders
- Powered by BART-large-CNN (state of the art summarization)

## Tech Stack
- Python
- Gradio
- HuggingFace Transformers
- Facebook BART-large-CNN model

## Installation

1. Clone the repo
   git clone https://github.com/vishnureddy1210/text-summarizer.git
   cd text-summarizer

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the app
   python app.py

5. Open browser at http://127.0.0.1:7860

## Project Structure
text-summarizer/
├── app.py
├── requirements.txt
└── README.md

## Author
Your Name — github.com/vishnureddy1210