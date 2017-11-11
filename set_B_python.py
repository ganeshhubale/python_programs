
import tkinter as tk
def click(key):
    global memory
    if key == '=':
        # avoid division by integer
        if '/' in entry.get() and '.' not in entry.get():
            entry.insert(tk.END, ".0")
        # guard against the bad guys abusing eval()
        str1 = "-+0123456789."
        if entry.get()[0] not in str1:
            entry.insert(tk.END, "first char not in " + str1)
        # here comes the calculation part
        try:
            result = eval(entry.get())
            entry.insert(tk.END, " = " + str(result))
        except:
            entry.insert(tk.END, "--> Error!")
    elif key == 'C':
        entry.delete(0, tk.END)  # clear entry
    else:
        # previous calculation has been done, clear entry
        if '=' in entry.get():
            entry.delete(0, tk.END)
        entry.insert(tk.END, key)
root = tk.Tk()
root.geometry("600x350")
root.title("Simple Calculator")
btn_list = [
'C',
'7',  '8',  '9',  '/',  
'4',  '5',  '6',  '*', 
'1',  '2',  '3',  '-',  
'0',  '.',  '+',  
'=' ]
# create all buttons with a loop
r = 1
c = 0
for b in btn_list:
    rel = 'ridge'
    cmd = lambda x=b: click(x)
    
    tk.Button(root,text=b,width=4,relief=rel,command=cmd).grid(row=r,column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1
# use Entry widget for an editable display
entry = tk.Entry(root, width=33, bg="yellow")
entry.grid(row=0, column=0, columnspan=5)
root.mainloop()

