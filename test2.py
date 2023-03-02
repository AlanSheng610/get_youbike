from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("apidemos.com")

# 建立Treeview
tree = Treeview(root,columns="cities") # tree = Treeview(root,columns=("cities"))
# 建立栏标题
tree.heading("#0",text="State") # 图标栏
tree.heading("#1",text="City")
# 建立内容
tree.insert("",index=END,text="Eleanor",values="Chicago")
tree.insert("",index=END,text="California",values="Los Angeles")
tree.insert("",index=END,text="Tokyo",values="Houston")
tree.pack()

root.mainloop()