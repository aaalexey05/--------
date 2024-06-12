import math
import tkinter as tk
from tkinter import ttk, messagebox, Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from ttkthemes import ThemedStyle
from googletrans import Translator
from concurrent.futures import ThreadPoolExecutor
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import json
from PIL import Image, ImageTk


# Создаем объект для синтеза речи
engine = pyttsx3.init()

# Глобальная переменная для хранения состояния голосового управления
voice_control_enabled = False


def execute_function(function_name):
    # Определяем функцию по её названию и вызываем её
    if function_name == "площадь" or function_name == "square":
        calculate_triangle()
    elif function_name == "случайные" or function_name == "random":
        fill_with_random_values()
    elif function_name == "управление":
        voice_control()
    elif function_name == "тема":
        change_theme()


def process_voice_command(command):
    # Выводим распознанную команду
    print("Вы сказали:", command)

    # Озвучиваем команду
    engine.say(command)
    engine.runAndWait()

    # Проверяем, является ли команда названием функции и вызываем её
    execute_function(command.lower())
# Перед возвратом из функции voice_control обновляем состояние индикатора
    update_voice_indicator()


# Функция для обработки голосового ввода
def voice_control():
    global voice_control_enabled
    voice_control_enabled = not voice_control_enabled

    update_voice_indicator()  # Обновляем индикатор сразу после изменения состояния голосового управления

    if voice_control_enabled:
        print("Голосовое управление включено")
    else:
        print("Голосовое управление выключено")

    # Если голосовое управление включено, начинаем прослушивание
    if voice_control_enabled:
        recognizer = sr.Recognizer()  # Создаем объект recognizer

        try:
            with sr.Microphone() as source:
                print("Скажите команду...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio, language="ru-RU").lower()
            process_voice_command(command)

        except sr.UnknownValueError:
            print("Извините, не могу распознать команду...")
        except sr.RequestError as e:
            print(f"Ошибка запроса к сервису распознавания: {e}")


# Функция для обновления состояния индикатора голосового управления
def update_voice_indicator():
    voice_indicator.config(text="Голосовое управление: ВКЛ" if voice_control_enabled else "Голосовое управление: ВЫКЛ", foreground="green" if voice_control_enabled else "red")


def calculate_triangle():
    try:
        a = float(a_tf.get())
        b = float(b_tf.get())
        c = float(c_tf.get())

        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            triangle_type = determine_triangle_type(a, b, c)
            display_triangle_info(a, b, c, triangle_area, triangle_type)
            draw_triangle(a, b, c)

            # Добавляем результат в историю
            add_to_history({'sides': (a, b, c), 'area': triangle_area})
        else:
            messagebox.showerror("Ошибка", "Треугольник с такими сторонами не существует!")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения для сторон треугольника!")


def calculate_perimeter(a, b, c):
    return a + b + c


def calculate_height(a, b, c):
    s = calculate_perimeter(a, b, c) / 2
    triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    height = (2 * triangle_area) / a
    return height


def determine_triangle_type(a, b, c):
    if a == b == c:
        return "Равносторонний"
    elif a == b or a == c or b == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"


def fill_with_random_values():
    try:
        a_tf.delete(0, 'end')
        b_tf.delete(0, 'end')
        c_tf.delete(0, 'end')
        a_tf.insert(0, str(random.uniform(1, 10)))
        b_tf.insert(0, str(random.uniform(1, 10)))
        c_tf.insert(0, str(random.uniform(1, 10)))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при генерации случайных значений: {str(e)}")


def draw_triangle(a, b, c):
    canvas.ax.clear()
    x = [0, a, (a**2 + c**2 - b**2) / (2 * a), 0]
    y = [0, 0, math.sqrt(c**2 - ((a**2 + c**2 - b**2) / (2 * a))**2), 0]
    canvas.ax.plot(x, y, 'r-')
    canvas.ax.text(0, 0, 'A', fontsize=12, ha='right')
    canvas.ax.text(a, 0, 'B', fontsize=12, ha='left')
    canvas.ax.text((a**2 + c**2 - b**2) / (2 * a), math.sqrt(c**2 - ((a**2 + c**2 - b**2) / (2 * a))**2), 'C', fontsize=12, ha='center')
    canvas.draw()


def display_triangle_info(a, b, c, triangle_area, triangle_type):
    info_canvas.delete("all")
    text_x = 20
    text_y = 20

    info_canvas.create_text(text_x, text_y, anchor="nw", text="Triangle Information", font=("Arial", 16, "bold"))
    info_canvas.create_text(text_x, text_y + 40, anchor="nw", text=f'Side "a": {a:.2f} см', font=("Arial", 12))
    info_canvas.create_text(text_x, text_y + 60, anchor="nw", text=f'Side "b": {b:.2f} см', font=("Arial", 12))
    info_canvas.create_text(text_x, text_y + 80, anchor="nw", text=f'Side "c": {c:.2f} см', font=("Arial", 12))
    info_canvas.create_text(text_x, text_y + 120, anchor="nw", text=f'Площадь(S): {triangle_area:.2f} кв. см', font=("Arial", 12))
    perimeter = calculate_perimeter(a, b, c)
    info_canvas.create_text(text_x, text_y + 140, anchor="nw", text=f'Периметр(P): {perimeter:.2f} см', font=("Arial", 12))
    info_canvas.create_text(text_x, text_y + 180, anchor="nw", text=f'Тип(Type): {triangle_type}', font=("Arial", 12))
    height = calculate_height(a, b, c)
    info_canvas.create_text(text_x, text_y + 200, anchor="nw", text=f'Высота(h): {height:.2f} см', font=("Arial", 12))

    # Теперь добавим эту информацию в историю
    add_to_history((a, b, c), triangle_area)


def toggle_info_canvas():
    if info_canvas.winfo_ismapped():
        info_canvas.pack_forget()
        function_menu.entryconfigure("Отобразить информацию о треугольнике", label="Показать информацию о треугольнике")
    else:
        info_canvas.pack(side="right", padx=20, pady=20)
        function_menu.entryconfigure("Отобразить информацию о треугольнике", label="Скрыть информацию о треугольнике")


def plot_3d_triangle():
    try:
        a = float(a_tf.get())
        b = float(b_tf.get())
        c = float(c_tf.get())

        # Create a top-level window
        plot_window = tk.Toplevel(window)
        plot_window.title("3D Модель треугольника")

        # Create a figure and subplot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Coordinates of triangle vertices
        x = [0, a, (a ** 2 + c ** 2 - b ** 2) / (2 * a), 0]
        y = [0, 0, calculate_height(a, b, c), 0]
        z = [0, 0, 0, 0]

        # Display triangle vertices and lines
        ax.scatter(x, y, z, color='r', marker='o')  # Vertices
        ax.plot(x, y, z, color='b')  # Connecting lines

        # Vertex labels
        ax.text(0, 0, 0, f'A (0, 0, 0)', fontsize=12, ha='right')
        ax.text(a, 0, 0, f'B ({a:.2f}, 0, 0)', fontsize=12, ha='left')
        ax.text((a ** 2 + c ** 2 - b ** 2) / (2 * a), calculate_height(a, b, c), 0,
                f'C ({(a ** 2 + c ** 2 - b ** 2) / (2 * a):.2f}, {calculate_height(a, b, c):.2f}, 0)',
                fontsize=12, ha='center')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_xlim(0, max(a, (a ** 2 + c ** 2 - b ** 2) / (2 * a)) * 1.1)  # Extend X axis for better visibility
        ax.set_ylim(0, max(0, calculate_height(a, b, c)) * 1.1)  # Extend Y axis for better visibility

        # Display the plot in the top-level window
        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        # Ensure the plot window stays on top
        plot_window.attributes('-topmost', True)

    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовые значения для сторон треугольника!")


def toggle_canvas_visibility():
    if canvas.get_tk_widget().winfo_ismapped():
        canvas.get_tk_widget().pack_forget()
        function_menu.entryconfigure("Показать холст с треугольником", label="Показать холст с треугольником")
    else:
        canvas.get_tk_widget().pack(fill='both', expand=True)
        function_menu.entryconfigure("Показать холст с треугольником", label="Скрыть холст с треугольником")


def clear_entries():
    a_tf.delete(0, 'end')
    b_tf.delete(0, 'end')
    c_tf.delete(0, 'end')


def change_theme():
    current_theme = style.theme_use()
    if current_theme == "clam":
        style.theme_use("equilux")
        canvas.ax.patch.set_facecolor(themed_style.lookup("TFrame", "background"))
        info_canvas.config(bg=themed_style.lookup("TFrame", "background"))
    else:
        style.theme_use("clam")
        canvas.ax.patch.set_facecolor("white")
        info_canvas.config(bg="white")


translator = Translator()
current_language = 'ru'  # Начальный язык по умолчанию
translation_cache = {}  # Кэш для хранения переведенных строк

# Список текстовых строк для перевода
texts_to_translate = [
    "Side 'a' (cm):",
    "Side 'b' (cm):",
    "Side 'c' (cm):",
    'Triangle Area Calculator', 'Калькулятор площади треугольника',
    "Calculate Area",
    "Random Values",
    'Display Triangle Information', 'Show Canvas with Triangle',
    'Display 3D Triangle Model', 'Clear Entries', 'Change Theme',
    'Functions', 'History results'  # Пример добавления новых текстов для перевода
    # Добавьте другие текстовые строки, которые нужно перевести
]

# Список поддерживаемых языков
supported_languages = ['en', 'zh-CN']  # Добавьте другие языки при необходимости


# Функция для перевода текста с кэшированием
def translate_with_cache(text, dest_language):
    cache_key = (text, dest_language)
    if cache_key in translation_cache:
        return translation_cache[cache_key]
    try:
        translated_text = translator.translate(text, dest=dest_language).text
        translation_cache[cache_key] = translated_text
        return translated_text
    except Exception as e:
        print(f"Translation error for '{text}' to '{dest_language}': {e}")
        return text  # Fall back to the original text if translation fails
        translation_cache[cache_key] = translated_text
        return translated_text


# Функция для предварительной загрузки переводов в кэш
def preload_translations():
    with ThreadPoolExecutor() as executor:
        futures = []
        for text in texts_to_translate:
            translated = translate_with_cache(text, 'en')
            print(f"Original: {text} -> Translated: {translated}")
        # Дождитесь завершения всех запросов
        for future in futures:
            future.result()


# Предварительно загрузить переводы при запуске программы
preload_translations()


def translate_text(text, dest_language='en'):
    if (text, dest_language) in translation_cache:
        return translation_cache[(text, dest_language)]
    else:
        translated_text = translator.translate(text, dest=dest_language)
        translation_cache[(text, dest_language)] = translated_text.text
        return translated_text.text


def switch_language(dest_language):
    global current_language
    current_language = dest_language

    translations = {text: translate_with_cache(text, dest_language) for text in texts_to_translate}

    # Обновляем тексты меток пакетно
    a_label["text"] = translations.get("Side 'a' (cm):", a_label["text"])
    b_label["text"] = translations.get("Side 'b' (cm):", b_label["text"])
    c_label["text"] = translations.get("Side 'c' (cm):", c_label["text"])
    calculate_btn["text"] = translations.get("Calculate Area", calculate_btn["text"])
    random_values_btn["text"] = translations.get("Random Values", random_values_btn["text"])

    # Обновляем тексты в меню пакетно
    function_menu_labels = ['Display Triangle Information', 'Show Canvas with Triangle',
                            'Display 3D Triangle Model', 'Clear Entries', 'Change Theme',
                            'Functions', 'History results']

    for i, label_text in enumerate(function_menu_labels):
        function_menu.entryconfigure(i, label=translations.get(label_text, function_menu.entrycget(i, "label")))

    window.title(translations.get('Triangle Area Calculator', window.title()))
# Обновляем название окна
    window.title(translations.get('Калькулятор площади треугольника', window.title()))


# Создаем функцию для переключения языка с блокировкой уже выбранного языка
def switch_language_menu(lang_code):
    def switch():
        if lang_code != current_language:  # Проверяем, не выбран ли уже этот язык
            switch_language(lang_code)
        else:
            messagebox.showinfo("Предупреждение", "Этот язык уже выбран как интерфейсный язык.")
    return switch


language_codes = {'ru': 'Русский', 'en': 'English', 'zh-CN': '中文'}  # Словарь языков и их кодов


def show_about():
    about_window = tk.Toplevel(window)
    about_window.title("О программе")
    about_window.geometry("600x400")
    about_window.configure(bg="#FFFFFF")

    title_label = ttk.Label(about_window, text="О программе", font=("Arial", 24, "bold"), background="#FFFFFF")
    title_label.pack(pady=(20, 10))

    separator = ttk.Separator(about_window, orient="horizontal")
    separator.pack(fill="x", padx=20, pady=(0, 20))

    info_frame = ttk.Frame(about_window, padding=20, style="Info.TFrame", borderwidth=2, relief="groove")
    info_frame.pack(fill='both', expand=True, padx=20)

    author_label = ttk.Label(info_frame, text="Автор:", font=("Arial", 16, "bold"), background="#FFFFFF")
    author_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    author_info = ttk.Label(info_frame, text="Alexey Shilyaev", font=("Arial", 14), background="#FFFFFF")
    author_info.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    year_label = ttk.Label(info_frame, text="Год создания:", font=("Arial", 16, "bold"), background="#FFFFFF")
    year_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    year_info = ttk.Label(info_frame, text="2024", font=("Arial", 14), background="#FFFFFF")
    year_info.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    purpose_label = ttk.Label(info_frame, text="Цель:", font=("Arial", 16, "bold"), background="#FFFFFF")
    purpose_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    purpose_text = "Учебная и научная деятельность"
    purpose_info = ttk.Label(info_frame, text=purpose_text, font=("Arial", 14), background="#FFFFFF", wraplength=500, justify="left")
    purpose_info.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Кнопка закрытия окна
    close_button = ttk.Button(about_window, text="Закрыть", command=about_window.destroy)
    close_button.pack(pady=(0, 20))

    # Стилизация
    style = ttk.Style()
    style.configure("Info.TFrame", background="#FFFFFF")


class HistoryItem:
    def __init__(self, function_name, input_data, result):
        self.function_name = function_name
        self.input_data = input_data
        self.result = result
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp}] Function: {self.function_name}, Input: {self.input_data}, Result: {self.result}"


