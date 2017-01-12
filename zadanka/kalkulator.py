from Tkinter import *


class LabelDemo(Frame):
    number1 = 0
    number2 = 0
    operation = ""

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Przyklad")

        self.editText = Entry()

        self.buttonClear = Button(self, text="C", command=self.clickedEqu, width=16, height=1)
        self.buttonEqu = Button(self, text="=", command=self.clickedEqu, width=16, height=1)
        self.buttonAdd = Button(self, text="+", command=self.clickedAdd, width=16, height=1)
        self.buttonSub = Button(self, text="-", command=self.clickedSub, width=16, height=1)
        self.buttonMul = Button(self, text="*", command=self.clickedMul, width=16, height=1)
        self.buttonDiv = Button(self, text="/", command=self.clickedDiv, width=16, height=1)

        self.button1 = Button(self, text="1", command=self.clicked1, width=16, height=1)
        self.button2 = Button(self, text="2", command=self.clicked2, width=16, height=1)
        self.button3 = Button(self, text="3", command=self.clicked3, width=16, height=1)

        self.button4 = Button(self, text="4", command=self.clicked4, width=16, height=1)
        self.button5 = Button(self, text="5", command=self.clicked5, width=16, height=1)
        self.button6 = Button(self, text="6", command=self.clicked6, width=16, height=1)

        self.button7 = Button(self, text="7", command=self.clicked7, width=16, height=1)
        self.button8 = Button(self, text="8", command=self.clicked8, width=16, height=1)
        self.button9 = Button(self, text="9", command=self.clicked9, width=16, height=1)

        self.button0 = Button(self, text="0", command=self.clicked0, width=16, height=1)

        self.buttonEqu.pack(side=TOP)
        self.buttonClear.pack(side=TOP)
        self.buttonAdd.pack(side=TOP)
        self.buttonSub.pack(side=TOP)
        self.buttonMul.pack(side=TOP)
        self.buttonDiv.pack(side=TOP)

        self.button1.pack(side=BOTTOM)
        self.button2.pack(side=BOTTOM)
        self.button3.pack(side=BOTTOM)

        self.button4.pack(side=BOTTOM)
        self.button5.pack(side=BOTTOM)
        self.button6.pack(side=BOTTOM)

        self.button7.pack(side=BOTTOM)
        self.button8.pack(side=BOTTOM)
        self.button9.pack(side=BOTTOM)

        self.button0.pack(side=BOTTOM)

        self.editText.pack(side=TOP)

    def clickedEqu(self):
        self.number2 = self.editText.get()
        self.editText.delete(0, END)
        if self.operation == "+":
            self.editText.insert(int(self.number1) + int(self.number2), int(self.number1) + int(self.number2))
        if self.operation == "-":
            self.editText.insert(int(self.number1) - int(self.number2), int(self.number1) - int(self.number2))
        if self.operation == "*":
            self.editText.insert(int(self.number1) * int(self.number2), int(self.number1) * int(self.number2))
        if self.operation == "/":
            self.editText.insert(int(self.number1) / int(self.number2), int(self.number1) / int(self.number2))

    def clickedClear(self):
        self.number1 = 0
        self.number2 = 0
        self.editText.delete(0, END)

    def clickedAdd(self):
        self.operation = "+"
        self.number1 = self.editText.get()
        self.editText.delete(0, END)

    def clickedSub(self):
        self.operation = "-"
        self.number1 = self.editText.get()
        self.editText.delete(0, END)

    def clickedMul(self):
        self.operation = "*"
        self.number1 = self.editText.get()
        self.editText.delete(0, END)

    def clickedDiv(self):
        self.operation = "/"
        self.number1 = self.editText.get()
        self.editText.delete(0, END)

    def clicked1(self):
        self.editText.insert("1", "1")

    def clicked2(self):
        self.editText.insert("2", "2")

    def clicked3(self):
        self.editText.insert("3", "3")

    def clicked4(self):
        self.editText.insert("4", "4")

    def clicked5(self):
        self.editText.insert("5", "5")

    def clicked6(self):
        self.editText.insert("6", "6")

    def clicked7(self):
        self.editText.insert("7", "7")

    def clicked8(self):
        self.editText.insert("8", "8")

    def clicked9(self):
        self.editText.insert("9", "9")

    def clicked0(self):
        self.editText.insert("0", "9")


def main():
    LabelDemo().mainloop()


if __name__ == "__main__":
    main()
