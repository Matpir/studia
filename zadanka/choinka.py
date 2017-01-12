from Tkinter import *

from ttfquery.glyphquery import width

root = Tk()
root.title(u"Przyklad Canvas")

canvas = Canvas(root, width=500, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_line(250, 400, 250, 150, width=35, fill='brown')

galezi = 10
odleglosc = 10
i = 0

x1 = 100
y1 = 140
x2 = 400
y2 = 185

while i < galezi:
    canvas.create_line(x1, y1, x2, y2, width=6, fil='green')
    y1 += odleglosc
    y2 += odleglosc
    i += 1

i = 0
x1 = 85
y1 = 140
x2 = 400
y2 = 100
while i < galezi:
    canvas.create_line(x1, y1, x2, y2, width=6, fil='green')
    y1 += odleglosc
    y2 += odleglosc
    i += 1

root.mainloop()
