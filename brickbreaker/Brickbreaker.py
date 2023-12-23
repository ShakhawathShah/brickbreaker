##########----------B r i c k    B r e a k e r ! ! ! !----------##########

# Screen Resolution 1920 x 720
# Game buttons P to pause, P to continue
# Space to start

# References:

# http://pixelartmaker.com/art/948dfe7d156736e - paused.png, ( Accessed: 25/11/20 )

# http://pixelartmaker.com/art/0d111fb05fe3517 - win.png, ( Accessed: 04/12/20 )

# http://www.seekgif.com/backgrounds/game-over-png.html - game_over.png, ( Accessed: 25/11/20 )



# tkinter imports
from tkinter import Tk, Label, Button, Entry, Canvas, BOTH, PhotoImage, ANCHOR, NW

# Module imports
from leaderboard import configureLeaderboardWindow
from user_module import *

import time, os
from random import randint as rand

# Global variables declared
score_counter = barrier_num = game_speedx = game_speedy = player_speedx = lives = 0
brick_points = 100


# Tkinter window initialsed
def configure_window():
    window.geometry("1280x720")
    window.configure(background="black")
    window.title(
        "##########----------B r i c k    B r e a k e r ! ! ! !----------##########"
    )

    global name_entry, lbl_name
    # Home screen welcome
    lbl_name = Label(
        window,
        text="Welcome, Please enter your name below ",
        font=("Arial Bold", 30),
        background="black",
        fg="blue",
    )
    lbl_name.place(x=250, y=100)

    name_entry = Entry(
        window, text="Easy", font=("Arial Bold", 30), width=25, fg="white", bg="blue"
    )
    name_entry.place(x=350, y=250)
    name_entry.bind("<Return>", welcomeUser)


def welcomeUser(event):

    global user_name, welcome

    user_name = name_entry.get()

    if user_name != "" or user_name == " ":
        window.unbind("<Return>")

        global brick_points

        lbl_name.place_forget()
        name_entry.place_forget()

        # Check for a cheat code entry
        if user_name == "BrickBreaker":
            brick_points = 500
            user_name = read_user_file()

        print(user_name)
        # Saves users name, for leaderboard use
        write_user_file(str(user_name))

        welcome = Label(
            window,
            text="Welcome to back to Brick Breaker, " + user_name,
            font=("Arial Bold", 25),
            background="black",
            fg="blue",
        )
        welcome.pack()
        # All neccessary key binds for game to start
        window.bind("<space>", ball.startGame)
        window.bind("<p>", pause)
        window.bind("<b>", bossKey)
        window.bind("<q>", cheat_code)

        create_buttons()
    else:
        None


# All buttons created
def create_buttons():

    global btn_easy, btn_medium, btn_hard, btn_load, btn_leaderboard, btn_quit

    btn_easy = Button(
        window, text="Easy", font=("Arial Bold", 25), width=7, fg="blue", bg="black"
    )
    # Button runs function when clicked using binds
    btn_easy.bind("<Button-1>", set_game_easy)

    btn_medium = Button(
        window, text="Medium", font=("Arial Bold", 25), width=7, fg="blue", bg="black"
    )
    btn_medium.bind("<Button-1>", set_game_medium)

    btn_hard = Button(
        window, text="Hard", font=("Arial Bold", 25), width=7, fg="blue", bg="black"
    )
    btn_hard.bind("<Button-1>", set_game_hard)
    # Buttons offer variety of options for user
    btn_load = Button(
        window,
        text="Load Game",
        font=("Arial Bold", 25),
        width=22,
        fg="blue",
        bg="black",
    )
    btn_load.bind("<Button-1>", loadGame)

    btn_leaderboard = Button(
        window,
        text="Leaderboard",
        font=("Arial Bold", 25),
        width=22,
        fg="blue",
        bg="black",
    )
    btn_leaderboard.bind("<Button-1>", configureLeaderboardWindow)

    btn_quit = Button(
        window, text="Quit", font=("Arial Bold", 25), width=22, fg="blue", bg="black"
    )
    btn_quit.bind("<Button-1>", quit_game)

    place_buttons()


def remove_buttons():
    # Function to hide buttons when required
    btn_easy.place_forget()
    btn_medium.place_forget()
    btn_hard.place_forget()

    btn_load.place_forget()
    btn_leaderboard.place_forget()
    btn_quit.place_forget()


