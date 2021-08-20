import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

#label

my_label = tkinter.Label(text="I'm am a label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

tim = turtle.Turtle()
tim.write()

window.mainloop()


