import os
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import extract_msg

def main():
  tkinter.messagebox.showinfo(title="Say", message="Hello World")

def selectFile():
  typ = [("メールテンプレート", "*.oft"), ("メッセージファイル", "*.msg")]
  dir = "~/Desktop"
  fp = tkinter.filedialog.askopenfilename(filetypes = typ, initialdir = dir)
  if fp:
    selected_file.set(fp)

def convertMsg():
  fp = selected_file.get()
  if not fp:
    tkinter.messagebox.showerror("エラー", "ファイルを選択してください")
    return

  custom_path, _ext = os.path.splitext(fp)

  kwds = {
    'customPath': custom_path,
    'html': is_html.get(),
    'overwriteExisting': True,
  }

  with extract_msg.openMsg(fp) as msg:
    msg.save(**kwds)

# ウィンドウの基本設定
app = tkinter.Tk()
app.title("oft converter")
app.geometry("300x200")

# 変数管理
selected_file = tkinter.StringVar(app)
is_html = tkinter.BooleanVar(app, True)

# ボタン
button = tkinter.Button(app, text="ファイルを選択", command=selectFile)

# 選択したファイルパス
selected_file_label = tkinter.Label(app, textvariable=selected_file, text="ファイルが選択されていません")

# 変換ボタン
confirm = tkinter.Button(app, text="変換する", command=convertMsg)

# チェックボックス
checkbox = tkinter.Checkbutton(text="HTMLメールとして変換", variable=is_html)

button.pack()
selected_file_label.pack()
confirm.pack()
checkbox.pack()

app.mainloop()
