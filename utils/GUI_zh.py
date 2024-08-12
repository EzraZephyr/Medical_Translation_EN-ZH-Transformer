import tkinter as tk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def GUI():

    def click_submit():
        english_sentence = text.get(1.0, tk.END).strip()
        # 从第一个字符开始获取输入的英文句子并去掉空白字符

        inputs = tokenizer(english_sentence, return_tensors='pt', max_length=128, padding=True, truncation=True)
        # 转换成模型对应的token ID序列

        translated = model.generate(**inputs)
        # 将序列传入模型生成结果

        chinese_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        chinese_text = chinese_text.replace(' ','')
        # 取出可能性最大的结果并去除特殊字符和空格

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, chinese_text)
        # 清除之前的字符并将新的字符显示在翻译结果的文本框中

    model_path = "translation_dir/checkpoint-19000"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    # 加载模型和对应的分词器

    root = tk.Tk()
    root.title("医学翻译")
    root.geometry("600x400")
    # 创建主窗口 定义窗口名称并调整窗口大小

    text_label = tk.Label(root, text="输入文本")
    text_label.pack(pady=10)
    text = tk.Text(root, height=5, width=60)
    text.pack(pady=5)
    # 定义输入的文本框 并垂直排列

    submit_button = tk.Button(root, text="提交", command=click_submit)
    submit_button.pack(pady=10)
    # 定义提交的按钮并调用click_submit函数处理结果

    result_label = tk.Label(root, text="翻译结果")
    result_label.pack(pady=10)
    result_text = tk.Text(root, height=5, width=60)
    result_text.pack(pady=5)
    # 定义翻译结果的文本框

    root.mainloop()
    # 启动主事件循环

GUI()