# Создаем список для хранения истории результатов
results_history = []

# Объявляем глобальные переменные для окна истории
history_window = None
history_text = None
checkbox_vars = []  # Список переменных для флажков (чекбоксов)

# Путь к файлу истории
history_file = "history.json"


# Функция для отображения окна с историей результатов
def show_history():
    global history_window, history_text
    if history_window is None:
        history_window = tk.Toplevel(window)
        history_window.title("История результатов")
        history_window.protocol("WM_DELETE_WINDOW", on_history_window_close)  # Обработчик закрытия окна

        # Создаем текстовый виджет для отображения истории
        history_text = tk.Text(history_window, height=20, width=60)
        history_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Создаем кнопку для удаления выбранных записей
        remove_selected_button = ttk.Button(history_window, text="Удалить выбранное", command=remove_selected)
        remove_selected_button.pack(side="left", padx=5, pady=5)

        # Создаем кнопку для удаления всех записей
        remove_all_button = ttk.Button(history_window, text="Удалить все", command=clear_history)
        remove_all_button.pack(side="left", padx=5, pady=5)

        # Выводим записи истории
        update_history_display()


# Функция для загрузки истории из файла
def load_history_from_file():
    global results_history
    try:
        with open(history_file, "r") as file:
            data = file.read()
            if data:  # Проверяем, что файл не пустой
                results_history = json.loads(data)
            else:
                results_history = []
    except (FileNotFoundError, json.JSONDecodeError):
        results_history = []


