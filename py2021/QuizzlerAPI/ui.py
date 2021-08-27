from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self):
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    
    self.score_label = Label(text="Score: 0", fg="white")
    self.score_label.grid(row=0, column=1)
    
    self.canvas = Canvas(width=300, heigh=250, bg="white")
    self.question_text = self.canvas.create_text(
      150,
      125,
      text="some q text",
      fill=THEME_COLOR,
      font=("ARIAL", 20, "italic"),
    )
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
    true_image = Photoimage(file="images\true.png")
    false_image = Photoimage(file="images\false.png", highlightthickness=0)
    self.true_button = Button(image=true_image, highlightthickness=0)
    self.true_button.grid(row=2, column=0)
    self.false_button = Button(image=false_image, highlightthickness=0)
    self.false_button.grid(row=2, column=0)
    
    self.window.mainloop()


