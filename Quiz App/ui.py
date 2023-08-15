from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizzler:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.user_answer = None
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=300, height=400, bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.score_text = Label(text=f"Score:0", bg=THEME_COLOR, font=("Arial", 12, "bold"),
                                fg="white")
        self.score_text.grid(row=0, column=1, pady=2)
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_btn = Button(image=self.true_img, command=self.true_press)
        self.true_btn.grid(row=2, column=1)
        self.false_btn = Button(image=self.false_img, command=self.false_press)
        self.false_btn.grid(row=2, column=0)
        self.question_text = self.canvas.create_text(150, 125, text="some question text.",
                                                     font=("Arial", 16, "normal"), width=270)
        self.get_nex_question()
        self.window.mainloop()

    def get_nex_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Ended!", font=("Arial", 36, "bold"))
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_press(self):
        self.feed_back(self.quiz.check_answer("True"))
        self.score_text.config(text=f"Score:{self.quiz.score}")

    def false_press(self):

        self.feed_back(self.quiz.check_answer("False"))
        self.score_text.config(text=f"Score:{self.quiz.score}")

    def feed_back(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nex_question)