def place_buttons():
    # Replaces button when required
    btn_easy.place(x=350, y=100)
    btn_medium.place(x=550, y=100)
    btn_hard.place(x=750, y=100)
    btn_load.place(x=400, y=250)
    btn_leaderboard.place(x=400, y=400)
    btn_quit.place(x=400, y=550)


# methods which set variables based on difficulty of game
def set_game_easy(event):
    remove_buttons()

    global game_speedx, game_speedy, lives, barrier_num, player_speedx
    lbl_game_help.place(x=360, y=350)
    # Different values for each difficulty
    game_speedx = 4
    game_speedy = 4
    player_speedx = 4
    lives = 5
    barrier_num = 0
    create_canvas()


def set_game_medium(event):
    remove_buttons()

    global game_speedx, game_speedy, lives, barrier_num, player_speedx
    lbl_game_help.place(x=360, y=350)

    game_speedx = 7
    game_speedy = 7
    player_speedx = 7
    lives = 3
    barrier_num = 1
    # Creates game display
    create_canvas()


def set_game_hard(event):
    remove_buttons()

    global game_speedx, game_speedy, lives, barrier_num, player_speedx
    lbl_game_help.place(x=360, y=350)

    game_speedx = 10
    game_speedy = 10
    player_speedx = 10
    lives = 1
    barrier_num = 3
    create_canvas()


def create_canvas():
    canvas.pack(fill=BOTH)


def pause(event):
    global paused_img
    # Image used for pause screen
    paused_img = canvas.create_image((375, 50), image=img1, anchor=NW)

    global btn_save
    btn_save = Button(
        window,
        text="Save and Quit",
        font=("Arial Bold", 25),
        width=20,
        fg="blue",
        bg="black",
    )

    btn_save.place(x=425, y=300)
    btn_save.bind("<Button-1>", save_game)

    # User help to make game more user friendly
    global lbl_pause_help
    lbl_pause_help = Label(
        canvas,
        text="Press 'P' to continue ",
        font=("Arial Bold", 25),
        background="black",
        fg="blue",
    )
    lbl_pause_help.place(x=475, y=350)

    # Boolean value used to stop game loop
    ball.pause_pressed = True

    # Saves ball location and direction so that user can continue where they left off
    ball.canvas.coords(ball.ball)
    resetX = ball.ball_speedx
    resetY = ball.ball_speedy

    global game_speedx, game_speedy
    game_speedx = resetX
    game_speedy = resetY

    # Key binds to allow P to unpause game
    window.unbind("<p>")
    window.bind("<p>", unpause)


def unpause(event):
    # Removes buttons displayed during pause screen
    btn_save.place_forget()
    lbl_pause_help.place_forget()

    window.unbind("<p>")
    window.bind("<p>", pause)

    # Removes pause image
    canvas.delete(paused_img)
    time.sleep(1)

    ball.pause_pressed = False
    # Calls movement method with updated Bool value
    ball.movement()


# Adds boss screen image to screen
def bossKey(event):
    ball.pause_pressed = True

    global boss_img
    boss_img = canvas.create_image((0, 0), image=img_boss, anchor=NW)
    welcome.pack_forget()

    # Saves ball location and direction so that user can continue where they left off
    ball.canvas.coords(ball.ball)
    resetX = ball.ball_speedx
    resetY = ball.ball_speedy

    global game_speedx, game_speedy
    game_speedx = resetX
    game_speedy = resetY

    window.unbind("<b>")
    window.bind("<b>", unBoss)


def unBoss(event):
    # Removes boss image allowing game to continue
    canvas.delete(boss_img)

    window.unbind("<b>")
    window.bind("<b>", bossKey)

    ball.pause_pressed = False
    ball.movement()


