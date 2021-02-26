import basic


print(basic.show_information)
while True:
    text = input(f'{basic.shell_running}')
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(result)