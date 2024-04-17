import os
import shutil
from datetime import datetime
import re

# Путь к директории с изображениями
image_dir = r"C:\Users\Dm1tr\OneDrive\Изображения\Снимки экрана"
undefined_dir = os.path.join(image_dir, "Неопределено")

if not os.path.exists(undefined_dir):
    os.makedirs(undefined_dir)


def extract_date(filename):
    match = re.search(r'\d{4}-\d{2}-\d{2}', filename)
    if match:
        return datetime.strptime(match.group(), '%Y-%m-%d').date()
    else:
        return None


for filename in os.listdir(image_dir):
    filepath = os.path.join(image_dir, filename)

    if filename.startswith("Снимок экрана") and filename.endswith(".png"):
        image_date = extract_date(filename)

        if image_date:
            date_dir = os.path.join(image_dir, str(image_date))
            if not os.path.exists(date_dir):
                os.makedirs(date_dir)
            shutil.move(filepath, os.path.join(date_dir, filename))
        else:
            shutil.move(filepath, os.path.join(undefined_dir, filename))

