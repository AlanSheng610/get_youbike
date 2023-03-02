from cProfile import label
import tkinter as tk
from youbike import getbike

global i
i = 0
def refreshText():
    global i
    i += 1
    text1.delete(0.0,tk.END)
    text1.insert(tk.INSERT,i)
    text1.update()
    windows.after(1000,refreshText)
 
windows = tk.Tk()
windows.geometry('1000x1000')  ## 规定窗口小500*500像素
text1 = tk.Text(windows,width=15,height=1)
text1.grid(row=0,column=1,padx=10,pady=10)
label = tk.Label(windows , text = "數量")
windows.after(1000,refreshText)
windows.mainloop()
