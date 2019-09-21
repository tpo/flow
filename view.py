# originally based on https://codereview.stackexchange.com/questions/181401/laminar-flow-in-a-pipe-animation-using-tkinter
# by Putzikki
from tkinter import *

screenwidth = 200
screenheight = 200

color = "blue"

class Animation:
    """Class for the animation and buttons"""

    def __init__(self):
        """
        Creates the canvas, lines, buttons and runs the mainloop of the tkinter window
        self.objectlist is a list for the rows of pipes
        """

        self.root = Tk()
        self.canvas = Canvas(self.root, width=screenwidth, height=screenheight)
        self.canvas.pack()

        self.root.title("Laminar flow in a pipe")

        self.objectlist = []

        self.stop_animation = False
        self.start = Button(self.root, text="Start animation", command=self.start_anim)
        self.start.pack()
        self.stop = Button(self.root, text="Stop animation", command=self.stop_anim)
        self.stop.pack()

        self.init()
        self.root.mainloop()


    def start_anim(self):
        """Starts the animation"""

        self.stop_animation = False
        self.start.configure(state=DISABLED)
        self.stop.configure(state=NORMAL)
        self.update()


    def stop_anim(self):
        """
        Stops the animation and deletes the pipes
        Runs the function init to draw new pipes to the beginning positions
        """

        self.stop_animation = True
        self.start.configure(state=NORMAL)
        self.stop.configure(state=DISABLED)
        self.update()


    def init(self):
        """
        Creates connected machines and appends them to self.objectlist
        """

        self.objectlist = []
        self.objectlist.append(Machine(self.canvas,  0, 0, 10, 10, "red"   ))
        self.objectlist.append(Machine(self.canvas, 20, 0, 30, 10, "green" ))

        self.objectlist.append(Pipe(self.canvas, 10, 5,
                                                 20, 5, color))


    def update(self):
        """
        Updates the screen
            * t: update interval in milliseconds
        """

        t = 20

        if self.stop_animation == False:
            for o in self.objectlist:
                o.animate()

            self.canvas.after(t, self.update)



class Pipe():
    """
    Class for pipes

    Parameters:
        * canvas: canvas from the class "Animation"
        * x0, y0: start coordinate for the pipe
        * x1, y1: end   coordinate for the pipe
        * color: color of fluid in the pipe
    """


    def __init__(self, canvas, x0, y0, x1, y1, color):
        self.canvas = canvas
        self.line = self.canvas.create_line(x0, y0, x1, y1, fill=color, dash=[4,4], width=2)
        self.dashoffset = 0


    def animate(self):
        """
        Function for moving the "contents of the pipe.
        """
        self.dashoffset += 0.5
        self.canvas.itemconfig(self.line, dashoffset=self.dashoffset)



    def delete(self):
        """Function for deleting of the pipe"""

        self.canvas.delete(self.line)

class Machine():
    """
    Class for machines

    Parameters:
        * canvas: canvas from the class "Animation"
        * x0, y0: top left     machine coordinate
        * x1, y1: bottom right machine coordinate
        * color: color of the machine
    """


    def __init__(self, canvas, x0, y0, x1, y1, color):
        self.canvas = canvas
        self.rectangle = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)


    def animate(self):
        """
        Function for animating of the machine
        """


    def delete(self):
        """Function for deleting of the pipe"""

        self.canvas.delete(self.rectangle)

Animation()