def loadGame(event):
    # Uses method form imported module to read file
    save_data = read_save_game_file()

    # Retrives ball location data
    saved_ball_data = save_data[0].split(",")
    saved_ball_data[-1] = saved_ball_data[-1].strip()
    ball.start_coords = saved_ball_data

    # Retrives player location data
    saved_player_data = save_data[1].split(",")
    saved_player_data[-1] = saved_player_data[-1].strip()
    player.player_start_coords = saved_player_data

    saved_brick_data = save_data[2].split(",")
    saved_brick_data[-1] = saved_brick_data[-1].strip()

    # Moves every brick back to saved location
    for i, j in zip(range(len(brick.bricks)), range(0, len(saved_brick_data), 4)):
        coords = [
            saved_brick_data[j],
            saved_brick_data[j + 1],
            saved_brick_data[j + 2],
            saved_brick_data[j + 3],
        ]
        brick.canvas.coords(brick.bricks[i], coords[0], coords[1], coords[2], coords[3])
        j += 4
        i += 1

    # Sets global values such as score, lives etc
    global score_counter, lives, game_speedx, game_speedy, barrier_num, player_speedx

    score_counter = int(save_data[3])
    lives = int(save_data[4])
    game_speedx = int(save_data[5])
    game_speedy = int(save_data[6])
    barrier_num = int(save_data[7])
    player_speedx = int(save_data[8])

    remove_buttons()
    # Starts game again with saved data
    create_canvas()


def save_game(event):
    # Stores ball data
    save_ball = ball.canvas.coords(ball.ball)
    ball_coords = ""
    for val in save_ball:
        ball_coords = ball_coords + str(val) + " "
    ball_data = ball_coords.replace(" ", ",", 3)

    # Stores player data
    save_player = player.canvas.coords(player.playerID)
    player_coords = ""
    for val in save_player:
        player_coords = player_coords + str(val) + " "
    player_data = player_coords.replace(" ", ",", 3)

    # Stores brick data
    brick_coords = ""
    for i in range(len(brick.bricks)):
        save_brick = brick.canvas.coords(brick.bricks[i])
        for val in save_brick:
            brick_coords = brick_coords + str(val) + " "
        i += 1
    brick_data = brick_coords.replace(" ", ",", 191)

    global score_counter, lives, game_speedx, game_speedy, barrier_num, player_speedx

    # Writes data to file with values as parameters
    write_to_save_game_file(
        ball_data,
        player_data,
        brick_data,
        score_counter,
        lives,
        game_speedx,
        game_speedy,
        barrier_num,
        player_speedx,
    )

    # Exists game
    quit()


def game_over():
    # Game actions for when the user dies
    window.unbind("<space>")
    ball.pause_pressed = True

    # canvas.delete("all")

    # Displays game over image
    ball.img = PhotoImage(file="game_over.png")
    ball.imgGO = ball.canvas.create_image((375, 10), image=ball.img, anchor=NW)
    global score_counter, lives

    # Moves all bricks off screen
    for i in range(len(brick.bricks)):
        canvas.coords(brick.bricks[i], 0, 0, 0, 0)

    canvas.coords(ball.ball, 0, 0, 0, 0)
    canvas.coords(player.playerID, 0, 0, 0, 0)

    global btn_restart
    btn_restart = Button(
        window,
        text="Restart Game",
        font=("Arial Bold", 25),
        width=22,
        fg="blue",
        bg="black",
    )
    # User has option to restart
    btn_restart.place(x=410, y=160)
    btn_restart.bind("<Button-1>", restart_game)

    # Gets users score ready to write to file
    end_score_info = str(score_counter) + " " + user_name
    write_to_leaderboard_file(end_score_info)

    global lbl_score
    lbl_score = Label(
        canvas,
        text=("Your Score: " + str(score_counter)),
        font=("Arial Bold", 40),
        background="black",
        fg="blue",
    )
    lbl_score.place(x=425, y=200)

    # Resets score counter
    score_counter = lives = 0
    ball.update_score(score_counter)

    global lbl_leaderboard
    lbl_leaderboard = Label(
        canvas,
        text="Leaderboard",
        font=("Arial Bold", 35),
        background="black",
        fg="blue",
    )
    lbl_leaderboard.place(x=475, y=325)

    # Reads data from leaderborad file
    data = read_leaderboard_file()

    leader_size = 35
    y = 400
    x = 450

    global lbls
    lbls = []
    # Loop to display the leaderboard data as labels on screen
    for idx, name in enumerate(data, start=1):
        lbl = Label(
            canvas,
            text=(" " + str(idx) + ". " + str(name[0]) + " - " + str(name[1])),
            font=("Arial Bold", leader_size),
            background="black",
            fg="blue",
        )
        lbl.place(x=x, y=y)
        # Stores each label in an array
        lbls.append(lbl)
        leader_size -= 5
        y += 50
        x += 25
        # Only first 5 from file
        if idx == 5:
            break


