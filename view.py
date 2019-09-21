# originally based on https://codereview.stackexchange.com/questions/181401/laminar-flow-in-a-pipe-animation-using-tkinter
# by Putzikki
from tkinter import *

columns = 25

screenwidth = 200
screenheight = 200

color = "blue"

class Animation:
    """Class for the animation and buttons"""

    def __init__(self):
        """
        Creates the canvas, lines, buttons and runs the mainloop of the tkinter window
        self.pipelist is a list for the rows of pipes
        """

        self.root = Tk()
        self.canvas = Canvas(self.root, width=screenwidth, height=screenheight)
        self.canvas.pack()

        self.root.title("Laminar flow in a pipe")

        self.pipelist = []

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

        for i in range(len(self.pipelist)):
            xlist = self.pipelist[i]
            for pipe in xlist:
                pipe.delete()
            self.pipelist[i] = []

        self.init()


    def init(self):
        """
        Creates lists of pipes and appends them to self.pipelist
        """

        x0 = 0
        y0 = 10
        xlist = []

        for t in range(columns):
            xlist.append(Pipe(self.canvas, x0, y0,
                                           x0 + screenwidth,
                                           y0 + screenheight, color))

        self.pipelist.append(xlist)


    def update(self):
        """
        Updates the screen
            * t: update interval in milliseconds
        """

        t = 20

        if self.stop_animation == False:
            for i in range(len(self.pipelist)):
                xlist = self.pipelist[i]
                for pipe in xlist:
                    pipe.transport()

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


    def transport(self):
        """
        Function for moving the "contents of the pipe.
        """
        self.dashoffset += 0.5
        self.canvas.itemconfig(self.line, dashoffset=self.dashoffset)



    def delete(self):
        """Function for deleting of the pipe"""

        self.canvas.delete(self.line)

Animation()
