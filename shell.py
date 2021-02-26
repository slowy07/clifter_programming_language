import basic


print(basic.show_information)
while True:
    text = input(f'{basic.shell_running[0]}')
    result, error = basic.run(f'{basic.shell_running[1]}', text)

    if error: print(error.as_string())
    elif result: print(result)