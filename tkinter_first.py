import tkinter as tk
import jieba

# 創建一個頂層窗口
root = tk.Tk()

# 設置窗口標題
root.title("Input Text")

# 創建一個提交按鈕
button = tk.Button(root, text="Submit")

# 創建一個文本框
textbox = tk.Entry(root)

# 定義按鈕的事件處理器
def submit(event):
    # 取得文本框中的文本
    text = textbox.get()
    print("輸入的文件為：" + text)

    # 將文件分詞
    words = list(jieba.cut(text))
    print("分詞後的結果為：", words)

# 為按鈕綁定事件處理器
button.bind("<Button-1>", submit)

# 將按鈕顯示在窗口中
button.pack()

# 將文本框顯示在窗口中
textbox.pack()

# 顯示窗口
root.mainloop()
