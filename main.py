import tkinter as tk
import random

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.current_level = 1 #Set this number to the starting number of the program
        self.max_level = 11 #Set this number to whatever you want the maximum level the user can reach is
        self.target_key = None
        self.score = 0
        self.label_text = tk.StringVar()
        self.label_text.set("Type the displayed key to advance to the next level")
        self.label = tk.Label(self.root, textvariable=self.label_text)
        self.label.pack()
        self.display_target_key()

    def display_target_key(self):
        if self.current_level > self.max_level:
            self.label_text.set("Game Over! Your score is {}".format(self.score))
            self.label.pack()
            return
        self.target_key = chr(random.randint(ord('a'), ord('z')))
        self.label_text.set("Level {}: Type the key '{}'".format(self.current_level, self.target_key))
        self.label.pack()

    def key_press(self, event):
        if event.char == self.target_key:
            self.score += 1
            self.current_level += 1
            self.display_target_key()
        else:
            self.label_text.set("Incorrect key! Your score is {}".format(self.score))
            self.label.pack()

root = tk.Tk()
game = TypingGame(root)
root.bind('<Key>', game.key_press)
root.mainloop()
