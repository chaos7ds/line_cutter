# import
import tkinter as tk
import tkinter.font
from win32api import GetSystemMetrics

# 인터페이스 기본
root = tk.Tk()
sw, sh = GetSystemMetrics(0), GetSystemMetrics(1)
root.geometry(f"{int(sw / 2)}x{int(sh / 2)}+0+0")
root.title('line cutter')
root.update()
rsize = root.winfo_geometry()
rw = int(rsize[:rsize.find('x')])
rh = int(rsize[rsize.find('x') + 1:rsize.find('+')])


# 수행
def skiper(ip, op, i, n):
    op += ip[i:i + n]
    i += (n - 1)
    return op, i


def cutter():
    a = original.get(1.0, tk.END)
    b = ""
    i = 0
    while i < len(a):
        if a[i] in ".?!":
            b += a[i]
            if i + 1 < len(a):
                if a[i + 1] in ['"', "'"]:
                    i += 1
                    b += a[i]
            b += "\n"
        elif a[i] == "[":
            if len(b) != 0:
                if b[len(b) - 1] == " ":
                    b = b[0:len(b) - 1]
            while a[i] != "]":
                i += 1
        elif a[i] == '\n':
            b += ' '
        elif (i + 2 < len(a)) and (a[i] in "0123456789") and (a[i + 1] == ".") and (a[i + 2] in "0123456789"):
            (b, i) = skiper(a, b, i, 3)
        elif a[i:i + 2].lower() in ["=.", ">.", "<.", "-."]:
            (b, i) = skiper(a, b, i, 2)
        elif a[i:i + 3].lower() in ["= .", "> .", "< .", "- .", "pp.", "vs.", "eq.", "st.", "i.e"]:
            (b, i) = skiper(a, b, i, 3)
        elif a[i:i + 4].lower() in ["e.g.", "inc.", "n.s.", "fig.", "etc.", "i.e.", "s.d.", "u.s."]:
            (b, i) = skiper(a, b, i, 4)
        elif a[i:i + 6].lower() in ["et al.", " etal.", "u.s.a."]:
            (b, i) = skiper(a, b, i, 6)
        else:
            b += a[i]
        i += 1
    # b=b+'\n\n'
    return a, b


# 인터페이스 커스텀
font_MS = tkinter.font.Font(family='Times New Roman', size=18)

fr00 = tk.Frame(root, width=rw / 2 - 40, height=rh)
fr00.grid_propagate(False)
fr00.grid(row=0, column=0, rowspan=2)
original = tk.Text(fr00, wrap='word', spacing2=2, spacing3=15, padx=5, pady=5, undo=True, font=font_MS)
original.pack(fill='both')

fr02 = tk.Frame(root, width=rw / 2 - 40, height=rh)
fr02.grid_propagate(False)
fr02.grid(row=0, column=2, rowspan=2)
trans = tk.Text(fr02, wrap='word', spacing2=2, spacing3=15, padx=5, pady=5, undo=True, font=font_MS)
trans.pack(fill='both')

fr01 = tk.Frame(root, width=80, height=rh / 2)
fr01.grid_propagate(False)
fr01.grid(row=0, column=1, sticky='news')
btn1 = tk.Button(fr01, text='Reset', font=font_MS)
btn1.pack(fill='both', expand=True)

fr11 = tk.Frame(root, width=80, height=rh / 2)
fr11.grid_propagate(False)
fr11.grid(row=1, column=1, sticky='news')
btn2 = tk.Button(fr11, text='Cut', font=font_MS)
btn2.pack(fill='both', expand=True)

root.update()
fr00.config(width=rw / 2 - 40, height=rh)
fr02.config(width=rw / 2 - 40, height=rh)


def resize(event):
    root.update()
    rsize = root.winfo_geometry()
    rw = int(rsize[:rsize.find('x')])
    rh = int(rsize[rsize.find('x') + 1:rsize.find('+')])

    fr00.config(width=rw / 2 - 40, height=rh)
    fr02.config(width=rw / 2 - 40, height=rh)


root.bind("<Configure>", resize)


# 인터페이스 기능
def btn1cl():
    original.delete(1.0, tk.END)
    trans.delete(1.0, tk.END)


btn1.config(command=btn1cl)


def btn2cl():
    it, ot = cutter()
    btn1cl()
    original.insert(1.0, it)
    trans.insert(1.0, ot)


btn2.config(command=btn2cl)

# 인터페이스 기본
root.mainloop()
