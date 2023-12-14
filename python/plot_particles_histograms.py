
''' 
To run the code simply pass the channel names you would like to monitor, example:
    python plot_particles_histograms SLAM_PARTICLES   OTHER_PARTICLE_MESSAGES ...
''' 

import sys
sys.path.append("lcmtypes")
import lcm
from lcmtypes import particles_t
from lcmtypes import pose_xyt_t
lcm = lcm.LCM()
import pyqtgraph as pg
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, pyqtSlot, QObject
import numpy as np
import threading

class ParticlesHandler(QObject):
    update_plots = pyqtSignal(list)
    def __init__(self):
        QObject.__init__(self)
        self.curves = [None, None, None]
    def __call__(self, channel, msg):
        data = [[], [], []]
        for p in particles_t.decode(msg).particles:
            data[0].append(p.pose.x)
            data[1].append(p.pose.y)
            data[2].append(p.pose.theta)
        self.update_plots.emit(data)

class QtPlotsHandler(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent) 
        self.curves = [None, None, None]
        self.padding = 0.2
    def set_plots(self, plots):
        assert(len(plots)==3)
        self.plots = plots
    @pyqtSlot(list)
    def update(self, data):
        for i, data in enumerate(data):
            vals = np.array(data)
            mean, radius = vals.mean(), (vals.max()-vals.min())/2
            # y,x = np.histogram(vals, bins=np.linspace(-3, 8, 40))
            y,x = np.histogram(vals, bins='auto')
            if self.curves[i] is not None: 
                self.plots[i].removeItem(self.curves[i])
            self.curves[i] = pg.PlotCurveItem(x, y, stepMode=True, fillLevel=0, brush=(0, 0, 255, 80))
            self.plots[i].addItem(self.curves[i])
            self.plots[i].setXRange(mean - radius - self.padding, mean + radius + self.padding)

def handle_lcm(lcm):
    while True:
        lcm.handle()

if __name__ == '__main__':
    channels = [sys.argv[i] for i in range(1, len(sys.argv))]
    try:
        assert(len(channels) > 0)
    except: 
        sys.exit("Provide channel names to monitor as input arguments.")

    qt_app = QtGui.QApplication([])
    qt_widget = QtGui.QWidget()
    qt_layout = QtGui.QGridLayout()
    qt_widget.setLayout(qt_layout)

    data_handlers, plot_handlers = [], []
    plot_titles = ['x', 'y', 'theta']
    for i, ch in enumerate(channels):
        # Handle LCM messages
        data_handlers.append(ParticlesHandler())
        subscription = lcm.subscribe(ch, data_handlers[-1])

        # Display Message Channel Name
        title_bar = QtGui.QLabel(ch)
        title_bar.setAlignment(QtCore.Qt.AlignCenter)
        qt_layout.addWidget(title_bar, 2*i, 0, 1, 3)

        # Handle Qt plot updates
        plot_handlers.append(QtPlotsHandler())
        plots = []
        for plot_i in range(3):
            plots.append(pg.PlotWidget(title=plot_titles[plot_i]))
            qt_layout.addWidget(plots[-1], 2*i + 1, plot_i)
        plot_handlers[-1].set_plots(plots)

        # Connect LCM Data to Qt Plots
        data_handlers[-1].update_plots.connect(plot_handlers[-1].update)

    # Start up LCM Threads
    lcm_thread = threading.Thread(target=handle_lcm, args=(lcm, ), daemon=True)
    lcm_thread.start()

    # Show Plots
    qt_widget.show()
    sys.exit(qt_app.exec_())