# Функция для сохранения истории в файл
def save_history_to_file():
    with open(history_file, "w") as file:
        json.dump(results_history, file)


# Добавляем функцию сохранения и загрузки истории при запуске программы
load_history_from_file()


# Функция для обновления отображения истории результатов и сохранения в файл
def update_history_display():
    global checkbox_vars
    history_text.delete('1.0', tk.END)  # Очищаем текстовый виджет перед обновлением
    checkbox_vars.clear()  # Очищаем список переменных для флажков перед обновлением

    for index, triangle_data in enumerate(results_history, start=1):
        sides = [round(side, 2) for side in triangle_data['sides']]
        area = round(triangle_data['area'], 2)

        history_text.insert(tk.END, f"Запись {index}:\n")
        history_text.insert(tk.END, f"Стороны треугольника: a = {sides[0]}, b = {sides[1]}, c = {sides[2]}\n")
        history_text.insert(tk.END, f"Площадь треугольника: {area} кв. см\n\n")

        # Создаем переменную для каждого флажка
        var = tk.BooleanVar(value=False)
        checkbox_vars.append(var)

        # Создаем флажок для текущей записи
        checkbox = ttk.Checkbutton(history_text, variable=var)
        history_text.window_create(tk.END, window=checkbox)
        history_text.insert(tk.END, '\n')

    # Сохраняем историю в файл после обновления
    save_history_to_file()


