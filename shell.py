import basic


print(basic.show_information)
while True:
    text = input(f'{basic.shell_running[0]}')
    
    if text.strip() == "": continue
    result, error = basic.run(f'{basic.shell_running[1]}', text)

    if error: print(error.as_string())
    elif result: 
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))