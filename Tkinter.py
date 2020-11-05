from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time


def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self , master):
        self.master = master
        self.master.title("RESTAURANT LOGIN SYSTEM")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'PeachPuff3')
        self.frame = Frame(self.master, bg = 'PeachPuff3' )
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = "Restaurant Login System" ,font=('arial',50,'bold'), bg = 'PeachPuff4',fg='black')
        self.lblTitle.grid(row = 0, column = 0, columnspan = 2, pady = 40)
#===================================================================================================================================
        self.LoginFrame1= LabelFrame(self.frame , width=1350,height= 600,font=('arial',20,'bold'),relief='ridge',bg='PeachPuff4',bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame ,width =1000,height = 600,font=('arial',20,'bold'),relief='ridge',bg='PeachPuff3',bd=20)
        self.LoginFrame2.grid(row=2, column=0)

#=============================================labels and Entry========================================================================
        self.lblUsername = Label(self.LoginFrame1, text = 'Username' ,font=('arial',20,'bold'),bd=22,bg='PeachPuff4',fg='Cornsilk')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1,font=('arial',20,'bold'),textvariable= self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LoginFrame1, text = 'Password' ,font=('arial',20,'bold'),bd=22,bg='PeachPuff4',fg='Cornsilk')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1,font=('arial',20,'bold'),show = '*', textvariable = self.Password)
        self.txtPassword.grid(row=1, column=1)