# Функция для удаления выбранных записей
def remove_selected():
    global results_history
    updated_history = [triangle_data for triangle_data, var in zip(results_history, checkbox_vars) if not var.get()]
    results_history = updated_history
    if history_window is not None:
        update_history_display()


# Функция для удаления всех записей
def clear_history():
    global results_history
    results_history.clear()
    update_history_display()


# Обработчик закрытия окна истории
def on_history_window_close():
    global history_window
    history_window.destroy()
    history_window = None


# Функция для добавления результатов в историю
def add_to_history(sides, area):
    results_history.append({'sides': sides, 'area': area})
    if history_window is not None:
        update_history_display()


def on_closing():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        window.quit()
        window.destroy()
        plt.close('all')


info_canvas_width = 200
canvas_width = 200

window = tk.Tk()
window.title('Калькулятор площади треугольника')
window.geometry('600x400+100+100')  # Width x Height + XOffset + YOffset
window.resizable(True, True)

style = ttk.Style(window)
style.theme_use("clam")

frame = ttk.Frame(window, padding=20)
frame.pack(fill='both', expand=True, side='left')

a_label = ttk.Label(frame, text='Сторона "a" (см):')
a_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

a_tf = ttk.Entry(frame)
a_tf.grid(row=0, column=1, padx=5, pady=5)

