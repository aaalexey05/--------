import flet as ft
import requests


def main(page: ft.Page):

    page.adaptive = True

    page.title = 'Погода'
    page.theme_mode = 'dark'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    user_data = ft.TextField(label="Введите город", width=200)
    weather_data = ft.Text('')
    name_data = ft.Text('')

    def get_info(e):
        if len(user_data.value) < 2:
            return

        API = '60bae81ae39635b5df3073ffb3dd2f22'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        name_t = res['name']

        weather_data.value = 'ПОГОДА СЕЙЧАС: ' + str(temp) + ' °C'
        name_data.value = 'Город: ' + str(name_t)
        
        
        # print(res)

        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

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
        ft.Row([name_data],  alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([ft.ElevatedButton(text='Информация', on_click=get_info)],
               alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
