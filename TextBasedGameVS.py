# Carleigh Young

# all ascii art courtesy of https://ascii.co.uk/art/school

import time

player_name = ''
player_major = ''
current_room = 'Admissions Office'
inventory = []
directions = ['north', 'east', 'south', 'west']

def orientation():
    print('                      .')
    print('                     /_\ ')
    print('                     |Ω| ')
    print("               .-----' '-----.")
    print('              /_____[SNHU]____\ ')
    print('               | [] .-.-. [] |')
    print('            ...|____|_|_|____|...')
    print('\nCongratulations! You have been accepted to SNHU!\n')
    time.sleep(3)
    print('Now you must get all set up and complete the requirements needed to get your degree!')
    print('You will need a few things to prepare yourself for the capstone to be able to graduate.')
    print('To help get your journey started, your Admissions Advisor will give you your Student ID Card.')
    print('\nYou will also need to get the following:')
    print(' - Tuition from the Financial Aid')
    print(' - Gen Eds from the Classroom')
    print(' - Free Electives from the Library')
    print(' - Major from the Academic Advising Office')
    print(' - A Snack for Later from the Cafeteria')
    print(' - Major Reqs from the Computer Lab (you will need your Major before heading to the Computer Lab though!)')
    print('\nOnce you’ve got those items you can head to your desk to work on the Capstone that is needed to graduate.')
    print('If you don’t have all the items in your student file you will fail the  Capstone and not be able to graduate!')
    print('If your Capstone is successfully completed you will be able to head down to the Auditorium for Graduation!')
    time.sleep(3)
    print('******************************')
    print('Welcome to the Admissions Office!\n')
    print('\nYour Admissions Advisor asks for your name to check your name off for Orientation.')
    print('------------------------------')
    print('Input Player Name - this can not be more than 64 characters')

    name_confirm()

    print('------------------------------')
    print(f'It’s great to have you here at SNHU {player_name}!')
    print('Your Admissions Advisor hands you a brochure to help you along your way.')
    print('They tell you to head South to go to the Financial Aid office to get your tuition taken care of.')
    print('They hold out your Student ID Card. You will need to add this item to your inventory to move forward.')
    print('To add this item to your inventory type "Get Student ID Card"')
    print('------------------------------')

    command = lower_command()

    # tutorial section - add item, opening brochure and moving to new room
    while command != 'get student id card':
        print('Please type "Get Student ID Card" to pick up the item and continue play.')
        command = lower_command()

    print('You have added your Student ID Card to your inventory.')
    inventory.append('Student ID Card')
    show_inventory()

    print('------------------------------')
    print('Now that you have your Student ID Card you need to head to Financial Aid.')
    print('Open your brochure to see how to get around campus. To open your brochure type "open brochure".')
    command = lower_command()

    while command.lower() != 'open brochure':
        print('Please type open brochure to see game instructions and continue play.')
        command = lower_command()

    show_brochure()

    time.sleep(3)
    print('Great job! Now you can head to the Financial Aid Office to get your tuition taken care of!')
    print('You will not be able to return to the Admissions Office once you leave this room.')
    print('To move to a room type "go" and the direction you want to go. Financial aid is to the SOUTH of Admissions so type "Go South"')

def lower_command():
    command = input()
    command = command.lower()
    return command

def name_confirm():
    global player_name
    player_name = input()
    while len(player_name) > 64:
        print('Your Player Name is too long. Please input a player name of up to 64 characters.')
        player_name = input()
    while player_name == '' or player_name == ' ':
        print('You must input at least put some range of characters for your Name. Please input a player name of up to 64 characters.')
        player_name = input()

    print(f'Your Advisor wants to confirm your name. Is {player_name} correct? You will not be able to change it after this point. Please type Yes or No.')

    name_verify = input()

    while name_verify.lower() != 'yes' and name_verify.lower() != 'no':
        print('that is not a valid response')
        name_verify = input()
    while name_verify.lower() == 'no':
        print('Please input a player name of up to 64 characters.')
        player_name = input()
        print(f'Your Advisor wants to confirm that your name. Is {player_name} correct? You will not be able to change it after this point. Please type Yes or No.')
        name_verify = input()

# commands that can be accessed at almost any time - Exit, Inventory, Help

def finish_game():
    print(f'Thank you for playing {player_name}!')
    time.sleep(3)
    print('Game created by Carleigh Young')
    time.sleep(120)
    quit()


