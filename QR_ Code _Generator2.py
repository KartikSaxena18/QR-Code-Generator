from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_generator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+330+125")
        self.root.title("QR-code Generator")
        self.root.resizable(False,False)

        title = Label(self.root, text="QR-code Generator",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)
        
        # ==============Detail window =====================

        #-----variables----
        self.var_name=StringVar()
        self.var_flat_no=StringVar()
        self.var_block=StringVar()
        self.var_vehicle_no=StringVar()
        self.var_vehicle_model=StringVar()

        emp_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title = Label(emp_Frame,text="Details",font=("times new roman",30),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        lbl_name = Label(emp_Frame,text="NAME",font=("Goudy",13,'bold'),bg='white').place(x=30,y=70)
        lbl_flat_no = Label(emp_Frame,text="FLAT NO.",font=("Goudy",13,'bold'),bg='white').place(x=30,y=120)
        lbl_block = Label(emp_Frame,text="BLOCK",font=("Goudy",13,'bold'),bg='white').place(x=30,y=170)
        lbl_vehicle_no = Label(emp_Frame,text="VEHICLE NO.",font=("Goudy",13,'bold'),bg='white').place(x=30,y=220)
        lbl_vehicle_model = Label(emp_Frame,text="VEHICLE MODEL",font=("Goudy",13,'bold'),bg='white').place(x=30,y=270)

        txt_name = Entry(emp_Frame,font=("Goudy",13),textvariable=self.var_name,bg='lightyellow').place(x=280,y=70)
        txt_flat_no = Entry(emp_Frame,font=("Goudy",13),textvariable=self.var_flat_no,bg='lightyellow').place(x=280,y=120)
        txt_block = Entry(emp_Frame,font=("Goudy",13),textvariable=self.var_block,bg='lightyellow').place(x=280,y=170)
        txt_vehicle_no = Entry(emp_Frame,font=("Goudy",13),textvariable=self.var_vehicle_no,bg='lightyellow').place(x=280,y=220)
        txt_vehicle_model = Entry(emp_Frame,font=("Goudy",13),textvariable=self.var_vehicle_model,bg='lightyellow').place(x=280,y=270)

        btn_generate=Button(emp_Frame, text="Generate QR",command=self.generate, font=("Goudy",18,'bold'),bg="#2196f3",fg="white").place(x=40,y=330,width=200,height=30)
        btn_clear=Button(emp_Frame, text="Clear",command=self.clear,font=("Goudy",18,'bold'),bg="#607d8b",fg="white").place(x=280,y=330,width=150,height=30)
        

         # ==============qr code window =====================
        qr_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)
        qr_title = Label(qr_Frame,text="QR Code",font=("times new roman",30),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        

        self.qr_code=Label(qr_Frame,text="QR code \nnot available",font=("Goudy",10),bg="#4682B4",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)


        self.msg = ""
        self.lbl_msg = Label(qr_Frame,text=self.msg,font=("Goudy",12),bg="white")
        self.lbl_msg.place(x=0,y=310,relwidth=1)

    def clear(self):
        self.var_name.set('')
        self.var_flat_no.set('')
        self.var_block.set('')
        self.var_vehicle_no.set('')
        self.var_vehicle_model.set('')

    def generate(self):
        if self.var_name.get()=='' or self.var_flat_no.get()=='' or self.var_block.get()=='' or self.var_vehicle_no.get()=='' or self.var_vehicle_model.get()=='':
            self.msg = "All Fields are required !!"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            
            qr_data=(f"Owner's Name: {self.var_name.get()}\nFlat no.: {self.var_flat_no.get()}\nBlock: {self.var_block.get()}\nVehicle no.: {self.var_vehicle_no.get()}\nVehicle Model: {self.var_vehicle_model.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            # ===============QR Code image update==============
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im) 
            # ============Updating Notification==========
            self.msg = "QR Generated successfully !!"
            self.lbl_msg.config(text=self.msg,fg="green")


root = Tk()
obj = Qr_generator(root)
root.mainloop()