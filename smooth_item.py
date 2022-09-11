from PyQt5.QtCore import QRectF, Qt, QLineF
from PyQt5.QtGui import QPainter, QPixmap, QPen
from PyQt5.QtWidgets import QGraphicsEllipseItem, QStyleOptionGraphicsItem, QWidget, QGraphicsLineItem, \
    QGraphicsRectItem


class SmoothLineItem(QGraphicsLineItem):
    def __init__(self, line: QLineF, pen: QPen, parent=None):
        super(SmoothLineItem, self).__init__(parent)
        self.setLine(line)
        self.setPen(pen)
        self.setPos(-0.5, -0.5)

    def boundingRect(self) -> QRectF:
        return self.scene().sceneRect()

    def redraw_pix(self):
        pixmap = QPixmap(self.scene().width(), self.scene().height())
        pixmap.fill(Qt.transparent)
        pix_painter = QPainter(pixmap)
        pix_painter.drawLine(self.line())
        return pixmap

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget) -> None:
        painter.setPen(self.pen())
        pixmap = self.redraw_pix()
        pixmap_rect = QRectF(pixmap.rect())
        painter.drawPixmap(self.boundingRect(), pixmap, pixmap_rect)


class SmoothRectItem(QGraphicsRectItem):
    def __init__(self, rect: QRectF, pen: QPen, parent=None):
        super(SmoothRectItem, self).__init__(parent)
        self.setRect(rect)
        self.setPen(pen)
        self.setPos(-0.5, -0.5)

    def boundingRect(self) -> QRectF:
        return self.scene().sceneRect()

    def redraw_pix(self):
        pixmap = QPixmap(self.scene().width(), self.scene().height())
        pixmap.fill(Qt.transparent)
        pix_painter = QPainter(pixmap)
        pix_painter.drawRect(self.rect())
        return pixmap

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget) -> None:
        painter.setPen(self.pen())
        pixmap = self.redraw_pix()
        pixmap_rect = QRectF(pixmap.rect())
        painter.drawPixmap(self.boundingRect(), pixmap, pixmap_rect)


class SmoothEllipseItem(QGraphicsEllipseItem):
    def __init__(self, rect: QRectF, pen: QPen, parent=None):
        super(SmoothEllipseItem, self).__init__(parent)
        self.setRect(rect)
        self.setPen(pen)
        self.setPos(-0.5, -0.5)

    def boundingRect(self) -> QRectF:
        return self.scene().sceneRect()

    def redraw_pix(self):
        pixmap = QPixmap(self.scene().width(), self.scene().height())
        pixmap.fill(Qt.transparent)
        pix_painter = QPainter(pixmap)
        pix_painter.drawEllipse(self.rect())
        return pixmap

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget) -> None:
        painter.setPen(self.pen())
        pixmap = self.redraw_pix()
        pixmap_rect = QRectF(pixmap.rect())
        painter.drawPixmap(self.boundingRect(), pixmap, pixmap_rect)