b_label = ttk.Label(frame, text='Сторона "b" (см):')
b_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

b_tf = ttk.Entry(frame)
b_tf.grid(row=1, column=1, padx=5, pady=5)

c_label = ttk.Label(frame, text='Сторона "c" (см):')
c_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

c_tf = ttk.Entry(frame)
c_tf.grid(row=2, column=1, padx=5, pady=5)

calculate_btn = ttk.Button(frame, text='Вычислить площадь', command=calculate_triangle, width=20)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

random_values_btn = ttk.Button(frame, text='Случайные значения', command=fill_with_random_values, width=20)
random_values_btn.grid(row=4, column=0, columnspan=2, pady=10)

info_canvas = tk.Canvas(window, width=info_canvas_width, height=400, bg="white")
info_canvas.pack(side="left", fill="y", padx=20, pady=20)

canvas_frame = ttk.Frame(window, padding=30, width=canvas_width, height=400)
canvas_frame.pack(side="right", fill="both", expand=True)

fig = plt.figure(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.ax = fig.add_subplot(111)
canvas.get_tk_widget().pack(fill='both', expand=True)

menu = tk.Menu(window)
window.config(menu=menu)

function_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Функции", menu=function_menu)

# Создаем меню для выбора языка
language_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Language", menu=language_menu)

for code in language_codes.keys():
    language_menu.add_radiobutton(label=language_codes[code], command=switch_language_menu(code))


info_canvas_visible = tk.BooleanVar()
info_canvas_visible.set(True)


function_menu.add_checkbutton(label="Отображать информацию о треугольнике", variable=info_canvas_visible,
                              command=toggle_info_canvas)

canvas_visible = tk.BooleanVar()
canvas_visible.set(True)  # Set the default visibility to True

function_menu.add_checkbutton(label="Показать холст с треугольником", variable=canvas_visible, command=toggle_canvas_visibility)

# Добавляем функцию в меню
function_menu.add_command(label="Отобразить 3D модель треугольника", command=plot_3d_triangle)

function_menu.add_command(label="Очистить поля", command=clear_entries)

function_menu.add_command(label="Сменить тему", command=change_theme)
themed_style = ThemedStyle()
themed_style.set_theme("clam")

window.protocol("WM_DELETE_WINDOW", on_closing)  # закрытие всех окон, которые открываются параллельно с главным

preload_translations()

# Создаем меню "О программе"
about_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="О программе", menu=about_menu)

# Добавляем функцию в меню "О программе"
about_menu.add_command(label="Информация", command=show_about)

voice_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Голосовое управление", menu=voice_menu)

voice_menu.add_command(label="Голосовое управление", command=voice_control)

# Создаем метку для отображения состояния голосового управления
voice_indicator = ttk.Label(frame, text="Голосовое управление: ВЫКЛ", font=("Arial", 10))
voice_indicator.grid(row=5, column=0, columnspan=2, pady=5)

# Вызываем функцию обновления индикатора после инициализации окна
update_voice_indicator()

# Добавляем функцию в меню для отображения истории результатов
function_menu.add_command(label="История результатов", command=show_history)

window.mainloop()