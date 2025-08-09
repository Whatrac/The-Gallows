import tkinter as tk
from tkinter import messagebox

class Gameplay:
    def __init__(self):
        self.inital_word = None
        self.right_user_letter = set()
        self.wrong_user_letter = 0
        self.display_word = []

        
        self.root = tk.Tk()
        self.root.title("Игра Виселица")

        
        self.word_label = tk.Label(self.root, text="Введите слово:", font=("Arial", 14))
        self.word_label.pack()
        self.word_entry = tk.Entry(self.root, font=("Arial", 14))
        self.word_entry.pack()
        self.start_button = tk.Button(self.root, text="Начать игру", command=self.start_game, font=("Arial", 14))
        self.start_button.pack()

        
        self.letter_label = tk.Label(self.root, text="Введите букву:", font=("Arial", 14))
        self.letter_entry = tk.Entry(self.root, font=("Arial", 14))
        self.letter_button = tk.Button(self.root, text="Проверить букву", command=self.check_letter, font=("Arial", 14))

        
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack()

        
        self.word_display = tk.Label(self.root, text="", font=("Arial", 14))
        self.word_display.pack()

        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack()

        
        self.draw_gallows()

    def draw_gallows(self):
        
        self.canvas.create_line(50, 180, 150, 180)
        self.canvas.create_line(100, 180, 100, 50) 
        self.canvas.create_line(100, 50, 150, 50)  
        self.canvas.create_line(150, 50, 150, 70)  

    def draw_hangman(self, step):
        
        if step >= 1:
            self.canvas.create_oval(140, 70, 160, 90) 
        if step >= 2:
            self.canvas.create_line(150, 90, 150, 130)  
        if step >= 3:
            self.canvas.create_line(150, 100, 130, 120) 
        if step >= 4:
            self.canvas.create_line(150, 100, 170, 120)  
        if step >= 5:
            self.canvas.create_line(150, 130, 130, 160)  
        if step >= 6:
            self.canvas.create_line(150, 130, 170, 160)  

    def start_game(self):
        
        self.inital_word = self.word_entry.get().lower().strip()
        if self.inital_word.isalpha():
            self.word_label.config(text="Слово принято")
            self.word_entry.pack_forget()
            self.start_button.pack_forget()
            self.letter_label.pack()
            self.letter_entry.pack()
            self.letter_button.pack()
            self.display_word = ['_' for _ in self.inital_word]
            self.word_display.config(text=' '.join(self.display_word))
        else:
            messagebox.showerror("Ошибка", "Слово содержит недопустимые символы. Повторите попытку.")

    def check_letter(self):
        
        letter = self.letter_entry.get().lower().strip()
        self.letter_entry.delete(0, tk.END)  

        if len(letter) != 1:
            messagebox.showerror("Ошибка", "Недопустимая длина буквы. Введите одну букву.")
        else:
            if letter in self.inital_word:
                self.right_user_letter.add(letter)
                self.update_display_word()
                if '_' not in self.display_word:
                    messagebox.showinfo("Победа", "Вы угадали слово!")
                    self.root.quit()
            else:
                self.wrong_user_letter += 1
                self.draw_hangman(self.wrong_user_letter)
                if self.wrong_user_letter == 6:
                    messagebox.showinfo("Поражение", "Игра окончена. Вы проиграли!")
                    self.root.quit()

    def update_display_word(self):
        
        self.display_word = [letter if letter in self.right_user_letter else '_' for letter in self.inital_word]
        self.word_display.config(text=' '.join(self.display_word))

    def run(self):
        
        self.root.mainloop()

# Запуск игры
game = Gameplay()
game.run()