def show_inventory():
    print('------------------------------')
    if len(inventory) == 0:
        print('You have not added anything to your student file yet')
    else:
        print('Your Student File contains the following:')
        inventory_cap = [item.upper() for item in inventory]
        print(inventory_cap)
        if len(inventory_cap) == 7:
            print('You have all the items needed to be able to pass your Capstone project!')
        else:
            print('You are missing some items to be able to pass your Capstone project.')
    if current_room != 'Admissions Office' and (current_room != 'Academic Advising Office' and player_major == ''):
        print('What would you like to do now?')

def show_brochure():
    print('******************************')
    print('Object of the Game:')
    print('To complete your student file by picking up the below items in the appropriate rooms then heading to the Desk to complete your capstone and graduate from SNHU')
    print('     Admissions Office - Student ID Card || Financial Aid - Tuition')
    print('     Cafeteria         - Snack for Later || Classroom     - Gen Eds')
    print('     Computer Lab      - Major Reqs      || Library       - Free Electives')
    print('     Academic Advising - Major')
    print('If you try to go to the desk without any of the items above you will fail your capstone lose the game')
    print('------------------------------')
    print('To be able to move between rooms:')
    print('     Each room you enter will have a list of rooms you can enter designated by a cardinal direction')
    print('     To leave the room you simply have to type the word "go" and the cardinal direction you want to go')
    print('     For Example To leave Admissions you simply have to type "Go South" to go to Financial Aid')
    print('     To enter the Computer Lab you must have the Major item from Academic Advising')
    print('     You will not be able to return to the Admissions Office after leaving there')
    print('------------------------------')
    print('To be able to pick up items:')
    print('     Most rooms you enter will have an item that you can pick up')
    print('     Rooms with an item to get will say "The following item is available" and the item name whenever you enter a room')
    print('     To pick up the item type "get" and then the name of the item')
    print('     For Example To pick up the Student ID Card in Admissions you had to type "get Student ID Card"')
    print('------------------------------')
    print('Other Things to Note:')
    print('     You can type "view student file" to view the items that you have already picked up')
    print('     You can type "exit" to exit the game at any time')
    print('     You can type "open brochure" or "help" at any time to view game objectives and instructions')
    print('     You can type "where am I?" to see room location and directions')
    print('     Input commands are not Case Sensitive')
    print('******************************')

    if current_room != 'Admissions Office' or (current_room != 'Academic Advising Office' and player_major != ''):
        print('What would you like to do now?')

    # Academic Advising room specific functions

def advising_major(room):
    print('------------------------------')
    print('Welcome to the Academic Advising Office!')
    print('You will get to declare your Major here!')

    major_declare()

    print(f'The Academic Advisor says that choosing {player_major} as your Major is a great choice and knows that as  long as you accomplish the tasks needed you will be successful.')
    print('They go to their computer, type up the documentation needed for you and let you know that you can get the  Major item from the printer now.')
    room_info(room)

def major_declare():
    global player_major
    print('Your Academic Advisor asks you what you would like to Major in.')
    print('If you would like to view a list of programs available at SNHU you can go to this site:')
    print('https://www.snhu.edu/program-finder')
    print('Please type out your chosen Major (limit of up to 64 characters)')

    player_major = input()

    while len(player_major) > 64:
        print('Your chosen Major is too long. Please declare a Major of up to 64 characters')
        player_major = input()

    while player_major == '' or player_major == ' ':
        print('''You must input at least put some range of characters for your Major. Please declare a Major of up to 
        64 characters''')
        player_major = input()

    while player_major.lower() == 'help' or player_major.lower() == 'open brochure':
        show_brochure()
        print('Please type out your chosen Major (limit of up to 64 characters)')
        player_major = input()

    while player_major.lower() == 'view student file':
        show_inventory()
        print('Please type out your chosen Major (limit of up to 64 characters)')
        player_major = input()

    while player_major.lower() == 'where am i?':
        print('You need to finish declaring your major first.')
        player_major = input()

    if player_major.lower() == 'exit':
        finish_game()

    print(f'Your Advisor wants to confirm that you are wanting to declare {player_major} as your Major of choice. You will not be able to change it after this point. Please type Yes or No.')

    major_confirm = input()

    while major_confirm.lower() != 'yes' and major_confirm.lower() != 'no':
        print('that is not a valid response')
        major_confirm = input()
    while major_confirm.lower() == 'no':
        major_declare()
        print(f'Your Advisor wants to confirm that you are wanting to declare {player_major} as your Major of choice. You will not be able to change it once you pick up your Major. Please type Yes or No.')
        major_confirm = input()


