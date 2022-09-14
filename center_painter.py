from PyQt5.QtCore import QPointF, QPoint, QLine, QRect, QRectF, Qt
from PyQt5.QtGui import QPainter, QPixmap, QPolygon


class CenterPainter(QPainter):
    def __init__(self, pixmap: QPixmap = None):
        super(CenterPainter, self).__init__(pixmap)

        self.pixmap = pixmap
        self.x0 = int(pixmap.width() / 2) + 1
        self.y0 = int(pixmap.height() / 2) + 1
        self.origin = QPoint(self.x0, self.y0)
        # self.origin = QPoint(1, 1) + QPoint(pixmap.width(), pixmap.height()) / 2

    def drawPointC(self, point: [QPointF, QPoint]) -> None:
        point = self._to_origin_min1(point)
        return super(CenterPainter, self).drawPoint(point)

    def drawLineC(self, line: QLine) -> None:
        line = QLine(self._to_origin(line.p1()), self._to_origin(line.p2()))
        return super(CenterPainter, self).drawLine(line)

    def drawLinesC(self, lines: list) -> None:
        lines = list(map(lambda line: QLine(self._to_origin(line.p1()), self._to_origin(line.p2())), lines))
        return super(CenterPainter, self).drawLines(lines)

    def drawRectC(self, r: QRect) -> None:
        p1 = QPoint(self._to_origin(QPoint(r.x(), r.y())))
        p2 = QPoint(self._to_origin_min1(QPoint(r.width(), r.height())))
        r = QRect(p1, p2)
        return super(CenterPainter, self).drawRect(r)

    def drawEllipseC(self, r: QRectF) -> None:
        p1 = QPoint(self._to_origin_min1(QPoint(r.x(), r.y())))
        p2 = QPoint(self._to_origin_min1(QPoint(r.width(), r.height())))
        r = QRect(p1, p2)
        return super(CenterPainter, self).drawEllipse(r)

    def drawPolygonC(self, polygon: QPolygon, fillRule: Qt.FillRule = Qt.OddEvenFill) -> None:
        points = [self._to_origin(point) for point in polygon]
        polygon = QPolygon(points)
        return super(CenterPainter, self).drawPolygon(polygon, fillRule)

    def _to_origin(self, p: [QPointF, QPoint]):
        return p + self.origin

    def _to_origin_min1(self, p: [QPointF, QPoint]):
        return p + self.origin + QPoint(-1, -1)
