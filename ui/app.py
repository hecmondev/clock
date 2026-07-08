from PySide6.QtWidgets import (
    QApplication,
)
from ui.form import FormWidget
from ui.layout import LayoutWidget
import sys


class AppWidget(LayoutWidget):
    def __init__(self):
        super().__init__()

        # Loading the actions widgets
        self.layout.addLayout(FormWidget(), 1, 0, 1, 2)


def init():
    """
    Initializes the application.
    """
    app = QApplication(sys.argv)

    app_widget = AppWidget()
    app_widget.resize(400, 200)
    app_widget.setMaximumSize(400, 200)
    app_widget.show()

    sys.exit(app.exec())