# generic room function
def room_info(room):
    print('------------------------------')
    print(room['text'])
    if 'item' in room:
        print(room['item text'])
        print('The following item is available:')
        item = room['item']
        print(f'Item: {item.capitalize()}')
    else:
        print(room['no item'])
    print('This is where you can go from here:')
    for direction, movement in room.items():
        if direction in directions:
            print(f'{direction.capitalize()} - {movement}')
    print('What do you want to do now?')


# all ascii art courtesy of https://ascii.co.uk/art/school
def desk_art():
    print('******************************************************************')
    print("__ _____ ____ _____ ______ _______ _____ ______ ______ ______ ___")
    print("__]_____]____]_____]______]_______]_____]______]______]______]___]")
    print("             _                       _______  |||_||__|_||__||_|||")
    print("  _                           _     |   *  3| |||-|| =|-||==||+|||")
    print("  ____________       _              |       | |||_||__|_||__||_|||")
    print("|`.   --__     `.        _______    |       | ||================||")
    print("|  `._____________`.  .'|.-----.|   _ ======| ||| | -|&|^^|!!|-|||")
    print("|   | .-----------.| |  ||     ||  (o))   _ | ||| |**|=|+-|##|=|||")
    print("|   | |  .-------.|| |  ||     ||  /||   / \`._|  .-.|_|__|__|_|||")
    print("|   | |  |       |||_`..|'_____'| //||___\_/.'\| (( ))==========||")
    print("|   | |`.|  ==== ||| | `---------(o)||         \  /-'-=|+|.-|-'|||")
    print("|`. | |`.|_______|||/|______________||__.--._ (o)/|=|;:|-|&&|&&|||")
    print("|  `|_|===========||_|                 (____)-.'(o)_|__|_|__|__|||")
    print("|   | |  .-------.||                           `._\=============||")
    print("|   | |  |       |||                             `.     |       ||")
    print("|   | |`.|  ==== |||`._____________________________`.  o|o      ||")
    print("|`. | |`.|_______||| |._.----------------.__.-------.|__|_______||")
    print("|  `|_|===========|| || '----------------'  | .---. ||  __")
    print("|   | |  .-------.|| ||               |     |_______||.'\.'.")
    print("|   | |  |       ||| || ______________|     | .---. ||'.__.'")
    print("|   | |`.|  ==== ||| ||                `.   |_______|||  _ |")
    print(" `. | |`.|_______||| ||                  `. | .---. |||_  ||")
    print("   `|_|========LGB||`||                    `|_______|||____|")
    print('******************************************************************')


def graduation():
    print('  ,-"-.')
    print(",'  .----.      _________")
    print("`.     ,' )    (@)__))___)")
    print(" |`-.-'| #          \\")
    print(" `-----'               ^")


