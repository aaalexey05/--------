import flet as ft


async def main(page: ft.Page) -> None:
    page.title = "Mandarin Clicker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#411221"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {"FulboaArgenta": "FulboArgenta.ttf"}

    async def score_up(event: ft.ContainerTapEvent) -> None:
        pass

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="2.lpg",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width-100,
        bar_height=30,
        color='#FF8B1F',
        bgcolor='#BF6524'
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius= ft.BorderRadius(10, 10, 10, 10)
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)