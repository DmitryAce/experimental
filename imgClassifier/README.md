## Sorting Screenshots Application

```cmd
imgClassifier.py
```

This Python application is designed to automatically organize screenshots stored in a specified directory on your computer. It utilizes PyQt5 for creating a system tray icon with a menu for easy access and control.

### Features

- **Automatic Sorting**: The application automatically sorts screenshots based on their filenames into subdirectories according to their capture dates.
  
- **System Tray Integration**: The application runs in the system tray, allowing users to easily access its functionality with a right-click menu.
  
- **Customization**: Users can customize the directory where screenshots are stored and the directory structure for organizing them.

### Installation

To install the application, follow these steps:

1. **Clone the Repository**: Clone or download the repository to your local machine.

2. **Navigate to the Code Folder**: Open a command prompt (cmd) and navigate to the folder containing the application code.

3. **Execute PyInstaller Command**: Run the following command to generate the executable file:
   ```powershell
   pyinstaller --onefile --noconsole --icon=icon.ico --add-data "icon.png;." imgClassifier.py
   ```

   This command compiles the Python script (`imgClassifier.py`) into a standalone executable file with no console window, using `icon.ico` as the application icon and including `icon.png` as a resource.

4. **Find Executable**: Once the command finishes execution, navigate to the `dist` directory within the code folder. You will find the generated executable file (`imgClassifier.exe`).

### Usage

1. **Setup**: Before running the application, ensure that PyQt5 is installed (`pip install PyQt5`).

2. **Configuration**: Modify the `IMGSPATH` variable in the `imgClassifier.py` script to point to the directory where your screenshots are stored.

3. **Installation**: described above.

4. **Execution**: Double-click the `imgClassifier.exe` file to launch the application. The system tray icon will appear, indicating that the application is running.

5. **Tray Icon**: Right-click on the tray icon to access the menu options.

6. **Sorting**: Screenshots are sorted automatically when the application is launched and can also be sorted manually by selecting "Запустить обработчик" (Run Script) from the menu.

7. **Auto-Start Configuration (Optional)**: To configure the application to run automatically on system startup and ensure screenshots are sorted with each system boot, follow these steps:
   - **Windows**: Create a shortcut to the `imgClassifier.exe` file and place it in the Windows Startup folder (`C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`).

8. **Exit**: To exit the application, select "Выйти" (Quit) from the menu.

### Note

- This application assumes that screenshots are saved in PNG format and follow the naming convention "Снимок экрана_YYYY-MM-DD.png". Adjust the filename pattern and date format if necessary.

- Ensure that the application has appropriate permissions to read and move files in the specified directories.

- This README assumes familiarity with Python and PyQt5. If you encounter any issues or need further assistance, refer to the PyQt5 documentation or seek help from the developer community.