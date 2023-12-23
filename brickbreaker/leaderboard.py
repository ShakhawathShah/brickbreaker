# File for separate window for leaderboard display

# Tkinter imports
from tkinter import Tk, Label, Canvas, Y
from user_module import read_leaderboard_file


def configureLeaderboardWindow(event):
    # Sets window size colour etc
    LeaderboardWindow = Tk()
    LeaderboardWindow.geometry("600x400")
    LeaderboardWindow.configure(background="black")
    LeaderboardWindow.title(
        "##########----------B r i c k    B r e a k e r ! ! ! !----------##########"
    )

    # Title label
    welcome = Label(
        LeaderboardWindow,
        text="Leaderboard",
        font=("Arial Bold", 40),
        background="black",
        fg="blue",
    )
    welcome.pack(fill=Y)

    data = read_leaderboard_file()

    # loop to display leaderboard as labels
    leaderSize = 40
    for idx, name in enumerate(data, start=1):
        lbl = Label(
            LeaderboardWindow,
            text=(" " + str(idx) + ". " + str(name[0]) + " - " + str(name[1])),
            font=("Arial", leaderSize),
            background="black",
            fg="blue",
        )
        lbl.pack()
        leaderSize -= 5
        if idx == 5:
            break

    LeaderboardWindow.update()
    LeaderboardWindow.mainloop()