def main():
    rooms = {
        'Admissions Office': {'south': 'Financial Aid', 'text': 'You are in the Admissions Office', 'no item': 'You already have your Student ID Card'},
        'Financial Aid': {'south': 'Classroom', 'item': 'tuition', 'text': 'You are in the Financial Aid Office.', 'item text': 'There are several staffed desks with individuals that can handle tuition.', 'no item': 'Your Tuition has already been handled with a staff member.'},
        'Classroom': {'north': 'Financial Aid', 'east': 'Academic Advising Office', 'south': 'Cafeteria', 'west': 'Library', 'item': 'gen eds', 'text': 'You are in the Classroom.', 'item text': 'There are several professors here that will help you with your General Education Requirements.', 'no item': 'You have already completed your Gen Eds and do not need to get them again.'},
        'Academic Advising Office': {'north': 'Classroom', 'south': 'Computer Lab', 'west': 'Cafeteria', 'item': 'major', 'text': 'You are in the Academic Advising Office.', 'item text': 'You have already chosen your Major and you can get the Major item from the printer', 'no item': 'You have already have picked up your Major from the printer.'},
        'Cafeteria': {'north': 'Classroom', 'east': 'Academic Advising Office', 'south': 'Computer Lab', 'west': 'Library', 'item': 'snack for later', 'text': 'You are in the Cafeteria', 'item text': 'The Cafeteria is quite busy and there are several lines that hold a variety of snacks.', 'no item': 'The Cafeteria Service has ended. Fortunately, you already have your snack for later.'},
        'Library': {'north': 'Classroom', 'east': 'Cafeteria', 'south': 'Desk', 'item': 'free electives', 'text': 'You are in the library', 'item text': 'There are may types of books you can read while at the library for your free electives', 'no item': 'You have already read the books needed to complete your free electives'},
        'Computer Lab': {'north': 'Cafeteria', 'east': 'Academic Advising Office', 'south': 'Desk', 'item': 'major reqs', 'text': 'You are in the Computer Lab', 'item text': 'While you are here you can sit down at one of the computers to get your Major Requirements.', 'no item': 'You have already completed your Major Reqs and do not need to redo them'},
        'Desk': {'north': 'Computer Lab', 'south': 'Auditorium'},
        'Auditorium': {'north': 'Desk'}
    }

    global current_room
    current_room = 'Admissions Office'
    capstone = ''
    playing = 'yes'

    orientation()

    command = lower_command()

    # command action responses - non directional commands
    while playing.lower() == 'yes':
        while command.lower() == '':
            print('That is not a valid command. Please try again. Type "help" if you need it.')
            command = lower_command()
        if command.lower() == 'view student file':
            show_inventory()
            command = lower_command()
            print('What do you want to do now?')
        elif command.lower() == 'open brochure' or command.lower() == 'help':
            show_brochure()
            command = lower_command()
        elif command.lower() == 'where am i?':
            room_info(rooms[current_room])
            command = lower_command()
        elif command.lower() == 'exit':
            finish_game()
        elif 'item' in rooms[current_room] and command.lower() == 'get ' + rooms[current_room]['item']:
            print('------------------------------')
            print('You have added {} to your Student File'.format(rooms[current_room]['item']))
            inventory.append(rooms[current_room]['item'])
            del rooms[current_room]['item']
            print('What do you want to do now?')
            command = lower_command()
        elif command.lower().split()[0] == 'get':
            item = command.lower()[4:]
            if item in inventory:
                print('You already have that item')
                print('What do you want to do now?')
                command = lower_command()
            else:
                print('That is not a valid command. Please try again. Type "help" if you need it.')
                command = lower_command()
        # directional commands
        elif (command.lower().split()[0] == 'go') and (command.lower().split()[1] in directions) and (
                len(command.lower().split()) == 2):
            if command.lower().split()[1] in rooms[current_room]:
                current_room = rooms[current_room][command.lower().split()[1]]
                # specific room interactions
                if current_room == 'Computer Lab' and 'major' not in inventory:
                    current_room = prior_room
                    print('------------------------------')
                    print('You need your Major before you can go to the Computer Lab. Please go to Academic Advising  to get that.')
                    room_info(rooms[current_room])
                    command = lower_command()
                elif current_room == 'Desk':
                    if len(inventory) == 7 and capstone != 'completed':
                        desk_art()
                        print('You spend many hours at your desk putting together your capstone project and go to submit it for review.')
                        print('Because you were prepared and met all the requirements you passed!')
                        print('You now meet all the requirements to graduate! You can head South to the Auditorium to attend your Graduation Ceremony.')
                        capstone = 'completed'
                        command = lower_command()
                    elif len(inventory) == 7 and capstone == 'completed':
                        print('You have already completed your Capstone project. You can head South to the Auditorium to attend your Graduation Ceremony.')
                        command = lower_command()
                    else:
                        desk_art()
                        print('You spend a few hours at your desk putting together a capstone project and go to submit it for review.')
                        print('Since you were not prepared and didn’t have the necessary items, you failed your capstone!')
                        print('You are not able to graduate and must re-enroll to try again.\nGame Over.')
                        finish_game()
                elif current_room == 'Auditorium':
                    print('------------------------------')
                    print(f'Congratulations! You walk across the stage to accept your diploma from the Dean and have now graduated from SNHU with your degree in {player_major}!')
                    graduation()
                    time.sleep(3)
                    finish_game()
                elif current_room == 'Academic Advising Office':
                    if player_major == '':
                        advising_major(rooms[current_room])
                        prior_room = 'Academic Advising Office'
                        command = lower_command()
                    else:
                        room_info(rooms[current_room])
                        prior_room = 'Academic Advising Office'
                        command = lower_command()
                # regular room interaction
                else:
                    room_info(rooms[current_room])
                    prior_room = current_room
                    command = lower_command()
            # invalid direction
            else:
                print('You can’t go that way. Please try again. Type "help" if you need it.')
                command = lower_command()
            # invalid command
        else:
            print('That is not a valid command. Please try again. Type "help" if you need it.')
            command = lower_command()


if __name__ == '__main__':
    main()