def restart_game(event):

    canvas.delete(ball.imgGO)
    # Actions to show menu screen
    canvas.pack_forget()
    btn_restart.place_forget()
    lbl_leaderboard.place_forget()
    lbl_score.place_forget()

    # Removes leaderboard labels
    for i in range(len(lbls)):
        lbls[i].place_forget()

    place_buttons()

    brick.restart_bricks()
    canvas.coords(ball.ball, ball.start_coords)
    canvas.coords(player.playerID, player.player_start_coords)

    window.bind("<space>", ball.continue_game)


def quit_game(event):
    quit()


# Cheat code function for 100 lives
def cheat_code(event):
    window.unbind("<q>")
    global lives
    lives = 100
    ball.update_lives(lives)


# Ball class intialises all relevant data
class Ball:
    def __init__(self, canvas, player, brick, barrier):
        self.canvas = canvas
        self.player = player
        self.brick = brick
        self.barrier = barrier

        # Creates ball shape to canavs
        self.start_coords = [540, 540, 575, 575]
        self.ball = canvas.create_oval(self.start_coords, fill="red")

        self.pause_pressed = False

    def startGame(self, event):
        # Runs starting game methods and movement of objects

        window.unbind("<space>")

        barrier.create_barriers()

        self.canvas.coords(self.ball, self.start_coords)
        player.canvas.coords(player.playerID, player.player_start_coords)

        # Displays score and lives labels
        self.display_text()
        self.movement()

    def continue_game(self, event):

        window.unbind("<space>")
        global score_counter, lives

        self.update_score(score_counter)
        self.update_lives(lives)

        self.pause_pressed = False
        self.movement()

    def movement(self):
        lbl_game_help.place_forget()

        # Sets ball direction and speed
        global game_speedx, game_speedy
        self.ball_speedx = game_speedx
        self.ball_speedy = game_speedy

        # Objects are moved repeatedly by callin their functions repeatedly
        while True:
            if self.pause_pressed == False:
                self.move_ball()
                player.move_player()
                barrier.move_barrier()
            else:
                break

    def move_ball(self):
        canvas.move(self.ball, self.ball_speedx, self.ball_speedy)

        window.update()
        time.sleep(0.01)

        # Gets current co-ordinates of ball
        (lPos, topPos, rPos, botPos) = canvas.coords(self.ball)

        # Runs method for ball and brick collision
        if self.brick_collision1(lPos, topPos, rPos, botPos) == True:
            self.ball_speedy = -self.ball_speedy
            # Removes brick if hit
            brick.destroy_bricks()

        if self.brick_collision2(lPos, topPos, rPos, botPos) == True:
            self.ball_speedy = -self.ball_speedy
            # Removes brick if hit
            brick.destroy_bricks()

        if self.brick_collision3(lPos, topPos, rPos, botPos) == True:
            self.ball_speedy = -self.ball_speedy
            # Removes brick if hit
            brick.destroy_bricks()

        # Wall and ball collision detection
        if lPos <= 0 or rPos >= 1280:
            self.ball_speedx = -self.ball_speedx
        if topPos <= 0:
            self.ball_speedy = -self.ball_speedy

        # Player 'dying' collision
        if botPos >= 720:
            # Resets player and ball position
            self.start_coords = [540, 540, 575, 575]
            player.player_start_coords = [525, 580, 600, 595]

            canvas.coords(player.playerID, player.player_start_coords)
            canvas.coords(self.ball, self.start_coords)

            # Decreases lives
            global lives
            lives -= 1
            # Pauses game for player to restart
            self.pause_pressed = True
            self.update_lives(lives)
            # Check to see if player has lives left
            if lives <= 0:
                game_over()

            else:
                window.bind("<space>", self.continue_game)

        if self.player_collision(lPos, topPos, rPos, botPos) == True:
            self.ball_speedy = -self.ball_speedy
            self.ball_speedx = self.player.direction

        if self.barrier_collision(lPos, topPos, rPos, botPos) == True:
            self.ball_speedy = -self.ball_speedy

    # Player and ball collision check
    def player_collision(self, lPos, topPos, rPos, botPos):
        player_pos = self.canvas.coords(self.player.playerID)
        # Check for overlap of co-ordinates then returns a Boolean
        if rPos >= player_pos[0] and lPos <= player_pos[2]:
            if botPos >= player_pos[1] and botPos <= player_pos[3]:
                return True
            return False

    # Barrier and ball collision check
    def brick_collision1(self, lPos, topPos, rPos, botPos):

        for i in range(16):
            brick_pos = self.canvas.coords(self.brick.bricks[i])

            # Check for overlap of co-ordinates then returns a Boolean
            if rPos >= brick_pos[0] and lPos <= brick_pos[2]:
                if topPos >= brick_pos[1] and topPos <= brick_pos[3]:
                    # Finds which brick has been hit so that it can be destroyed
                    self.brick.brickID = i
                    global score_counter, brick_points
                    # Increments score
                    score_counter += brick_points
                    self.update_score(score_counter)
                    # Checks for max points
                    if score_counter == brick_points * 48:
                        self.pause_pressed = True
                        ball.imgW = ball.canvas.create_image(
                            (375, 10), image=imgW, anchor=NW
                        )
                        btn_quit.place(x=400, y=400)
                    return True
                return False

    def brick_collision2(self, lPos, topPos, rPos, botPos):
        for i in range(16, 32):
            brick_pos = self.canvas.coords(self.brick.bricks[i])

            # Check for overlap of co-ordinates then returns a Boolean
            if rPos >= brick_pos[0] and lPos <= brick_pos[2]:
                if topPos >= brick_pos[1] and topPos <= brick_pos[3]:
                    # Finds which brick has been hit so that it can be destroyed
                    self.brick.brickID = i
                    global score_counter, brick_points
                    # Increments score
                    score_counter += brick_points
                    self.update_score(score_counter)
                    # Checks for max points
                    if score_counter == brick_points * 48:
                        self.pause_pressed = True
                        ball.imgW = ball.canvas.create_image(
                            (375, 10), image=imgW, anchor=NW
                        )
                        btn_quit.place(x=400, y=400)

                    return True
                return False

    def brick_collision3(self, lPos, topPos, rPos, botPos):
        for i in range(32, 48):
            brick_pos = self.canvas.coords(self.brick.bricks[i])

            # Check for overlap of co-ordinates then returns a Boolean
            if rPos >= brick_pos[0] and lPos <= brick_pos[2]:
                if topPos >= brick_pos[1] and topPos <= brick_pos[3]:
                    # Finds which brick has been hit so that it can be destroyed
                    self.brick.brickID = i
                    global score_counter, brick_points
                    # Increments score
                    score_counter += brick_points
                    self.update_score(score_counter)
                    # Checks for max points
                    if score_counter == brick_points * 48:
                        self.pause_pressed = True
                        ball.imgW = ball.canvas.create_image(
                            (375, 10), image=imgW, anchor=NW
                        )
                        btn_quit.place(x=400, y=400)
                    return True
                return False

    def barrier_collision(self, lPos, topPos, rPos, botPos):
        for i in range(len(self.barrier.barriers)):
            # Check for overlap of co-ordinates then returns a Boolean
            barrier_pos = self.canvas.coords(self.barrier.barriers[i])
            if rPos >= barrier_pos[0] and lPos <= barrier_pos[2]:
                if topPos >= barrier_pos[1] and topPos <= barrier_pos[3]:
                    return True
                return False

    def display_text(self):
        global lives
        # Creates text to be displayed for score and lives
        self.score_text = canvas.create_text(
            100, 20, text="Score: ", font=("Arial", 25), fill="blue"
        )
        self.lives_text = canvas.create_text(
            1150, 20, text="Lives: " + str(lives), font=("Arial", 25), fill="blue"
        )

    # Update text function for lives and score
    def update_score(self, score_counter):
        canvas.itemconfig(self.score_text, text="Score: " + str(score_counter))

    def update_lives(self, liveCounter):
        canvas.itemconfig(self.lives_text, text="Lives: " + str(liveCounter))


