import tkinter as tk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def GUI():

    def click_submit():
        english_sentence = text.get(1.0, tk.END).strip()
        # Get the input English sentence starting from the first character and remove any surrounding whitespace

        inputs = tokenizer(english_sentence, return_tensors='pt', max_length=128, padding=True, truncation=True)
        # Convert the input text into the token ID sequence corresponding to the model

        translated = model.generate(**inputs)
        # Pass the sequence to the model to generate the translation

        chinese_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        chinese_text = chinese_text.replace(' ', '')
        # Take the most likely result, and remove special characters and spaces

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, chinese_text)
        # Clear previous content and display the new translation result in the result text box

    model_path = "translation_dir/checkpoint-19000"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    # Load the model and the corresponding tokenizer

    root = tk.Tk()
    root.title("Medical Translation")
    root.geometry("600x400")
    # Create the main window, define the window title, and adjust the window size

    text_label = tk.Label(root, text="Enter Text")
    text_label.pack(pady=10)
    text = tk.Text(root, height=5, width=60)
    text.pack(pady=5)
    # Define the input text box and arrange it vertically

    submit_button = tk.Button(root, text="Submit", command=click_submit)
    submit_button.pack(pady=10)
    # Define the submit button and link it to the click_submit function to handle the input

    result_label = tk.Label(root, text="Translation Result")
    result_label.pack(pady=10)
    result_text = tk.Text(root, height=5, width=60)
    result_text.pack(pady=5)
    # Define the text box for displaying the translation result

    root.mainloop()
    # Start the main event loop

GUI()
