"""
Menu options:
:m - menu
:q - quit
:s - start and stop initiave
:e - stop initiave
:r - Remove someone from initiative

"""


def print_full_initiative(dict, dict_keys):
    for key in dict_keys:
        print(f'{key}: {", ".join(dict[key])}')



def print_current_initiative(dict, dict_keys, current):
    print('\nCurrent initiative ------> *', ", ".join(dict[dict_keys[current]]), '*')

    if current == len(dict_keys) - 1:
        current = 0
    else: 
        current += 1
    print('Next -> ', ", ".join(dict[dict_keys[current]]))
    return current

def main():
    print('Please input the initiave and the name of the creatures that you want to track. Input -m to see other commands, and :q to quit.')
    user_input = ''
    initDict = {
        1: ['Eliel', 'Tanja'],
        2: ['Malla', 'Alina'],
        20: ['Elisa', 'Goblin'],
        15: ['Goblin1', 'Goblin2']
    }
    initiativeBool = False
    currentInit = 0
    while user_input != ':q':
        user_input = input('Input here: ')
        if user_input:
            if user_input[0] == ':':
                if user_input == ':s':
                    if initDict:
                        initiativeBool = True
                        dict_keys = list(initDict.keys())
                        dict_keys.sort(reverse=True)

                        print('\nFull initiative: ')
                        print_full_initiative(initDict, dict_keys)
                        print('---------------------------------')

                        currentInit = print_current_initiative(initDict, dict_keys, currentInit)

                    else: 
                        print("You don't have anyone in the initiative, please add someone to it first.")

                elif user_input == ':e':
                    initiativeBool = False
                elif user_input == ':r':
                    print('Do you want to remove a whole initiative or a specific person?')
                    user_remove = input('I for whole initiative, p for person: ')
                    if user_remove.lower() == 'i':
                        remInit = int(input('Which initiative you want to remove: '))
                        if remInit in initDict:
                            initDict.pop(remInit)
                        else:
                            print('Not a valid Initiative.')
                    elif user_remove.lower() == 'p':
                        remInit = int(input('Which initiative you want to modify: '))
                        if remInit in initDict:
                            remPerson = input('Which person you want to remove: ')
                        else:
                            print('Not a valid Initiative.')
                                

                elif user_input == ':m':
                    print("""
Menu options:
:m - menu
:q - quit
:s - start initiave
:e - stop initiave
:r - Remove someone from initiative
""")
                else:
                    return
            else:
                initiative, *names = user_input.split(' ')
                int_init = int(initiative)
                if int_init  in initDict:
                    initDict[int_init].extend(names)
                else:
                    initDict[int_init] = names
                print(initDict)
        elif initiativeBool == True:
                currentInit = print_current_initiative(initDict, dict_keys, currentInit)

    print('Thanks for using the initiative tracker!')



if __name__ == '__main__':
    main()