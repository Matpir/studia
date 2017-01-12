from Tkinter import *


class LabelDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Przyklad")

        self.first_button = Button(self, text="PRINT RANDOM 1", command=self.commandPrintRandom2, width=16, height=1)
        self.second_button = Button(self, text="PRINT RANDOM 2", command=self.commandPrintRandom1, width=16,
                                    height=1)

        self.second_button.pack(side=BOTTOM)
        self.first_button.pack(side=BOTTOM)

    def commandPrintRandom1(self):
        print "1232193482423329482394823"

    def commandPrintRandom2(self):
        print "1232193482423329482394823"


def main():
    LabelDemo().mainloop()


if __name__ == "__main__":
    main()
