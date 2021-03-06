from PyQt5.QtWidgets import QPushButton, QDialog, QComboBox, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...const import Settings_Logo, std_settings

from .Delete_Passive import Delete_Window
from .Change_User_Infos import Change_Window

import json
import os


class Settings_Window(QDialog):
    def __init__(self, active, parent=None):
        super().__init__(parent)

        self.active = active

        self.current_settings = open(f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\settings.json", "r")
        self.parsed = json.load(self.current_settings)

        self.currency_label = QLabel(self)
        self.currency_label.setText("Currency")

        self.currencys = QComboBox(self)
        self.currencys.addItems(["USD", "Euro"])
        self.currencys.setCurrentText("Euro")
        self.currencys.setCurrentText(self.parsed["currency"])
        self.currencys.setToolTip("Select to currency you want your money to be shown in")

        self.lang_label = QLabel(self)
        self.lang_label.setText("Language")

        self.languages = QComboBox(self)
        self.languages.addItems(["EN", "DE"])
        self.languages.setCurrentText(self.parsed["language"])
        self.languages.setToolTip("Select the language")

        self.darkmode_label = QLabel(self)
        self.darkmode_label.setText("Darkmode:")

        self.darkmode = QCheckBox(self)
        self.darkmode.setChecked(self.parsed["darkmode"])

        self.mod_label = QLabel(self)
        self.mod_label.setText("Modifiy: ")

        self.mod_btn = QPushButton("Modifiy", self)
        self.mod_btn.setToolTip("Click to open the menu with which you can modifiy your information")
        self.mod_btn.clicked.connect(self.mod)

        self.passive_label = QLabel(self)
        self.passive_label.setText("Delete Passive Income: ")

        self.passivebtn = QPushButton("Delete", self)
        self.passivebtn.setToolTip("Click to open the delete Menu")
        self.passivebtn.clicked.connect(self.del_passive)

        self.reset_label = QLabel(self)
        self.reset_label.setText("Reset Settings: ")
        
        self.reset = QPushButton("Reset", self)
        self.reset.setToolTip("Click to reset your settings")
        self.reset.clicked.connect(self.resetfunc)

        self.savebtn = QPushButton("Save", self)
        self.savebtn.setToolTip("Click to save the selected settings")
        self.savebtn.clicked.connect(self.save)

        currency_layout = QHBoxLayout()
        currency_layout.addWidget(self.currency_label)
        currency_layout.addWidget(self.currencys)

        lang_layout = QHBoxLayout()
        lang_layout.addWidget(self.lang_label)
        lang_layout.addWidget(self.languages)

        dark_layout = QHBoxLayout()
        dark_layout.addWidget(self.darkmode_label)
        dark_layout.addWidget(self.darkmode)

        mod_layout = QHBoxLayout()
        mod_layout.addWidget(self.mod_label)
        mod_layout.addWidget(self.mod_btn)

        del_layout = QHBoxLayout()
        del_layout.addWidget(self.passive_label)
        del_layout.addWidget(self.passivebtn)

        reset_layout = QHBoxLayout()
        reset_layout.addWidget(self.reset_label)
        reset_layout.addWidget(self.reset)
        
        root = QVBoxLayout()
        root.addLayout(currency_layout)
        root.addLayout(lang_layout)
        root.addLayout(dark_layout)
        root.addLayout(mod_layout)
        root.addLayout(del_layout)
        root.addLayout(reset_layout)
        root.addWidget(self.savebtn)

        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon(Settings_Logo))
        self.setGeometry(400, 400, 500, 750)
        self.setLayout(root)
        self.exec_()

    def resetfunc(self):
        path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\settings.json"

        with open(path, "w") as f_user: 
            std_file = json.dumps(std_settings, indent=4, sort_keys=False)
            f_user.write(std_file)
            f_user.close()

        self.close()

    def save(self):
        currency = self.currencys.currentText()
        language = self.languages.currentText()
        darkmode = self.darkmode.isChecked()

        path = f"C:\\Users\\{os.getlogin()}\\AppData\\local\\Expense_Tracker\\users\\{self.active}\\settings.json"

        dictio = {
            "currency": currency, 
            "language": language, 
            "darkmode": darkmode
        }

        parsed = json.dumps(dictio, indent=4, sort_keys=False)

        with open(path, "w") as f: 
            f.write(parsed)
            f.close()

        self.close()

    def del_passive(self):
        dialog = Delete_Window(self.active) 

    def mod(self):
        dialog = Change_Window(self.active) 
