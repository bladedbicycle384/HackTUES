from tkinter import *


root = Tk()
root.title("Spaces Trading Calculator")
a = Label(root, text = "Please choose an option", width = 65, bd = 130)
a.pack()


class Application(Frame):
    root.configure(bg = "grey")
    def say_hi(self):
        w = Label(root, text="Hello")
        w.pack()
        



    def createWidgets(self):

        self.Rent = Button(self)

        self.Rent["text"] = "Rent"

        self.Rent["fg"] = "red"

        self.Rent["bg"] = "#332200"
        
        self.Rent["command"] =  self.Rent



        self.Rent.pack({"side": "right"})



        self.Sell = Button(self)

        self.Sell["text"] = "Sell",

        self.Sell["fg"] = "green"

        self.Sell["bg"] = "#332200"

        self.Sell["command"] = self.Sell



        self.Sell.pack({"side": "left"})



        self.Combined = Button(self)
        
        self.Combined["text"] = "Rent and Sell"
        
        self.Combined["fg"] = "purple"

        self.Combined["bg"] = "#332200"

        self.Combined["command"] = self.Combined
        
        
        self.Combined.pack({})
        
        
        self.Quit = Button(self)

        self.Quit["text"] = "Exit this application"
        
        
        
    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.pack()
   
        self.createWidgets()

        
        



app = Application(master=root)

app.mainloop()

root.destroy()

