import flet as ft

def main(page: ft.Page):

    page.adaptive = True

    page.title = 'Расчёт ИМТ'
    page.theme_mode = 'dark'
    page.window_width = 400
    page.window_height = 500
    page.window_resizable = False

    user_weight = ft.TextField(label='Введите массу (КГ)', width=150)
    user_height = ft.TextField(label='Введите рост (СМ)', width=150)
    user_gender = ft.Dropdown(
        label='Введите пол',
        width=150,
        options=[
            ft.dropdown.Option('Мужчина'),
            ft.dropdown.Option('Женщина')
        ]
    )
    user_age = ft.TextField(label='Введите возраст', width=150)

    imt_data = ft.Text('')
    imt_check_data = ft.Text('')
    imt_check_gender = ft.Text('')

    def do_imt(e):
        height_x2 = (int(user_height.value) / 100) ** 2
        imt = int(user_weight.value) / height_x2
        imt_data.value = 'IMT:  ' + str(round(imt, 2)) + '  кг/м2'

        check_imt(imt, user_gender.value.lower(), int(user_age.value))

        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    def check_imt(imt, gender, age):
        if gender not in ['мужчина', 'женщина']:
            imt_check_gender.value = 'Ошибка: некорректный пол'
            page.update()
            return

        if age < 19:
            imt_check_data.value = 'Ошибка: возраст должен быть 19 или старше'
            page.update()
            return

        # Интерпретация ИМТ
        if imt < 16:
            imt_check_data.value = 'Выраженный дефицит массы тела'
        elif 16 <= imt < 18.5:
            imt_check_data.value = "Недостаточная (дефицит) масса тела"
        elif 18.5 <= imt < 25:
            imt_check_data.value = 'Норма массы тела'
        elif 25 <= imt < 30:
            imt_check_data.value = 'Избыточная масса тела (предожирение)'
        elif 30 <= imt < 35:
            imt_check_data.value = 'Ожирение первой степени'
        elif 35 <= imt < 40:
            imt_check_data.value = 'Ожирение второй степени'
        else:
            imt_check_data.value = 'Ожирение третьей степени (морбидное)'

        # Дополнительно: риск для здоровья
        if imt < 18:
            health_risk = 'Низкий'
        elif 18 <= imt < 25:
            health_risk = 'Обычный'
        elif 25 <= imt < 30:
            health_risk = 'Повышенный'
        elif 30 <= imt < 35:
            health_risk = 'Высокий'
        elif 35 <= imt < 40:
            health_risk = 'Очень высокий'
        else:
            health_risk = 'Чрезвычайно высокий'

        imt_check_gender.value = f'Риск развития заболеваний: {health_risk}'

        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.WB_SUNNY, on_click=change_theme),
                ft.Text("Изменить тему")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([user_age], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_gender], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_height], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_weight], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([imt_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([imt_check_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([imt_check_gender], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([ft.ElevatedButton(text='РАССЧИТАТЬ!', on_click=do_imt)],
               alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)