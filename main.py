
HOME_DIR = 'FPS_files/home'
WD = HOME_DIR

def help():
    print('Commands:')
    print('  make \{filename\} - Make a new file')
    print('  edit \{filename\} - Edit a file')
    print('  remove \{filename\} - Remove a file from the system')
    print('  list - List all files in the system')
    print('  help - Display this message')
    print('  quit - Exit the program')
    print('  cd \{option\} - Change the working directory (not functional)')


input = ''
while input != 'quit':
    print('Welcome to your File Provenance System!')
    print('Type "quit" to exit the program or "help" for a list of commands.')
    input = input(f'{WD} % ')
    input_words = input.split(' ')
    if input_words[0] == 'help':
        help()
    elif input_words[0] == 'make':
        filename = input_words[1]
        print(f'{filename} has been added to the system.')
    elif input_words[0] == 'edit':
        print('Editing a file...')
    elif input_words[0] == 'remove':
        print('Removing a file...')
    elif input_words[0] == 'list':
        print('Listing all files...')
    elif input_words[0] == 'quit':
        print('Exiting the program...')
    else:
        print('Invalid command. Type "help" for a list of commands.')
