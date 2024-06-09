import flet as ft
import random
import os
import json

def main(page: ft.Page):

    page.adaptive = True

    page.title = "Генератор паролей"
    page.theme_mode = 'dark'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    user_length = (ft.TextField(label='Длина пароля:', width=150))

    user_password_data = ft.Text('')

    def generation_password(e):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        # user_number = int(input("Введите количество паролей:"))
        # user_length = int(input('Длина паролей?'))
        password = ''
        for i in range(int(user_length.value)):
            password += random.choice(chars)
            user_password_data.value = f"Пароль: " + str(password)

        # Обновление JSON файла
        password_file = 'password.json'
        if os.path.exists(password_file):
            with open(password_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
        else:
            data = []
            
        data.append(password)
        
        with open(password_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        page.update()
        
        
    page.add(
        ft.Row([user_length], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='сгенерировать пароль!', on_click=generation_password)],
               alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_password_data], alignment=ft.MainAxisAlignment.CENTER),

    )


ft.app(target=main)
