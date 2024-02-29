# -*- coding: utf-8 -*-
# drink_recipes/main.py

"""This module provides the main drink recipes application."""

import sys
from PyQt5.QtWidgets import QApplication
# from .database import createConnection
from drink_recipes.front_end import MainWindow

def main():
    app = QApplication(sys.argv)
    # if not createConnection("drink_ingredients.sqlite"):
    #     sys.exit(1)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
