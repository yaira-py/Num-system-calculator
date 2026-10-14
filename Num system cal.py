import tkinter as tk



class NumSysCalculator:
    def __init__(self,root):
        self.root=root
        self.root.title('Calculator')
        self.root.geometry('450x500')
        self.root.configure(bg="#658F56")

        self.title_lb=tk.Label(self.root,text='Number System Calculator',font=('Arial',15,'bold'),
                               bg='#658F56',fg="#FFFFFF")
        self.title_lb.pack(pady=10)

        self.options= ['Decimal','Binary','Octal','Hexadecimal']

        self.frame1= tk.Frame(self.root,bg='#658F56',bd=0,highlightthickness=0)
        self.frame1.pack(pady=20,padx=10)

        self.from_lb=tk.Label(self.frame1,text='Convert from:',font=('Arial',13),bg='#658F56',fg='white')
        self.from_lb.pack(side='left',padx=10)

        self.from_var= tk.StringVar(value='Decimal')
        self.from_menu = tk.OptionMenu(self.frame1,self.from_var,*self.options)
        self.from_menu.pack(side='right',padx=10)

        self.frame2= tk.Frame(self.root,bg='#658F56',bd=0,highlightthickness=0)
        self.frame2.pack(pady=20,padx=10)

        self.from_lb=tk.Label(self.frame2,text='Convert to:',font=('Arial',13),bg='#658F56',fg='white')
        self.from_lb.pack(side='left',padx=20)

        self.to_var= tk.StringVar(value='Decimal')
        self.from_menu2 = tk.OptionMenu(self.frame2,self.to_var,*self.options)
        self.from_menu2.pack(side='right',padx=20)

        self.frame3=tk.Frame(self.root,bd=0,relief='solid',bg='#658F56')
        self.frame3.pack(pady=30,padx=20,)

        self.lb1=tk.Label(self.frame3,text='decimal:',font=('Arial',13,'bold'),bg='#658F56',fg="#FFFBFB")
        self.lb1.pack(padx=15,side='left')

        self.from_entry=tk.Entry(self.frame3,width=13)
        self.from_entry.pack(padx=15,side='right',ipady=4)

        self.frame4=tk.Frame(self.root,bd=0,relief='solid',bg='#658F56')
        self.frame4.pack(pady=10,padx=20,)

        self.lb2=tk.Label(self.frame4,text='decimal:',font=('Arial',13,'bold'),bg='#658F56',fg="#FFFBFB")
        self.lb2.pack(padx=15,side='left')

        self.en2=tk.Entry(self.frame4,width=13)
        self.en2.pack(padx=15,side='right',ipady=4)


        self.gen_btn=tk.Button(self.root,text='Calculate',font=('Arial',13,'bold'),bg="#F5852A",fg="#FFFBFB",command=self.do_convert)
        self.gen_btn.pack(pady=50,side='bottom')

        self.from_var.trace_add('write',self.do_convert)
        self.to_var.trace_add('write',self.do_convert)




    def do_convert(self,*args):
        number=self.from_entry.get().strip()
        from_name=self.from_var.get()
        to_name=self.to_var.get()

        self.lb1.config(text=from_name+':')
        self.lb2.config(text=to_name+':')

        if from_name=='Decimal':
            decimal= int(number)

        
        if from_name=='Binary':
            decimal= int(number,2)

        
        if from_name=='Octal':
            decimal= int(number,8)

        
        if from_name=='Hexadecimal':
            decimal= int(number,16)

        if to_name=='Decimal':
            ans=str(decimal)

        if to_name=="Binary":
            ans=bin(decimal)[2:]

        if to_name=="Octal":
            ans=oct(decimal)[2:]

        if to_name=="Hexadecimal":
            ans=hex(decimal)[2:]


        self.en2.delete(0,'end')
        self.en2.insert(0,ans)








if __name__=='__main__':
    window=tk.Tk()
    app=NumSysCalculator(window)
    window.mainloop()
