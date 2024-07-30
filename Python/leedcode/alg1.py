import PySimpleGUI as psg

psg.set_options(font=('Arial Bold', 16))

layout = [
    [psg.Text('Enter a num: '), psg.Input(key='-FIRST-')],
    [psg.Text('Enter a num: '), psg.Input(key='-SECOND-')],
    [psg.Text('Result : '), psg.Text(key='-OUT-')],
    [psg.Button('Add'), psg.Button('Sub'), psg.Button('Multiply'), psg.Button('Divide'), psg.Exit()]
]

window = psg.Window('Calculator', layout, size = (715, 180))

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Add':
        result = int(values['-FIRST-']) + int(values['-SECOND-'])
    if event == 'Sub':
        result = int(values['-FIRST-']) - int(values['-SECOND-'])
    if event == 'Multiply':
        result = int(values['-FIRST-']) * int(values['-SECOND-'])
    if event == 'Divide':
        if values['-SECOND-'] == 0 or values['-FIRST-'] == 0:
            result = 'Делить на 0 нельзя. Ошибка!'
        elif values['-FIRST-'] != 0 and values['-SECOND-'] != 0:
            result = (int(values['-FIRST-']) / int(values['-SECOND-']))
    window['-OUT-'].update(result)
    if event == psg.WINDOW_CLOSE_ATTEMPTED_EVENT and psg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    
window.Close()