# Player class
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        # Creates player shape at starting position
        self.player_start_coords = [525, 580, 600, 595]
        self.playerID = canvas.create_rectangle(self.player_start_coords, fill="blue")
        self.direction = 0

        # Key binds for player movement
        self.canvas.bind_all("<Right>", self.move_player_right)

        self.canvas.bind_all("<Left>", self.move_player_left)

        # Gets value of this depending on difficulty chosen
        global player_speedx

    def move_player(self):
        window.update()
        # Collision detection for player movement between walls
        canvas.move(self.playerID, self.direction, 0)
        player_pos = self.canvas.coords(self.playerID)

        # Stop moving when hit a wall
        if player_pos[0] <= 0:
            self.direction = 0
        if player_pos[2] >= 1280:
            self.direction = 0

    # Changes direction of player left or right when keys are pressed
    def move_player_right(self, event):
        self.direction = player_speedx

    def move_player_left(self, event):
        self.direction = -player_speedx


# Brick class
class Bricks:
    def __init__(self, canvas):
        self.canvas = canvas

        self.bricks = []

        # Variables created to allow positioning of the bricks
        self.brickLS = 40
        self.brickRS = 115
        self.brickID = 0
        self.brickTP = 150
        self.brickBT = 170

        self.brick_colour = "green"

        self.create_bricks()

    def create_bricks(self):
        # Creates bricks and stores them into an array
        for i in range(48):
            brick = canvas.create_rectangle(
                self.brickLS,
                self.brickTP,
                self.brickRS,
                self.brickBT,
                fill=self.brick_colour,
            )
            self.bricks.append(brick)
            # Increments these values
            self.brickRS += 75
            self.brickLS += 75

            # Check to display bricks on different line
            if self.brickRS > 1240:

                self.brickLS = 40
                self.brickRS = 115
                self.brickTP -= 50
                self.brickBT -= 50

                self.brick_colour = "purple"

            # Changes colour for a new line of bricks
            if self.brickTP == 50:
                self.brick_colour = "red"

    def restart_bricks(self):

        self.brickLS = 40
        self.brickRS = 115
        self.brickID = 0
        self.brickTP = 150
        self.brickBT = 170

        # Resets bricks to initial postion for a game restart
        for i in range(48):
            canvas.coords(
                self.bricks[i], self.brickLS, self.brickTP, self.brickRS, self.brickBT
            )
            self.brickRS += 75
            self.brickLS += 75

            if self.brickRS > 1240:
                self.brickLS = 40
                self.brickRS = 115
                self.brickTP -= 50
                self.brickBT -= 50

    # Destroys bricks by moving them off screen
    def destroy_bricks(self):
        canvas.coords(self.bricks[self.brickID], 0, 0, 0, 0)


