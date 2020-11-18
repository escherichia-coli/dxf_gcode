import ezdxf
import sys
import matplotlib.pyplot as plt
import numpy as np

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg


step = 0.01
precision = 3


def control_dist(x, y):
    control = []
    err_count = 0
    for i in range(len(x) - 1):
        control.append(np.sqrt((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2))
    if abs(max(control) - min(control)) < 0.05:
        print('***Control OK ***')
    else:
        print('***Control failed ***')
        # print('dist max : ', max(control))
        # print('dist min : ', min(control))
        # print('control = ', control)


def discretise_line(line):
    # line = np.round(line, precision)
    start = line[0]
    end = line[1]

    x = []
    y = []
    # print('start x pnt : ', start[0])
    # print('end x pnt : ', end[0])
    if start[0] == end[0]:
        # print('****** Vertical ******')
        len_line = abs(end[1] - start[1])
        if len_line <= step:
            return np.array([[start[0], end[0]], [start[1], end[1]]]).astype('float')
        n_pnt = int(len_line / step)
        x = (np.ones(n_pnt) * start[0]).astype('float')
        y = np.linspace(start[1], end[1], n_pnt)

    else:
        # print('****** Normal ******')
        len_line = np.sqrt((end[1] - start[1]) ** 2 + (end[0] - start[0]) ** 2)
        if len_line <= step:
            return np.array([[start[0], end[0]], [start[1], end[1]]]).astype('float')
        n_pnt = len_line / step
        a = (end[1] - start[1]) / (end[0] - start[0])
        b = start[1] - start[0] * a

        x_step = step / (len_line / abs(start[0] - end[0]))
        x = np.linspace(start[0], end[0], n_pnt)
        y = a * x + b

        # control_dist(x, y)
    return np.array([x, y]).astype('float')


def discretise_polyline(polyline):

    # print(polyline)

    x = discretise_line([polyline[0], polyline[1]])[0]
    y = discretise_line([polyline[0], polyline[1]])[1]

    for i in range(1, len(polyline) - 1, 1):
        x = np.concatenate((x, discretise_line([polyline[i], polyline[i + 1]])[0][1:]))
        y = np.concatenate((y, discretise_line([polyline[i], polyline[i + 1]])[1][1:]))

    try:
        control_dist(x, y)
    except ValueError:
        print('Control impossible')
    return np.array([x, y]).astype('float')


def discretise_circle(center_pnt, radius, start_angle=0, end_angle=360):
    print('**** discretise circle ****')
    # s_angle = min(start_angle, end_angle)
    # e_angle = max(start_angle, end_angle)
    start_angle = np.radians(start_angle)
    end_angle = np.radians(end_angle)
    print('start angle : ', start_angle)
    print('end angle : ', end_angle)
    perimeter = 2 * np.pi * radius
    n_pnt = perimeter / step
    # print(perimeter)

    if start_angle < np.pi and end_angle > np.pi:
        x = np.cos(np.linspace(start_angle, np.pi, n_pnt * abs(start_angle - np.pi) / (2 * np.pi)))
        y = np.sin(np.linspace(start_angle, np.pi, n_pnt * abs(start_angle - np.pi) / (2 * np.pi)))

        if end_angle < 2 * np.pi and end_angle > start_angle:
            x = np.concatenate((x, np.cos(np.linspace(np.pi, end_angle, n_pnt * abs(end_angle - np.pi) / (2 * np.pi)))[1:]))
            y = np.concatenate((y, np.sin(np.linspace(np.pi, end_angle, n_pnt * abs(end_angle - np.pi) / (2 * np.pi)))[1:]))
        else:
            x = np.concatenate((x, np.cos(np.linspace(np.pi, 2 * np.pi, n_pnt / 2))[1:]))
            y = np.concatenate((y, np.sin(np.linspace(np.pi, 2 * np.pi, n_pnt / 2))[1:]))
            x = np.concatenate((x, np.cos(np.linspace(0, end_angle, n_pnt * end_angle / (2 * np.pi)))[1:]))
            y = np.concatenate((y, np.sin(np.linspace(0, end_angle, n_pnt * end_angle / (2 * np.pi)))[1:]))

    elif start_angle > np.pi and end_angle < np.pi:
        x = (np.cos(np.linspace(start_angle, 2 * np.pi, n_pnt * abs(start_angle - (2 * np.pi)) / (2 * np.pi))))
        y = (np.sin(np.linspace(start_angle, 2 * np.pi, n_pnt * abs(start_angle - (2 * np.pi)) / (2 * np.pi))))

        if end_angle < np.pi and end_angle < start_angle:
            x = np.concatenate((x, np.cos(np.linspace(0, end_angle, n_pnt * end_angle / (2 * np.pi)))[1:]))
            y = np.concatenate((y, np.sin(np.linspace(0, end_angle, n_pnt * end_angle / (2 * np.pi)))[1:]))
        else:
            x = np.concatenate((x, np.cos(np.linspace(0, np.pi, n_pnt / 2))[1:]))
            y = np.concatenate((y, np.sin(np.linspace(0, np.pi, n_pnt / 2))[1:]))
            x = np.concatenate((x, np.cos(np.linspace(np.pi, end_angle, n_pnt * abs(np.pi - end_angle) / (2 * np.pi)))[1:]))
            y = np.concatenate((y, np.sin(np.linspace(np.pi, end_angle, n_pnt * abs(np.pi - end_angle) / (2 * np.pi)))[1:]))

    elif start_angle < np.pi and end_angle < np.pi:
        x = np.cos(np.linspace(start_angle, end_angle, n_pnt))
        y = np.sin(np.linspace(start_angle, end_angle, n_pnt))

    elif start_angle > np.pi and end_angle > np.pi:
        x = np.cos(np.linspace(start_angle, end_angle, n_pnt))
        y = np.sin(np.linspace(start_angle, end_angle, n_pnt))

    x = x * radius + center_pnt[0]
    y = y * radius + center_pnt[1]

    control_dist(x, y)
    return np.array([x, y]).astype('float')


try:
    doc = ezdxf.readfile("Drawing1.dxf")
    # doc = ezdxf.readfile("PLANdZ.dxf")

except IOError:
    print(f'Not a DXF file or a generic I/O error.')
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f'Invalid or corrupted DXF file.')
    sys.exit(2)


