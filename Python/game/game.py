import tkinter as tk

class PlayComponent:
    def __init__(self, canvas, item):
        self.item = item
        self.canvas = canvas

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def position(self):
        return self.canvas.coords(self.item)
    
    def delete(self):
        self.canvas.dele(self.item)


class Paddle(PlayComponent):
    def __init__(self, canvas, x, y):
        self.height = 5
        self.width = 100
        self.ball = None
        item = canvas.create_rectangle(x-self.width/2,
                                       y-self.height/2,
                                       x+self.width/2,
                                       y+self.height/2,
                                       fill = 'green')
        
        super(Paddle,self).__init__(canvas, item)


class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)

        self.width = 1000
        self.height = 400

        self.canvas = tk.Canvas(self, bg="cornsilk",
                                width = self.width,
                                height = self.height)
        
        self.canvas.pack()
        self.pack()

        self.item = {}

    def init_game(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title("")
    game = Game(root)
    game.mainloop()