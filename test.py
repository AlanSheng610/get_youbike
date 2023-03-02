import tkinter as tk
import tkinter.ttk as ttk
import  json, ssl, urllib.request
from turtle import width
import time



def getbike() :
    url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    context = ssl._create_unverified_context()  
    _barrow = []
    _return = []

    with urllib.request.urlopen(url, context=context) as jsondata:
    #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
        data = json.loads(jsondata.read().decode('utf-8-sig')) 
    name = '臺大男'

    for i in data:
        if i['sna'].find(name)>=0:
            print(i['sna'],'\t',i['sbi'],'\t',i['bemp'])
            _barrow.append(i['sbi'])
            _return.append(i['bemp'])
    return _barrow , _return



 



window = tk.Tk()
window.title('YouBike')
window.geometry("1000x1000")
tree = ttk.Treeview(window,columns=("可借車輛","可還車輛"))
tree.heading("#0",text="位置" ) # 图标栏
tree.heading("#1",text="可借車輛")
tree.heading("#2",text="可還車輛")

tree.column("#0",anchor= tk.CENTER ,width=300)
tree.column("#1",anchor= tk.CENTER ,width=300)
tree.column("#2",anchor= tk.CENTER ,width=300)

tree.insert("",index=tk.END ,text="男一舍前",values=("-1","-1"))
tree.insert("",index=tk.END,text="男六舍前",values=("-1","-1"))
tree.insert("",index=tk.END,text="男八舍東側",values=("-1","-1"))
tree.insert("",index=tk.END,text="男七舍前",values=("-1","-1"))

style = ttk.Style()
style.configure("Treeview.Heading", font=('黑體', 40)) # 设置标题头的字体
style.configure("Treeview", font=(None, 40)) # 设置每一行的字体
style.configure('Treeview',rowheight=60)


b = []
c = []

while(True):
    seconds = time.time()
    result = time.localtime(seconds)
    if(result.tm_sec < 30 and result.tm_sec > 10):
        (b , c) = getbike()
        break
    else: 
        time.sleep(5)
# 標示文字
tree.item('I001',values=(str(b[1]) , str(c[1]) ))
tree.item('I002',values=(str(b[2]) , str(c[2]) ))
tree.item('I003',values=(str(b[3]) , str(c[3]) ))
tree.item('I004',values=(str(b[0]) , str(c[0]) ))


# t = '位置           可借        可還'
# t1 = '男一舍前：        ' + str(b[1]) +'      ' + str(c[1])
# t2 = '男六舍前：       ' + str(b[2]) +'      ' + str(c[2])
# t3 = '男八舍東側：         ' + str(b[3]) +'      ' + str(c[3])
# t4 = '男七舍前：           ' + str(b[0]) +'      ' + str(c[0])





# label = tk.Label(window , text = t)
# label1 = tk.Label(window,                 # 文字標示所在視窗
#                  text = t1)  # 顯示文字
# label2 = tk.Label(window,                 # 文字標示所在視窗
#                  text = t2)  # 顯示文字
# label3 = tk.Label(window,                 # 文字標示所在視窗
#                  text = t3)  # 顯示文字
# label4 = tk.Label(window,                 # 文字標示所在視窗
#                  text = t4)  # 顯示文字

# 以預設方式排版標示文字
# label.pack()
# label1.pack()
# label2.pack()
# label3.pack()
# label4.pack()
tree.pack()


def refreshText():
    _b = []
    _c = []
    
    while(True):
        seconds = time.time()
        result = time.localtime(seconds)
        if(result.tm_sec < 20 and result.tm_sec > 15):
            print(result.tm_sec)
            (_b, _c) = getbike()
            break
        else: 
            time.sleep(3)
    # upt1 = '男一舍前：        ' + str(_b[1]) +'      ' + str(_c[1])
    # upt2 = '男六舍前：       ' + str(_b[2]) +'      ' + str(_c[2])
    # upt3 = '男八舍東側：         ' + str(_b[3]) +'      ' + str(_c[3])
    # upt4 = '男七舍前：           ' + str(_b[0]) +'      ' + str(_c[0])
    # label1.configure(text=upt1)
    # label2.configure(text=upt2)
    # label3.configure(text=upt3)
    # label4.configure(text=upt4)
    tree.item('I001',values=(str(_b[1]) , str(_c[1]) ))
    tree.item('I002',values=(str(_b[2]) , str(_c[2]) ))
    tree.item('I003',values=(str(_b[3]) , str(_c[3]) ))
    tree.item('I004',values=(str(_b[0]) , str(_c[0]) ))
    # window.after(1000 , refreshText)






window.after(1000, refreshText)
window.mainloop()