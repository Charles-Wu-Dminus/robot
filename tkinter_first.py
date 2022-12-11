import tkinter as tk
import jieba
from tkinter import filedialog

# 創建一個頂層窗口
root = tk.Tk()

# 設置窗口標題
root.title("Input Text")

# 新增輸出框架
output_frame = tk.Frame(root)
output_frame.pack()
output_text = tk.StringVar()
output_label = tk.Label(output_frame, textvariable=output_text)
output_label.pack()

# 創建一個提交按鈕
button = tk.Button(root, text="Submit")

# 定義按鈕的事件處理器
def submit(event):
    # 顯示文件選擇對話框
    filepath = filedialog.askopenfilename()
    print("選擇的文件為：" + filepath)

    # 讀取文件中的文本
    with open(filepath, "r") as f:
        text = f.read()
        print("文件中的文本為：" + text)

    # 將文本分詞
    words = list(jieba.cut(text))
    print("分詞後的結果為：", words)

     # 將輸出文字顯示在輸出框架中
    output_text.set("分詞後的結果為：" + " ".join(words))

# 為按鈕綁定事件處理器
button.bind("<Button-1>", submit)

# 將按鈕顯示在窗口中
button.pack()

# 顯示窗口
root.mainloop()
