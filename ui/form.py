from datetime import datetime
from logic.core import get_continents, get_countries_by_continent
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QMessageBox,
    QPushButton,
)
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


class FormWidget(QFormLayout):
    def __init__(self):
        super().__init__()

        self.current_country_selected = None

        # Continent list
        self.style_continents_list = QComboBox()
        self.style_continents_list.setPlaceholderText('Continent')
        self.style_continents_list.addItems(get_continents())
        self.style_continents_list.textActivated.connect(self.change_continent)

        # Country list
        self.style_countries_list = QComboBox()
        self.style_countries_list.setPlaceholderText('Country')
        self.style_countries_list.setEditable(True)
        self.style_countries_list.textActivated.connect(self.change_country)

        # Get time event
        self.style_get_time = QPushButton('Get Time')
        self.style_get_time.setDefault(True)
        self.style_get_time.clicked.connect(self.on_get_time_clicked)

        # Building form
        self.addRow('Select continent:', self.style_continents_list)
        self.addRow('Select country:', self.style_countries_list)
        self.addRow(self.style_get_time)

    @Slot(str)
    def change_continent(self, selected_continent):
        countries_by_iso_code = get_countries_by_continent(selected_continent)

        iso_code_by_countries = []
        for iso_code, countries in countries_by_iso_code.items():
            iso_code_by_countries.extend([{country: iso_code} for country in countries])

        self.style_countries_list.clear()
        self.style_countries_list.addItems(
            [next(iter(country_iso_code)) for country_iso_code in iso_code_by_countries]
        )

    @Slot(str)
    def change_country(self, selected_country):
        self.current_country_selected = selected_country

    @Slot()
    def on_get_time_clicked(self):
        try:
            zone = ZoneInfo(self.current_country_selected)
            now = datetime.now(zone)
            formatted_current_time = f'{now:%A %d de %B %Y at %I %M %p}'

            success_message = QMessageBox(
                QMessageBox.Icon.Information, 'Time', formatted_current_time
            )
            success_message.setStandardButtons(
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
            )
            success_message.setDefaultButton(QMessageBox.StandardButton.Ok)

            clicked_button = success_message.exec()
            if clicked_button == QMessageBox.StandardButton.Cancel:
                print('User cancel the operation')
        except ModuleNotFoundError as error:
            if 'tzdata' in error:
                QMessageBox.critical(
                    None, 'Dependency pending', 'Install tzdata dependency as dev'
                )
        except ZoneInfoNotFoundError as error:
            QMessageBox.critical(None, 'Timezone not found', str(error))
