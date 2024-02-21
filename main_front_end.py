import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liquor Recipe Ingredient Search System")
        self.setGeometry(700, 700, 850, 850) # (x, y, width, height)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Create the first QComboBox for selecting ingredient types
        self.type_combo_box = QComboBox()
        self.type_combo_box.addItems(["Select Type", "Liquor", "Mixer", "Garnish", "Glass"])
        layout.addWidget(self.type_combo_box)

        # Connect a slot to handle type selection changes
        self.type_combo_box.currentIndexChanged.connect(self.handle_type_selection)

        # Create the second QComboBox for selecting specific liquor types
        self.liquor_combo_box = QComboBox()
        layout.addWidget(self.liquor_combo_box)
        self.liquor_combo_box.hide()  # Initially hide this combo box

        self.mixer_combo_box = QComboBox()
        layout.addWidget(self.mixer_combo_box)
        self.mixer_combo_box.hide()

        self.garnish_combo_box = QComboBox()
        layout.addWidget(self.garnish_combo_box)
        self.garnish_combo_box.hide()

        self.glass_combo_box = QComboBox()
        layout.addWidget(self.glass_combo_box)
        self.glass_combo_box.hide()

        # Populate the liquor combo box with options and set icons
        liquor_items = ["Select Liquor", "Vodka", "Gin", "Rum", "Whiskey"]
        for liquor in liquor_items:
            self.liquor_combo_box.addItem(liquor)

        mixer_items = ["Select Mixer", "Pop", "Juice", "Syrup", "Ginger Ale"]
        for mixer in mixer_items:
            self.mixer_combo_box.addItem(mixer)

        garnish_items = ["Select Garnish", "Cinnamon", "Salt rim", "Fruit", "Citrus"]
        for garnish in garnish_items:
            self.garnish_combo_box.addItem(garnish)

        glass_items = ["Select Glass", "Wine", "Collins", "Highball", "Martini"]
        for glass in glass_items:
            self.glass_combo_box.addItem(glass)

        # Create the back button
        self.back_button = QPushButton("Back")
        layout.addWidget(self.back_button)
        self.back_button.hide()  # Initially hide the back button

        # Connect a slot to handle back button clicks
        self.back_button.clicked.connect(self.handle_back_button_click)

    def handle_type_selection(self, index):
        selected_type = self.type_combo_box.currentText()
        if selected_type == "Liquor":
            self.type_combo_box.hide()
            self.liquor_combo_box.show()
            self.back_button.show()
        elif selected_type == "Mixer":
            self.type_combo_box.hide()
            self.mixer_combo_box.show()
            self.back_button.show()
        elif selected_type == "Garnish":
            self.type_combo_box.hide()
            self.garnish_combo_box.show()
            self.back_button.show()
        elif selected_type == "Glass":
            self.type_combo_box.hide()
            self.glass_combo_box.show()
            self.back_button.show()
        else:
            self.liquor_combo_box.hide()
            self.mixer_combo_box.hide()
            self.garnish_combo_box.hide()
            self.glass_combo_box.hide()
            self.back_button.hide()
            self.type_combo_box.show()

    def handle_back_button_click(self):
        self.liquor_combo_box.hide()
        self.mixer_combo_box.hide()
        self.garnish_combo_box.hide()
        self.glass_combo_box.hide()
        self.back_button.hide()
        self.type_combo_box.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
