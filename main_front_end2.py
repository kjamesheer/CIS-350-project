import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton
import sqlite3

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
        self.liquor_combo_box.hide()

        self.mixer_combo_box = QComboBox()
        layout.addWidget(self.mixer_combo_box)
        self.mixer_combo_box.hide()

        self.garnish_combo_box = QComboBox()
        layout.addWidget(self.garnish_combo_box)
        self.garnish_combo_box.hide()

        self.glass_combo_box = QComboBox()
        layout.addWidget(self.glass_combo_box)
        self.glass_combo_box.hide()

        #Populate comboboxes
        self.liquor_combobox()
        self.mixer_combobox()
        self.garnish_combobox()
        self.glass_combobox()

        # Create the back button
        self.back_button = QPushButton("Back")
        layout.addWidget(self.back_button)
        self.back_button.hide()  # Initially hide the back button

        # Connect a slot to handle back button clicks
        self.back_button.clicked.connect(self.handle_back_button_click)

    def liquor_combobox(self):
        connect = sqlite3.connect('drinks2.sqlite')
        cursor = connect.cursor()
        # Run the SQL query to get all unique liquor values
        query = "SELECT DISTINCT liquor FROM download_2;"
        cursor.execute(query)
        liquor_items = cursor.fetchall()
        # Populate the liquor combo box with options and set icons
        for liquor in liquor_items:
            self.liquor_combo_box.addItem(str(liquor[0]))
        connect.close()

    def mixer_combobox(self):
        connect = sqlite3.connect('drinks2.sqlite')
        cursor = connect.cursor()
        query = "SELECT DISTINCT mixer FROM download_2;"
        cursor.execute(query)
        mixer_items = cursor.fetchall()
        for mixer in mixer_items:
            self.mixer_combo_box.addItem(str(mixer[0]))
        connect.close()

    def garnish_combobox(self):
        connect = sqlite3.connect('drinks2.sqlite')
        cursor = connect.cursor()
        query = "SELECT DISTINCT garnish FROM download_2;"
        cursor.execute(query)
        garnish_items = cursor.fetchall()
        for garnish in garnish_items:
            self.garnish_combo_box.addItem(str(garnish[0]))
        connect.close()

    def glass_combobox(self):
        connect = sqlite3.connect('drinks2.sqlite')
        cursor = connect.cursor()
        query = "SELECT DISTINCT glass FROM download_2;"
        cursor.execute(query)
        glass_items = cursor.fetchall()
        for glass in glass_items:
            self.glass_combo_box.addItem(str(glass[0]))
        connect.close()

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