# Barrier class
class Barriers:
    def __init__(self, canvas):
        self.canvas = canvas

        self.barriers = []
        self.barrierID = 0

        # Barrier position variables
        self.barrierLS = 200
        self.barrierRS = 300

        self.barrierTP = 75
        self.barrierBT = 95

        self.barrier_direction = [5, -5, 5]

    def create_barriers(self):
        global barrier_num

        # Creates an array of barriers depending on game difficulty
        for i in range(barrier_num):
            barrier_block = canvas.create_rectangle(
                self.barrierLS,
                self.barrierTP,
                self.barrierRS,
                self.barrierBT,
                fill="blue",
            )
            self.barriers.append(barrier_block)
            self.barrierLS += 300
            self.barrierRS += 300
            self.barrierTP += 50
            self.barrierBT += 50

    def move_barrier(self):
        window.update()
        # Moves each barrier in a different direction
        for i in range(len(self.barriers)):
            canvas.move(self.barriers[i], self.barrier_direction[i], 0)
            barrier_pos1 = self.canvas.coords(self.barriers[i])

            # Barrier collision detection
            if barrier_pos1[0] <= 0:
                self.barrier_direction[i] = 5
            if barrier_pos1[2] >= 1080:
                self.barrier_direction[i] = -5


window = Tk()
window.resizable(0, 0)

# Runs to create window size colour etc
configure_window()
# Canvas created but not displayed
canvas = Canvas(window, width=1280, height=720, bg="black", bd=1, highlightthickness=1)

# Images used in the game
img1 = PhotoImage(file="paused.png")
img_boss = PhotoImage(file="boss.png")
imgW = PhotoImage(file="win.png")

# Label to provide user help
lbl_game_help = Label(
    canvas,
    text="Press 'space' to start, 'P' to pause ",
    font=("Arial Bold", 25),
    background="black",
    fg="blue",
)

# Class objects declared
player = Player(canvas)
brick = Bricks(canvas)
barrier = Barriers(canvas)
ball = Ball(canvas, player, brick, barrier)


window.update()
window.mainloop()