#===================================================================================================================================

        self.btnLogin = Button(self.LoginFrame2 , text = 'Login', width = 17,font=('arial',20,'bold'),command =self.Login_System)
        self.btnLogin.grid(row=3,column =0,pady =20, padx=8)

        self.btnReset = Button(self.LoginFrame2, text = 'Reset' ,width = 17,font=('arial',20,'bold'), command=self.Rest)
        self.btnReset.grid(row=3,column =1,pady =20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit' ,width = 17,font=('arial',20,'bold'), command=self.iExit)
        self.btnExit.grid(row=3,column =2,pady =20, padx=8)

    def Login_System(self):
        u = (self.Username.get())
        p = (self.Password.get())
        if(u == str(12345) and p == str(54321)):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Login System", "invalid details")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
    def Rest(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
 def __init__(self , master):
        self.master = master
        self.master.title("RESTAURANT BILLING SYSTEM")
        self.master.geometry('1600x800+0+0')
        self.master.config(bg = 'PeachPuff4')
        self.frame = Frame(self.master, bg = 'PeachPuff3' )
        self.frame.pack()



       
        txt_Input=StringVar()
        operator=""

        Tops = Frame(self.master, width=1600, height=50 ,bg="PeachPuff3", relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self.master, width=800, height=700, relief=SUNKEN)
        f1.pack(side=LEFT)

        f2 = Frame(self.master, width=300, height=700 ,bg="PeachPuff3", relief=SUNKEN)
        f2.pack(side=RIGHT)






        #=========================================================================TIME=====================================================================================
        localtime=time.asctime(time.localtime(time.time()))
        #=========================================================================INFO=====================================================================================
        lblInfo = Label(Tops, font=('arial' ,50, 'bold'), text="Restaurant Billing System" ,fg="PeachPuff4" ,bd=10 ,anchor='w')
        lblInfo.grid(row=0, column=0)

        lblInfo = Label(Tops, font=('arial' ,20, 'bold'), text=localtime ,fg="PeachPuff4" ,bd=10 ,anchor='w')
        lblInfo.grid(row=1, column=0)

        #======================================================================calculator==================================================================================
        def btnClick(numbers):
            global operator
            operator= operator + str(numbers)
            txt_Input.set(operator)

        def btnClearDisplay():
            global operator
            operator=""
            txt_Input.set("")

        def btnEqualsInput():
            global operator
            sumup=str(eval(operator))
            txt_Input.set(sumup)
            operator=""

        def Ref():
            x=random.randint(10908,500876)
            randomRef=str(x)
            rand.set(randomRef)

            if (Fries.get()==""):
                CoFries=0
            else:
                CoFries=float(Fries.get())


            
            if (Noodles.get()==""):
                CoNoodles=0
            else:
                CoNoodles=float(Noodles.get())



            if (Soup.get()==""):
                CoSoup=0
            else:
                CoSoup=float(Soup.get())



            if (Burger.get()==""):
                CoBurger=0
            else:
                CoBurger=float(Burger.get())

                
            if (Sandwich.get()==""):
                CoSandwich=0
            else:
                CoSandwich=float(Sandwich.get())

             
            if (Drinks.get()==""):
                CoD=0
            else:
                CoD=float(Drinks.get())

                           
            CostofFries =CoFries * 140
            CostofDrinks=CoD * 65
            CostofNoodles = CoNoodles* 90
            CostofSoup = CoSoup * 140
            CostBurger = CoBurger* 260
            CostSandwich=CoSandwich * 300

            CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))

            PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich) * 0.2)

            TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)
         
            Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)/99)

            Service = "Rs", str ('%.2f' % Ser_Charge)

            OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

            PaidTax= "Rs", str ('%.2f' % PayTax)

            Service_Charge.set(Service)
            Cost.set(CostofMeal)
            Tax.set(PaidTax)
            SubTotal.set(CostofMeal)
            Total.set(OverAllCost)
            
        def qExit():
            self.master.destroy()



        def Reset():
            rand.set("") 
            Fries.set("")
            Noodles.set("")
            Soup.set("")
            SubTotal.set("")
            Total.set("")
            Service_Charge.set("")
            Drinks.set("")
            Tax.set("")
            Cost.set("")
            Burger.set("")
            Sandwich.set("")


         
        txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=txt_Input,bd=30, insertwidth=4,bg="PeachPuff3",justify='right')
        txtDisplay.grid(columnspan=4)

        btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="PeachPuff3",command=lambda:btnClick(7)).grid(row=2,column=0)
        btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="PeachPuff3",command=lambda:btnClick(8)).grid(row=2,column=1)
        btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="PeachPuff3",command=lambda:btnClick(9)).grid(row=2,column=2)
        Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="PeachPuff3",command=lambda:btnClick("+")).grid(row=2,column=3)
        #----------------------------------------------------------------------------------------------------------------------------------------------------------
        btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="PeachPuff3",command=lambda:btnClick(4)).grid(row=3,column=0)
        btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="PeachPuff3",command=lambda:btnClick(5)).grid(row=3,column=1)
        btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="PeachPuff3",command=lambda:btnClick(6)).grid(row=3,column=2)
        Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="PeachPuff3",command=lambda:btnClick("-")).grid(row=3,column=3)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="PeachPuff3",command=lambda:btnClick(1)).grid(row=4,column=0)
        btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="PeachPuff3",command=lambda:btnClick(2)).grid(row=4,column=1)
        btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="PeachPuff3",command=lambda:btnClick(3)).grid(row=4,column=2)
        Multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="PeachPuff3",command=lambda:btnClick("*")).grid(row=4,column=3)
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="PeachPuff3",command=lambda:btnClick(0)).grid(row=5,column=0)
        btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",bg="PeachPuff3",command=btnClearDisplay).grid(row=5,column=1)
        btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="PeachPuff3",command=btnEqualsInput).grid(row=5,column=2)
        Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="PeachPuff3",command=lambda:btnClick("/")).grid(row=5,column=3)

        #====================================================================RESTAURANT INFO 1=========================================================================
        rand = StringVar()
        Fries=StringVar()
        Noodles=StringVar()
        Soup=StringVar()
        SubTotal=StringVar()
        Total=StringVar()
        Service_Charge=StringVar()
        Drinks=StringVar()
        Tax=StringVar()
        Cost=StringVar()
        Burger=StringVar()
        Sandwich=StringVar()



        lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
        lblReference.grid(row=0, column=0)
        txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtReference.grid(row=0,column=1)

        lblFries= Label(f1, font=('arial', 16, 'bold'),text="Fries",bd=16,anchor="w")
        lblFries.grid(row=1, column=0)
        txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtFries.grid(row=1,column=1)


        lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
        lblNoodles.grid(row=2, column=0)
        txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtNoodles.grid(row=2,column=1)


        lblSoup= Label(f1, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
        lblSoup.grid(row=3, column=0)
        txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtSoup.grid(row=3,column=1)

        lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
        lblBurger.grid(row=4, column=0)
        txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtBurger.grid(row=4,column=1)

        lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="Sandwich",bd=16,anchor="w")
        lblSandwich.grid(row=5, column=0)
        txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtSandwich.grid(row=5,column=1)

        #============================================================================================================
        #                                RESTAURANT INFO 2
        #========================================================================================

        lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
        lblDrinks.grid(row=0, column=2)
        txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtDrinks.grid(row=0,column=3)

        lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
        lblCost.grid(row=1, column=2)
        txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtCost.grid(row=1,column=3)


        lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
        lblService.grid(row=2, column=2)
        txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtService.grid(row=2,column=3)


        lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
        lblStateTax.grid(row=3, column=2)
        txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtStateTax.grid(row=3,column=3)

        lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
        lblSubTotal.grid(row=4, column=2)
        txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtSubTotal.grid(row=4,column=3)

        lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
        lblTotalCost.grid(row=5, column=2)
        txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="PeachPuff3",justify='right')
        txtTotalCost.grid(row=5,column=3)

        #==========================================Buttons==========================================================================================
        btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="PeachPuff3",command=Ref).grid(row=7,column=1)

        btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="PeachPuff3",command=Reset).grid(row=7,column=2)

        btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="PeachPuff3",command=qExit).grid(row=7,column=3)
        self.master.mainloop()
main()


        #=============================================================================================================================













                





