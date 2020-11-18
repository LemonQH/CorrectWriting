import tkinter as tk
from tkinter import filedialog,messagebox,ttk
from correctclass import Correct
import os

correct=Correct([],"","")
select_type_dict=["默认","小学","初中","高中","四级","六级	","考研","托福","GRE","雅思"]
grade_type_dict=['default','elementary','junior','high','cet4','cet6','graduate','toefl','gre','ielts']

def get_files():
    files = filedialog.askopenfilenames(filetypes=[('text files', '*')])
    correct.file_paths=files
    if files:
        for file in files:
            text1.insert(tk.END, file + '\n')
            text1.update()
    else:
        print('')
def set_result_path():
    result_path=filedialog.askdirectory()
    correct.result_path=result_path
    text2.insert(tk.END,result_path)

def correct_files():
    correct.start_correct()
    os.system('start '+correct.result_path)

def get_grade_type(*args):
    select = combox.get()
    correct.grade = grade_type_dict[select_type_dict.index(select)]


root=tk.Tk()
root.title(" youdao correct writing test")
frm = tk.Frame(root)
frm.grid(padx='50', pady='50')

btn_get_file = tk.Button(frm, text='选择待批改的作业（图片或文本）', command=get_files)
btn_get_file.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
text1 = tk.Text(frm, width='40', height='10')
text1.grid(row=0, column=1)
btn_get_result_path=tk.Button(frm,text='选择批改结果存放路径',command=set_result_path)
btn_get_result_path.grid(row=1,column=0)
text2=tk.Text(frm,width='40', height='2')
text2.grid(row=1,column=1)

label=tk.Label(frm,text='选择年级：')
label.grid(row=3,column=0)
combox=ttk.Combobox(frm,textvariable=tk.StringVar(),width=38)
combox["value"]=select_type_dict
combox.current(0)
combox.bind("<<ComboboxSelected>>",get_grade_type)
combox.grid(row=3,column=1)

btn_sure=tk.Button(frm,text="批改",command=correct_files)
btn_sure.grid(row=4,column=1)

root.mainloop()