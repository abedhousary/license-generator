from tkinter import * 
import ttkbootstrap as bt
import string 
import random

class licensegenerator : 
    def __init__(self):
        self.generateUi() 
    def generateUi(self):
        root = Tk() 
        width = 400 
        height =100 
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw / 2) - (width / 2)
        y = (sh / 2) - (height / 2)
        root.geometry("%dx%d+%d+%d"%(width,height,x,y))
        root.title("License Generator")
        lbllicense = bt.Label(root,text = "License")
        self.entlicense = bt.Entry(root,width=40)
        btngenerate = bt.Button (root,text = "Generator",style="success",command=self.show_license,)
        lbllicense.grid(row=0,column=0,padx=20)
        self.entlicense.grid(row=0,column=1,padx=20)
        btngenerate.grid(row=1,column=1,padx=40,pady=20)
        root.mainloop()
    def generate_letters (self):
        self.licensedividor = []
        partholder = ""
        dictionary = str(string.ascii_letters) + str(string.digits)
        for x in range (30):
            if len(partholder) >= 5 :
                self.licensedividor.append(partholder)
                partholder = ""
            else:
                partholder += str(random.choice(dictionary)).upper()        
    def show_license(self):
        self.generate_letters()
        self.license = ""
        for license in str(self.licensedividor).replace(",","-").replace(" ","") :
            self.license += license
        self.last = self.license.replace("[","").replace("]","").replace("'","")
        self.entlicense.delete(0,END)
        self.entlicense.insert(0,self.last)
app = licensegenerator()