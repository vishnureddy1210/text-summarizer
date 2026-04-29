import gradio as gr
from transformers import BartForConditionalGeneration, BartTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize(text, max_len, min_len):
    if len(text.strip()) < 50:
        return "Please enter at least 50 characters."
    inputs = tokenizer(text, return_tensors="pt",
                       max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=int(max_len),
        min_length=int(min_len),
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

demo = gr.Interface(
    fn=summarize,
    inputs=[
        gr.Textbox(lines=10, label="Paste your text here",
            placeholder="Paste a news article, essay..."),
        gr.Slider(50, 300, value=130, step=10,
            label="Max summary length"),
        gr.Slider(20, 100, value=30, step=5,
            label="Min summary length"),
    ],
    outputs=gr.Textbox(label="Summary", lines=5),
    title="AI Text Summarizer",
    description="Powered by BART-large-CNN. Best quality summarization!"
)

demo.launch()