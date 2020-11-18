import numpy as np
import matplotlib.pyplot as plt


class DXFtoGCODE_Geometry(object):
    def __init__(self):
        self.side = 'positif'
        self.precision = 3
        self.offset = 0.1
        pass

    def __get_intersect(self, a1, a2, b1, b2):
        """
        Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
        a1: [x, y] a point on the first line
        a2: [x, y] another point on the first line
        b1: [x, y] a point on the second line
        b2: [x, y] another point on the second line
        """
        s = np.vstack([a1, a2, b1, b2])      # s for stacked
        h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
        l1 = np.cross(h[0], h[1])            # get first line
        l2 = np.cross(h[2], h[3])            # get second line
        x, y, z = np.cross(l1, l2)           # point of intersection
        if z == 0:                           # lines are parallel
            return None
        return (x / z, y / z)

    def __offsetLine(self, line, o=0.1):

        a = np.radians(90)
        r_mat = [[np.cos(a), -np.sin(a)],
                 [np.sin(a), np.cos(a)]]
        r_mat = np.array(r_mat)
        vector = [line[1][0] - line[0][0], line[1][1] - line[0][1]]
        norm = np.linalg.norm(vector)
        n_vector = np.dot(r_mat, vector)
        unit_n_vector = np.round(n_vector / norm, self.precision)
        # print(np.array(line + unit_n_vector * self.offset))
        return line + unit_n_vector * o

    def __offsetPolyline(self, polyline, offset=0.1, side=1):
        offset_lines = []

        for i in range(len(polyline) - 1):
            offset_line = self.__offsetLine([polyline[i], polyline[i + 1]], o=offset)
            offset_lines.append(offset_line[0])
            offset_lines.append(offset_line[1])
        # offset_lines = np.array(offset_lines).astype('float')
        inter = None
        # print('offset lines ', offset_lines)
        # print(offset_lines)
        for i in range(0, len(offset_lines) - 3, 2):
            p1 = offset_lines[i + 0]
            p2 = offset_lines[i + 1]
            p3 = offset_lines[i + 2]
            p4 = offset_lines[i + 3]

            # print('p1 ', p1)

            inter = self.__get_intersect(p1, p2, p3, p4)

            if inter is not None:
                offset_lines[i + 1] = inter
                offset_lines[i + 2] = inter

        return np.array(offset_lines).astype('float')

    def setThickness(self, polyline, thickness, side='alt'):
        offset_lines = []
        offset_list = np.ones(int(thickness / self.offset))
        if side == 'pos':
            offset_list = np.arange(self.offset, thickness + self.offset, self.offset)
        elif side == 'neg':
            offset_list = - np.arange(self.offset, thickness + self.offset, self.offset)
        elif side == 'alt':
            n = -1
            # offset_list[0] = self.offset
            j = 1
            for i in range(0, len(offset_list) - 1, 2):
                offset_list[i + 0] = j * n ** (j + 0) * self.offset
                offset_list[i + 1] = j * n ** (j + 1) * self.offset
                j = j + 1

        else:
            raise AttributeError
            print('side must be : "pos", "neg" or "alt"')

        # print(offset_list)

        for i in offset_list:
            offset_lines.append(self.__offsetPolyline(polyline, offset=i))

        return np.array(offset_lines).astype('float')

    def __getAngle(self, v1, v2):
        uv1 = v1 / np. linalg. norm(v1)
        uv2 = v2 / np. linalg. norm(v2)
        dot_product = np. dot(uv1, uv2)
        angle = np.arccos(dot_product)
        return angle

    def clean(self, polylines):
        new_polylines = []
        n = 0
        for polyline in polylines:
            lines = []
            t_pl = []
            split = 0
            for i in range(len(polyline) - 1):
                lines.append([polyline[i], polyline[i + 1]])

            lines = np.array(lines)
            # print(lines)
            for i in range(len(lines) - 1):

                v1 = vector = [lines[i + 0][1][0] - lines[i + 0][0][0], lines[i + 0][1][1] - lines[i + 0][0][1]]
                v2 = vector = [lines[i + 1][1][0] - lines[i + 1][0][0], lines[i + 1][1][1] - lines[i + 1][0][1]]
                a = self.__getAngle(v1, v2)
                # print(np.degrees(a))
                if abs(np.degrees(a)) >= 168 or abs(np.degrees(a)) <= 0.05:
                    t_pl.append(lines[split:i + 2, 0])
                    split = i

            if split != len(lines):
                t_pl.append(lines[split + 1:, 0])
            # print(t_pl)
        # print(t_pl[-1])
        # print(lines[-1][1])
            t_pl[-1] = np.concatenate([t_pl[-1], [lines[-1][1]]])
            for pl in t_pl:
                new_polylines.append(pl)
        return new_polylines


if __name__ == '__main__':
    a = DXFtoGCODE_Geometry()
    plt.figure()
    line1 = [[0, 0], [1, 1], [2, 0], [7, 5], [5, 2], [7, -4]]
    line1 = a.clean([line1])

    lines2 = []
    for line in line1:
        # print(line[0])
        lines2.append(a.setThickness(line, 1, 'alt'))

    for line in line1:
        x1 = [line[i][0] for i in range(len(line))]
        y1 = [line[i][1] for i in range(len(line))]
        plt.plot(x1, y1)

    for line2 in lines2:
        for line in line2:
            x2 = [line[i][0] for i in range(len(line))]
            y2 = [line[i][1] for i in range(len(line))]
            # print('x2 : ', x2)
            plt.plot(x2, y2)
    # print('line 2 : ', line2)
    plt.axis('equal')
    plt.show()

    # print(a.offsetLine())
