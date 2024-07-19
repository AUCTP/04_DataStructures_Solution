'''
Modify the code to build a program that allows a user to chose between different options. 
Option 1 should show all the available video games in the list. 
Option 2 should allow the user to enter the name of a video game and add it to the list if it is not already there. 
Option 3 should allow the user to enter the index of a game and delete it
Option 4 should stop the program
'''

def getChoice():
    '''
    Show the different options to the user and return the user selection
    '''
    print('\n')
    print(30*'-')
    print('1. Show games')
    print('2. Add game')
    print('3. Delete game')
    print('4. Stop program')
    print(30*'-')
    choice = int(input())
    print('\n')
    return choice


def printGames(games):
    '''
    Show the available games in the list
    '''
    print("Available games:")
    for i in range(len(games)):
        print(f'{i}: {games[i]}')


def addGame(games):
    '''
    Add a new game to the list and return the new list of games
    '''
    game = input('Name of the game: ')
    if game in games:
        print('You already have this game.')
    else:
        games.append(game)
        print('Success!')
    return games


def deleteGame(games):
    '''
    Delete a game from the list
    '''
    index = int(input('Index of game to delete: '))
    game = games.pop(index)
    print(f'Successfully removed {game} from your games.')
    return games



videoGames = ["Mario", "Sonic", "Joust", "Zelda"]

while True:
    choice = getChoice()
    if choice == 1:
        printGames(videoGames)
    elif choice == 2:
        videoGames = addGame(videoGames)
    elif choice == 3:
        videoGames = deleteGame(videoGames)
    elif choice == 4:
        break
    else:
        print('Invalid selection. Try again.')
    print('\n')