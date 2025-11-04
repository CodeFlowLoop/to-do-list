import tkinter as tk
from tkinter import messagebox,simpledialog

class Bank_App:
    def __init__(self,window):
        self.balance=0.0
        self.history=[]
        self.window=window
        window.title("BANK APPLICTION ")
        window.geometry("800x400")

        tk.Label(text="WECLCOME TO BANK ",font=('Arial', 15, 'bold')).pack(pady=10)
        tk.Button(text="DEPOSITE", width=30,command=self.deposite,font=('monaco',13,'bold')).pack(pady=10)
        tk.Button(text="BALANCE", width=30,command=self.show_balance,font=('monaco',13,'bold')).pack(pady=10)
        tk.Button(text="WITHDRAW", width=30,command=self.withdraw,font=('monaco',13,'bold')).pack(pady=10)
        tk.Button(text="HISTORY", width=30,command=self.statement,font=('monaco',13,'bold')).pack(pady=10)
        tk.Button(text="EXIT", width=30,command=window.quit,font=('monaco',13,'bold')).pack(pady=10)
    def show_balance(self):
        messagebox.showinfo("BALANCE",f"YOUR CURRENT ACCOUNT BALANCE\nRS {self.balance:.3f}")
    def deposite(self):
        amount=simpledialog.askfloat('DEPOSITE','ENTER THE DEPOSITE ANOUMT:\n ')
        if amount is not None:
            if amount>0:
                self.balance+=amount
                self.history.append(f"DEPOSITE:{amount:.3f}   |      BALANCE:{self.balance}")
                messagebox.showinfo('DEPOSITE',f'SUCCESSFUL DESPOSITE TO YOUR ACCOUNT\nRs={amount:.3F}')
            else:
                messagebox.showerror('DEPOSITE','PLEASE ENTER VALID AMOUNT')

    def withdraw(self):
        amount=simpledialog.askfloat('WITHDRAW','ENTER AN AMOUNT TO WITHDRAW:\n ')
        if amount is not None:
            if amount>self.balance:
                messagebox.showwarning("WITHDRAW",'INSUFFICIENT BALANCE.')
            elif amount<=0:
                messagebox.showerror('WITHDRAW','PLEASE ENTER VALID AMOUNT')
            else:
                self.balance-=amount
                self.history.append(f"WITHDRAW:{amount:.3f}     |      BALANCE:{self.balance}")
                messagebox.showinfo('WITHDRAW',f'WITHDRAW RS={amount:.3F}\n THE BANK BALANCE RS={self.balance:.3f}')  
    def statement(self):
        if self.history:
            history_text="\n".join(self.history)
        else:
            history_text="No Transaction yet."  
        messagebox.showinfo("TRANSACTION STATEMNET",history_text)  
                
if __name__=="__main__":  
    window=tk.Tk()
    app=Bank_App(window)
    window.mainloop()
    