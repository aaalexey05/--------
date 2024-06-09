import flet as ft


def main(page: ft.Page):

    page.adaptive = True

    page.title = 'Расчёт ИМТ'
    page.theme_mode = 'dark'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    user_weight = (ft.TextField(label='Введите массу (КГ)', width=150))
    user_hight = (ft.TextField(label='Введите рост (СМ)', width=150))
    user_gender = (ft.TextField(label='Введите пол (М/Ж)', width=150))

    imt_data = ft.Text('')
    imt_check_data = ft.Text('')
    imt_check_gender = ft.Text('')

    def do_imt(e):  # масса деленная на рост в квадрате
        hight_x2 = ((int(user_hight.value) / 100)
                    * (int(user_hight.value)) / 100)
        imt = (int(user_weight.value))/(float(hight_x2))
        imt_data.value = 'IMT:  ' + str(round(imt, 2)) + '  кг/м2'

        check_imt(imt)

        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    # def check_gender(user_gender):
    #     if user_gender == 'М' or user_gender == 'м':
    #         imt_check_gender.value = user_gender
    #     else:
    #         imt_check_gender.value == 'Ж' or imt_check_gender.value == 'ж'
    #     print(imt_check_gender)

    #     page.update()

    def check_imt(imt):
        # Обновляем значение текстового элемента
        if imt < 16:
            imt_check_data.value = 'Выраженный дефицит массы тела'
        elif 16 <= imt < 18.5:
            imt_check_data.value = "Недостаточная (дефицит) массы тела"
        elif 18.5 <= imt < 25:
            imt_check_data.value = 'Норма'
        elif 25 <= imt < 30:
            imt_check_data.value = 'Избыточная масса тела (предожирение)'
        elif 30 <= imt < 35:
            imt_check_data.value = 'Ожирение первой степени'
        elif 35 <= imt < 50:
            imt_check_data.value = 'Ожирение второй степени'
        else:
            imt_check_data.value = 'Ожирение третьей степени (морбидное)'

        # print(imt_check_data)

        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.WB_SUNNY, on_click=change_theme),
                ft.Text("Изменить тему")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_gender], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([user_hight], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([user_weight], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([imt_data], alignment=ft.MainAxisAlignment.CENTER),
        # Добавляем текстовый элемент в интерфейс
        ft.Row([imt_check_data], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([ft.ElevatedButton(text='РАССЧИТАТЬ!', on_click=do_imt)],
               alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
