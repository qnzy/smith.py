"""
smith.py, a simple minimalistic Smith Chart plotter.
See the end of this file for example usage.

public domain / CC0
"""

import numpy as np
import matplotlib.pyplot as pp

class smith:
    """
    Simple Smith Chart drawing.
    """

    def __init__(self, Z0=50):
        """
        Creates the figure and draws the grid.
        """
        pp.ioff()
        self.Z0=Z0
        self.fig = pp.figure(figsize=(8.0, 8.0))
        pp.axes().set_axis_off()
        self.drawGrid()

    def show(self):
        """
        Shows the plot. The plot can't be updated after it has been
        closed.
        """
        self.fig.show()

    def save(self, filename):
        """
        Saves the plot to filename. The extension defines the filetype.
        """
        self.fig.savefig(filename)

    def drawZList(self, l, c='b'):
        """
        Draws a list of impedances on the chart and connects them by lines. 
        To get a closed contour, the last impedance should be the same as the 
        first one. Use color c for the drawing.
        """
        pp.figure(self.fig.number)
        xlst = [self.z2gamma(z).real for z in l]
        ylst = [self.z2gamma(z).imag for z in l]
        pp.plot(xlst, ylst, c)
        pp.draw()

    def drawXCircle(self, x, npts=200):
        """
        Draws a circle with constant real part.
        """
        zlst = [x]+[complex(x, z) for z in np.logspace(0, 6, npts)]
        self.drawZList(zlst, 'k')
        zlst = [x]+[complex(x, -z) for z in np.logspace(0, 6, npts)]
        self.drawZList(zlst, 'k')

    def drawYCircle(self, y, npts=200):
        """
        Draws a circle with constant imaginary part.
        """
        zlst = [complex(0, y)]+[complex(z, y) for z in np.logspace(0, 6, npts)]
        self.drawZList(zlst,'k')

    def markZ(self, z, size=1):
        """
        Marks an impedance with a dot.
        """
        pp.figure(self.fig.number)
        g = self.z2gamma(z)
        pp.plot(g.real, g.imag, 'ob')
        pp.draw()
 
    def drawGrid(self):
        """
        Draws the Smith Chart grid.
        """
        self.drawXCircle(0)
        self.drawXCircle(self.Z0/5)
        self.drawXCircle(self.Z0/2)
        self.drawXCircle(self.Z0)
        self.drawXCircle(self.Z0*2)
        self.drawXCircle(self.Z0*5)
        self.drawYCircle(0)
        self.drawYCircle(self.Z0/5)
        self.drawYCircle(-self.Z0/5)
        self.drawYCircle(self.Z0/2)
        self.drawYCircle(-self.Z0/2)
        self.drawYCircle(self.Z0)
        self.drawYCircle(-self.Z0)
        self.drawYCircle(self.Z0*2)
        self.drawYCircle(-self.Z0*2)
        self.drawYCircle(self.Z0*5)
        self.drawYCircle(-self.Z0*5)

    def z2gamma(self, zl):
        """
        Converts an impedance to a reflection coefficient.
        """
        return complex(zl-self.Z0)/(zl+self.Z0)
 

if __name__ == '__main__':
    smith = smith()
    smith.markZ(20+30j)
    smith.markZ(130-60j)
    smith.drawZList([0, 50j, 10000j, -50j, 0])
    smith.show()
    raw_input()
    
