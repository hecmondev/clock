from logic.utils import get_asset
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QGridLayout, QLabel, QVBoxLayout, QWidget


class LayoutWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Setting up the icon and the title for the window bar
        self.setWindowIcon(QIcon(get_asset('clock.ico')))
        self.setWindowTitle('Timezone App')

        # Main layout
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)

        # App title
        self.style_title = QLabel('Timezones', alignment=Qt.AlignmentFlag.AlignCenter)

        # App image
        self.style_image = QLabel()
        self.style_image.setPixmap(
            QPixmap(get_asset('clock_256.png')).scaled(
                100, 100, Qt.AspectRatioMode.IgnoreAspectRatio
            )
        )

        # Middle top space
        self.style_middle = QVBoxLayout()
        self.style_middle.addWidget(self.style_title)
        self.style_middle.addWidget(self.style_image)

        # Adding the middle space to the main layout
        self.layout.addLayout(
            self.style_middle, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter
        )