def print_entity(e):
    print("LINE on layer: %s\n" % e.dxf.layer)


polylines = []
d_lines = []
d_circles = []
msp = doc.modelspace()
for e in msp:
    print('=====================\n')
    print(e.dxftype())
    polyline = []

    if e.dxftype() == 'LWPOLYLINE':

        print('**** LWPOLYLINE ****')
        for f in e:
            polyline.append([f[0], f[1]])

        polylines.append(polyline)
        d_lines.append(discretise_polyline(polyline))

    if e.dxftype() == 'CIRCLE':

        print('**** CIRCLE ****')

        d_circles.append(discretise_circle(e.dxf.center, e.dxf.radius))

    if e.dxftype() == 'ARC':

        print('**** ARC ****')
        d_circles.append(discretise_circle(e.dxf.center, e.dxf.radius, e.dxf.start_angle, e.dxf.end_angle))

    if e.dxftype() == 'SPLINE':

        print('**** SPLINE ****')
        print(e.dxf.n_knots)
        print(e.dxf.n_fit_points)


app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800, 800)
view = pg.PlotWidget()  # GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('pyqtgraph example: ScatterPlot')


fig = []
n_points = 0
drawing = []
i = 0
for d_line in d_lines:

    drawing.append(view.plot(d_line[0], d_line[1], connect='all', data=i, clickable=True))
    drawing[-1].curve.setClickable(True)
    i = i + 1


lastClicked = []
selected_curves = []
a = np.radians(-90)
r_mat = [[np.cos(a), -np.sin(a)],
         [np.sin(a), np.cos(a)]]
r_mat = np.array(r_mat).astype('float')


def get_intersect(a1, a2, b1, b2):
    """ 
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1, a2, b1, b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return None
    return (x / z, y / z)


def offset_line(offset, lines):
    # print('\n ****** CLICKED ******')
    # print('line to offset : ', lines)
    x_off = []
    y_off = []
    x = [line[0] for line in lines]
    # print(x)
    y = [line[1] for line in lines]
    # print(y)
    for i in range(0, len(x) - 1, 1):
        vector = np.array([x[i + 1] - x[i], y[i + 1] - y[i]]).astype('float')
        print(vector)
        norm = np.linalg.norm(vector)
        r_vect = np.dot(r_mat, vector)
        r_vect_u = np.round(r_vect / norm, precision)

        # print('normal vector : ', r_vect_u)

        x_off.append(x[i: i + 2] + r_vect_u[0] * offset)
        y_off.append(y[i: i + 2] + r_vect_u[1] * offset)

    x_off = np.array(x_off).astype('float').flatten()
    y_off = np.array(y_off).astype('float').flatten()
    # print('x_off before inter : ', x_off)
    # print('y_off before inter : ', y_off)
    inter = 0
    for i in range(0, len(x_off) - 3, 2):
        # print('bob')
        p1 = [x_off[i + 0], y_off[i + 0]]
        p2 = [x_off[i + 1], y_off[i + 1]]
        p3 = [x_off[i + 2], y_off[i + 2]]
        p4 = [x_off[i + 3], y_off[i + 3]]

        inter = get_intersect(p1, p2, p3, p4)
        # print('inter : ', inter)

        if inter is not None:
            x_off[i + 1] = inter[0]
            x_off[i + 2] = inter[0]
            y_off[i + 1] = inter[1]
            y_off[i + 2] = inter[1]
        else:
            break

    # print('x_off after inter : ', x_off)
    # print('y_off after inter : ', y_off)
    pnts = list([x_off[i], y_off[i]] for i in range(len(x_off)))
    # print('pnts : ', pnts)
    len_pnts = len(pnts)
    new_pnts = []
    for i in range(0, len_pnts, 2):
        new_pnts.append(pnts[i])

    new_pnts.append(pnts[-1])
    # print('new pnts : ', new_pnts)
    pnts = new_pnts

    

    if inter is not None:
        # print('return inter : ', np.array([x_off, y_off]).astype('float'))
        return np.round(np.array(pnts), precision).astype('float')
    else:
        raise ValueError
        print('Problem')
        # print('intersection : ', inter)


def clicked(curve):
    for c in lastClicked:
        c.setPen('w', size=38)
    curve.setPen('r', size=38)
    n_curve = curve.opts.get('data')
    # print('n° line : ', curve.opts.get('data'))
    # print('len polyline : ', len(polylines) - 1)
    lastClicked.append(curve)
    offset = np.arange(0, 1, 0.1)
    try:
        for o in offset:
            polylines.append(offset_line(o, polylines[n_curve]))
            # print('polylines [-0]', polylines[0])
            # print('polylines [-1]', polylines[-1])
            d_lines.append(discretise_polyline(polylines[-1]))
            # print(d_lines[-1])
            drawing.append(view.plot(d_lines[-1][0], d_lines[-1][1], pen=('b'), connect='all', data=int(len(polylines) - 1), clickable=True))
            # drawing[-1].curve.setClickable(True)
            # drawing[-1].sigClicked.connect(clicked)
            view.update()

    except ValueError:
        print('Operation impossible. Verifier la géometrie')


for d in drawing:
    d.sigClicked.connect(clicked)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
