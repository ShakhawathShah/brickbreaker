""" A bunch of functions to read game data."""
# Module for any file handling methods


# Stores user name in file
def write_user_file(name):
    userFile = open("userFile.txt", "w")
    userFile.write(name)
    userFile.close()


# reads user name from file
def read_user_file():
    userFile = open("userFile.txt")
    userName = userFile.readline()
    userFile.close()
    return userName


# Reads leaderboard file and returns the list of data
def read_leaderboard_file():
    leaders = []
    with open("leaderboard.txt") as leaderData:
        for line in leaderData:
            leaders.append(line.split())
    leaders = sorted(leaders, key=lambda x: int(x[0]), reverse=True)
    return leaders


# Stores new player info by appending to text file
def write_to_leaderboard_file(userScore):
    leaderFile = open("leaderboard.txt", "a")
    leaderFile.write(userScore + "\n")

    leaderFile.close()


# Writes all saved data to file
def write_to_save_game_file(
    ballData,
    playerData,
    brickData,
    scoreData,
    livesData,
    gameSpeedx,
    gameSpeedy,
    barrierNum,
    playerSpeedx,
):
    gameFile = open("gameFile.txt", "w")
    gameFile.write(ballData + "\n")
    gameFile.write(playerData + "\n")
    gameFile.write(brickData + "\n")
    gameFile.write(str(scoreData) + "\n")
    gameFile.write(str(livesData) + "\n")
    gameFile.write(str(gameSpeedx) + "\n")
    gameFile.write(str(gameSpeedy) + "\n")
    gameFile.write(str(barrierNum) + "\n")
    gameFile.write(str(playerSpeedx) + "\n")

    gameFile.close()


# Reads save data and returns it
def read_save_game_file():
    gameFile = open("gameFile.txt")
    saveData = gameFile.readlines()
    gameFile.close()
    return saveData
