# Random Place Generator

## Overview
The **Random Place Generator** is a simple desktop application that generates a random location anywhere in the world. It provides a clickable Google Maps link to explore the location and a brief description of the place (if available). This app is perfect for adventurers or anyone looking to explore new and unexpected destinations virtually!

---

## Features
- **Generate Random Locations**: Click the button to generate a random location anywhere on Earth.
- **Clickable Google Maps Link**: Open the random location directly in Google Maps.
- **Place Description**: See the country, region, or description of the location (when available).
- **User-Friendly Interface**: Clean and straightforward design for quick interaction.
- **Resizable Window Disabled**: Keeps the app at a fixed size to maintain a consistent user experience.

---

## Installation

### Requirements
- Python 3.8 or higher
- Libraries:
  - `tkinter`
  - `geopy`
  - `webbrowser`

### Steps
1. Clone or download the repository.
2. Install the required Python libraries:
   ```bash
   pip install geopy
   ```
3. Run the application:
   ```bash
   python random_place_generator.py
   ```

---

## Compilation to Executable
To convert the Python script into a standalone executable:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Use the following command:
   ```bash
   pyinstaller --onefile --noconsole random_place_generator.py
   ```
3. Locate the executable in the `dist` folder.

---

## Usage
1. Open the application.
2. Click the **"Random Place in the World"** button.
3. View the generated location, its description, and the Google Maps link.
4. Click the link to explore the location in your browser.

---

## Screenshots
![image](https://github.com/user-attachments/assets/b4a7199a-1b39-4075-87fe-4f7c0f4ddb8e)
![image](https://github.com/user-attachments/assets/dd060ebe-02ec-4c3a-bba8-87f0a4210acd)
![image](https://github.com/user-attachments/assets/5904652a-7d64-4345-afa2-71ea883f5d6a)


---

## Contributing
If you would like to improve this project, feel free to submit a pull request or create an issue.

---

## Credits
- Created with Python and Tkinter.
- Location data powered by [Geopy](https://geopy.readthedocs.io/).
- Maps powered by [Google Maps](https://www.google.com/maps).
