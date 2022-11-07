THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class UserInterface():

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340, height=550)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="score ", font=("Arial", 10), fg="white", bg=THEME_COLOR)
        self.score_lable.grid(row=0, column=1)

        self.canavas = Canvas(width=300, height=250, bg="white")
        self.qustion_text = self.canavas.create_text(
            150,
            125,
            width=260,
            text="some textsdfsdfds",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")

        )
        self.canavas.grid(row=1, column=0, columnspan=2, pady=50)
        self.get_nex_question()
        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_answer)
        self.right_button.grid(row=2, column=0, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, bg=THEME_COLOR, highlightthickness=0,
                                   command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_nex_question(self):
        self.score_lable.config(text=f"Score :{self.quiz.score}")
        if self.quiz.question_number == 50:
            self.canavas.config(bg="white")
            self.canavas.itemconfig(
                self.qustion_text,
                text=f"Your final score is :{self.quiz.score}/50",
                font=("Arial", 25, "italic")
            )
            self.right_button.config(state="disable")
            self.false_button.config(state="disable")
            return

        self.canavas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canavas.itemconfig(self.qustion_text, text=q_text)

    def false_answer(self):
        answer = self.quiz.check_answer("False")
        self.check_the_answer(answer)

    def true_answer(self):
        answer = self.quiz.check_answer("True")
        self.check_the_answer(answer)

    def check_the_answer(self, answer):
        if answer:
            self.canavas.config(bg="green")
        else:
            self.canavas.config(bg="red")
        self.window.after(1000, self.get_nex_question)
