
################################################################Muhammad Nabil#############################################
from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time;


class Customer:

    def __init__(self,roo):
        self.root = root
        self.root.title("Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

        ABC =Frame(self.root, bg="powder blue", bd=20, relief=RIDGE)
        ABC.grid()
        ABC1 =Frame(ABC, bd=14, width=1350, height=100, padx=10, bg="powder blue", relief=RIDGE)
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
        ABC2 =Frame(ABC, bd=14, width=450, height=488, padx=10, bg="cadet blue", relief=RIDGE)
        ABC2.grid(row=1, column=0, sticky=W)
        ABC3 =Frame(ABC, bd=14, width=430, height=488, padx=10, bg="powder blue", relief=RIDGE)
        ABC3.grid(row=1, column=1, sticky=W)
        ABC4 =Frame(ABC, bd=14, width=400, height=488, padx=10, bg="cadet blue", relief=RIDGE)
        ABC4.grid(row=1, column=2, sticky=W)
        ABC5 =Frame(ABC4, bd=14, width=320, height=340, padx=10, bg="cadet blue", relief=RIDGE)
        ABC5.grid(row=0, column=0, sticky=W)
        ABC6 =Frame(ABC4, bd=14, width=320, height=120, padx=10, bg="cadet blue", relief=RIDGE)
        ABC6.grid(row=1, column=0, columnspan=4, sticky=W)


        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle = Label(ABC1, textvariable=Date1, font =('arial',30,'bold'),pady=9,
                              bd=5, bg='cadet blue',fg="cornsilk").grid(row=0, column=0) 

        self.lblTitle = Label(ABC1, text="\tBilling System\t\t", font =('arial',30,'bold'),pady=9,
                              bd=5, bg='cadet blue',fg="cornsilk").grid(row=0, column=1)

        self.lblTitle = Label(ABC1, textvariable=Time1, font =('arial',30,'bold'),pady=9,
                              bd=5, bg='cadet blue',fg="cornsilk").grid(row=0, column=2)

        #########################################################Sarfraz Farooq##################################################

        CustomerRef =StringVar()
        AttendingStaff =StringVar()
        OrderDate =StringVar()
        Meal =StringVar()
        TableNumber =StringVar()
        TotalCost =StringVar()
        Subtotal =StringVar()
        PaidTax =StringVar()


        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()

        E_Fried_Chicken=StringVar()
        E_Fried_Rice=StringVar()
        E_Frenchfries=StringVar()
        E_Chicken_Curry=StringVar()
        E_Water=StringVar()
        E_Milo=StringVar()
        E_Pepsi=StringVar()
        E_Syrup=StringVar()

        E_Fried_Chicken.set=("0")
        E_Fried_Rice.set=("0")
        E_Frenchfries.set=("0")
        E_Chicken_Curry.set=("0")
        E_Water.set=("0")
        E_Milo.set=("0")
        E_Pepsi.set=("0")
        E_Syrup.set=("0")

        #================================================Initial Info=========================================================================
        self.lblCus_Ref=Label(ABC2, font=('arial',12,'bold'), text="Customer Ref:", padx=2, fg="Cornsilk", bg= "cadet blue")
        self.lblCus_Ref.grid(row=0, column=0, sticky=W)
        self.txtCus_Ref = Entry(ABC2, width=20, font =('arial',12,'bold'), textvariable= CustomerRef)
        self.txtCus_Ref.grid(row=0, column=1, pady=3, padx=20)

        self.lblAttendingStaff=Label(ABC2, font=('arial',12,'bold'), text="Attending Staff:", padx=2, pady=2, fg="Cornsilk", bg= "cadet blue")
        self.lblAttendingStaff.grid(row=1, column=0, sticky=W)
        self.cboAttendingStaff= ttk.Combobox(ABC2, textvariable= AttendingStaff, state='readonly', font=('arial',12,'bold'), width=18)

        self.cboAttendingStaff['value']=('','Sarfraz','Nabil')
        self.cboAttendingStaff.current(0)
        self.cboAttendingStaff.grid(row=1, column=1, pady=3, padx=20)

        self.lblOrderDate=Label(ABC2, font=('arial',12,'bold'), text="Order Date:", padx=2, fg="Cornsilk", bg= "cadet blue")
        self.lblOrderDate.grid(row=2, column=0, sticky=W)
        self.txtOrderDate = Entry(ABC2, width=20, font =('arial',12,'bold'), textvariable= OrderDate)
        self.txtOrderDate.grid(row=2, column=1, pady=3, padx=20)

        self.lblMeal=Label(ABC2, font=('arial',12,'bold'), text="Meal:", padx=2, pady=2, fg="Cornsilk", bg= "cadet blue")
        self.lblMeal.grid(row=3, column=0, sticky=W)
        self.cboMeal= ttk.Combobox(ABC2, textvariable= Meal, state='readonly', font=('arial',12,'bold'), width=18)

        self.cboMeal['value']=('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=3, column=1, pady=3, padx=20)
        

        self.lblTableNumber=Label(ABC2, font=('arial',12,'bold'), text="Table Number:", padx=2, fg="Cornsilk", bg= "cadet blue")
        self.lblTableNumber.grid(row=4, column=0, sticky=W)
        self.txtTableNumber = Entry(ABC2, width=20, font =('arial',12,'bold'), textvariable= TableNumber)
        self.txtTableNumber.grid(row=4, column=1, pady=3, padx=20)



        #===================================================Menu=================================================================

        self.Fried_Chicken = Checkbutton(ABC3, text="Fried Chicken ", variable=var1, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=0, sticky=W)
        self.txtFried_Chicken = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Fried_Chicken, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtFried_Chicken.grid(row=0, column=1)


        self.Fried_Rice = Checkbutton(ABC3, text="Fried Rice ", variable=var2, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=1, sticky=W)
        self.txtFried_Rice = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Fried_Rice, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtFried_Rice.grid(row=1, column=1)


        self.Frenchfries = Checkbutton(ABC3, text="Frenchfries ", variable=var3, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=2, sticky=W)
        self.txtFrenchfries = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Frenchfries, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtFrenchfries.grid(row=2, column=1)


        self.Chicken_Curry = Checkbutton(ABC3, text="Chicken Curry ", variable=var4, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=3, sticky=W)
        self.txtChicken_Curry = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Chicken_Curry, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtChicken_Curry.grid(row=3, column=1)


        self.Water = Checkbutton(ABC3, text="Water ", variable=var5, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=4, sticky=W)
        self.txtWater = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Water, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtWater.grid(row=4, column=1)


        self.Milo = Checkbutton(ABC3, text="Milo ", variable=var6, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=5, sticky=W)
        self.txtMilo = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Milo, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtMilo.grid(row=5, column=1)


        self.Pepsi = Checkbutton(ABC3, text="Pepsi ", variable=var7, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=6, sticky=W)
        self.txtPepsi = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Pepsi, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtPepsi.grid(row=6, column=1)


        self.Syrup = Checkbutton(ABC3, text="Syrup ", variable=var8, onvalue = 1, offvalue = 0,
                                         font=('arial',12,'bold'), bg="powder blue").grid(row=7, sticky=W)
        self.txtSyrup = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Syrup, bd=8,
                                      width=20, justify='left',state= DISABLED)
        self.txtSyrup.grid(row=7, column=1)
        







        #==========================================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Billing System", "Confirm if you want to Exit")
            if iExit > 0:
                root.destroy()
                return
        #==========================================================================================================
        def Reset():
            self.txtReceipt.delete("1.0",END)

            E_Fried_Chicken.set=("0")
            E_Fried_Rice.set=("0")
            E_Frenchfries.set=("0")
            E_Chicken_Curry.set=("0")
            E_Water.set=("0")
            E_Milo.set=("0")
            E_Pepsi.set=("0")
            E_Syrup.set=("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)

            CustomerRef.set("")
            AttendingStaff.set("")
            OrderDate.set("")
            Meal.set("")
            TableNumber.set("")
            TotalCost.set("")
            Subtotal.set("")
            PaidTax.set("")

        #==========================================================================================================
        
        self.txtReceipt = Text(ABC5, width=38, height=19,bd=10, font =('arial',9,'bold'))
        self.txtReceipt.grid(row=0, column=0)

        #=============================================Buttons======================================================


        self.btnTotal = Button(ABC6,padx=14, pady=7, bd=5,fg="Black", font =('arial',16,'bold'), width=4, height=1,
                               bg="powder blue", text="Total").grid(row=0, column=0)

        self.btnReset = Button(ABC6,padx=14, pady=7, bd=5,fg="Black", font =('arial',16,'bold'), width=4, height=1,
                               bg="powder blue", text="Reset", command=Reset).grid(row=0, column=1)

        self.btnExit = Button(ABC6,padx=14, pady=7, bd=5,fg="Black", font =('arial',16,'bold'), width=4, height=1,
                               bg="powder blue", text="Exit", command=iExit).grid(row=0, column=2)
        #==========================================================================================================
        
            

        
        
            
        #==========================================================================================================
        

if __name__=='__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()
    
