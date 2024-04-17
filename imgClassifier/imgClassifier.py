import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import subprocess
from threading import Thread
import os
import shutil
from datetime import datetime
import re

if getattr(sys, 'frozen', False):
    # Если программа была скомпилирована с помощью PyInstaller
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)
icon_path = os.path.join(basedir, 'icon.png')


IMGSPATH = r"C:\Users\Dm1tr\OneDrive\Изображения\Снимки экрана"
undefined_dir = os.path.join(IMGSPATH, "Неопределено")


def run_script():
    sortimages()


def sortimages():
    if not os.path.exists(undefined_dir):
        os.makedirs(undefined_dir)
    
    for filename in os.listdir(IMGSPATH):
        filepath = os.path.join(IMGSPATH, filename)

        if filename.startswith("Снимок экрана") and filename.endswith(".png"):
            image_date = extract_date(filename)

            if image_date:
                date_dir = os.path.join(IMGSPATH, str(image_date))
                if not os.path.exists(date_dir):
                    os.makedirs(date_dir)
                shutil.move(filepath, os.path.join(date_dir, filename))
            else:
                shutil.move(filepath, os.path.join(undefined_dir, filename))


def extract_date(filename):
    match = re.search(r'\d{4}-\d{2}-\d{2}', filename)
    if match:
        return datetime.strptime(match.group(), '%Y-%m-%d').date()
    else:
        return None


def main():
    sortimages()
    app = QApplication(sys.argv)
    tray_icon = QSystemTrayIcon(QIcon(icon_path), app)

    menu = QMenu()
    run_action = QAction("Запустить обработчик", menu)
    quit_action = QAction("Выйти", menu)

    menu.addAction(run_action)
    menu.addAction(quit_action)

    tray_icon.setContextMenu(menu)
    tray_icon.show()

    run_action.triggered.connect(run_script)
    quit_action.triggered.connect(app.quit)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
