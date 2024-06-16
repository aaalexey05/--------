![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Welcome+to+my+git+page.)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=aaalexey05&layout=compact)

# --------

Welcome to the -------- repository! 🎉 This project contains a collection of different programs and scripts developed using various programming languages. The repository is structured to help you easily navigate through each project.

## Projects Overview

### ConsoleApp1
A C# console application demonstrating basic programming concepts and practices.

### Python
A collection of Python scripts showcasing different functionalities and algorithms. Ideal for beginners and intermediate programmers.

### css10
Contains examples and projects using CSS for styling web pages. Includes modern design techniques and best practices.

## Getting Started

To get started with any of these projects, follow the instructions below:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/aaalexey05/--------.git
    ```
2. **Navigate to the desired project directory:**
    ```bash
    cd --------/ProjectName
    ```
3. **Follow the README instructions in each project for setup and usage.**

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Contact

For questions or suggestions, feel free to open an issue or reach out to: alexeshilyaev@yandex.ru

# Python Projects and HTML/CSS Project Description

## Python Projects

### Project 1: Python Calculator Project
**Description**: This project demonstrates a simple Python script that performs data analysis on a given dataset. It includes functionalities for data cleaning, visualization, and statistical analysis.
![](https://github.com/aaalexey05/--------/blob/main/file/image7.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image8.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image9.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image10.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image11.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image12.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image13.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image14.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image15.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image16.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image17.png)
![](https://github.com/aaalexey05/--------/blob/main/file/image18.png)


**Features**:
- Data cleaning and preprocessing
- Data visualization using matplotlib
- Statistical analysis and hypothesis testing
  
- **Design IMT Calculator**:
![](https://github.com/aaalexey05/--------/blob/main/file/image4.png)

- **Design Generation Password**:
![](https://github.com/aaalexey05/--------/blob/main/file/image5.png)
  
- **JSON**:
![](https://github.com/aaalexey05/--------/blob/main/file/image6.png)     

Weather App
This is a simple weather application built using the Flet framework. The application fetches and displays the current weather of a city entered by the user.

Features
Displays the current temperature of the entered city.
Option to toggle between dark and light themes.
Installation
Clone the repository:

sh
Копировать код
git clone https://github.com/yourusername/weather-app.git
cd weather-app
Install the required packages:

sh
Копировать код
pip install flet requests
Usage
Run the application:

sh
Копировать код
python app.py
Enter the name of the city in the input field and click the "Информация" button to fetch and display the current weather.

Code
Importing Modules
The application imports the following modules:

python
Копировать код
import flet as ft
import requests
flet: A framework for building interactive web, desktop, and mobile apps using Python.
requests: A simple HTTP library for Python to make API calls.
Main Function
The main function defines the core logic and UI elements of the application.

python
Копировать код
def main(page: ft.Page):
    ...
Page Configuration
The page is configured with the following properties:

python
Копировать код
    page.adaptive = True
    page.title = 'Погода'
    page.theme_mode = 'dark'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
adaptive: Makes the UI adaptive to different screen sizes.
title: Sets the title of the application window.
theme_mode: Sets the initial theme mode to dark.
window_width and window_height: Define the dimensions of the application window.
window_resizable: Prevents the window from being resizable.
UI Elements
The application contains the following UI elements:

user_data: A TextField for the user to enter the city name.
weather_data: A Text widget to display the current temperature.
name_data: A Text widget to display the city name.
python
Копировать код
    user_data = ft.TextField(label="Введите город", width=200)
    weather_data = ft.Text('')
    name_data = ft.Text('')
Fetching Weather Data
The get_info function fetches weather data from the OpenWeatherMap API and updates the UI elements.

python
Копировать код
    def get_info(e):
        if len(user_data.value) < 2:
            return

        API = 'your_openweathermap_api_key'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        name_t = res['name']

        weather_data.value = 'ПОГОДА СЕЙЧАС: ' + str(temp) + ' °C'
        name_data.value = 'Город: ' + str(name_t)
        
        page.update()
Checks if the entered city name is at least 2 characters long.
Constructs the API URL using the entered city name and API key.
Fetches the weather data and extracts the temperature and city name.
Updates the weather_data and name_data elements with the fetched information.
Calls page.update() to refresh the UI.
Changing Theme
The change_theme function toggles between light and dark themes.

python
Копировать код
    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()
Adding UI Elements to the Page
The following elements are added to the page layout:

python
Копировать код
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Изменить тему')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='Информация', on_click=get_info)],
               alignment=ft.MainAxisAlignment.CENTER)
    )
A row containing an icon button to change the theme and a text label.
A row to display the current weather data.
A row for the city input field.
A row to display the city name.
A row containing a button to fetch the weather information.
Running the Application
Finally, the application is run using the ft.app function.

python
Копировать код
ft.app(target=main)
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.
- **Design**:
![](https://github.com/aaalexey05/--------/blob/main/file/image3.png)  


## HTML and CSS Project

### Project: HTML and CSS Redesign
**Description**: This project showcases a redesign of a webpage using HTML and CSS. It compares the original design with the new design created in this project.

**Features**:
- Responsive web design
- Improved layout and typography
- Enhanced user experience

**Before and After Images**:
- **Original Design**:
![](https://github.com/aaalexey05/--------/blob/main/file/image2.png)    

- **New Design**:
![](https://github.com/aaalexey05/--------/blob/main/file/image1.png)    


---



Happy coding! 🚀
