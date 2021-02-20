def input_select(selection):

    while True:
        for i, item in enumerate(selection, start=1):
            try:
                print(str(i), '-', item.name)
            except AttributeError:
                print(str(i), '-', item)

        try:
            option = int(input('Select your option:'))
        except:
            print('Not an integer value')
            continue

        if option < 1 or option > len(selection):
            print('Unavailable option')
            continue
        else:
            return option
            break
