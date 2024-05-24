import tkinter as tk
import random
from tkinter import font


def check_winner(user_action: str) -> None:
    machine_action = random.choice(actions)
    global round_no

    if user_action == machine_action:
        scrores["draw"] += 1
        lbl_score_draw.config(text=f"Draw: {scrores["draw"]}")
        lbl_round_result.config(text=f"DRAW, both selected {user_action}")
    elif (
        (user_action == "rock" and machine_action == "scissors")
        or (user_action == "scissors" and machine_action == "paper")
        or (user_action == "paper" and machine_action == "rock")
    ):
        scrores["player"] += 1
        lbl_score_player.config(text=f"Player: {scrores["player"]}")
        lbl_round_result.config(
            text=f"PLAYER wins! {user_action} over {machine_action}"
        )
    else:
        scrores["machine"] += 1
        lbl_score_machine.config(text=f"Computer: {scrores["machine"]}")
        lbl_round_result.config(
            text=f"COMPUTER wins! {machine_action} over {user_action}"
        )

    round_no += 1
    lbl_round_count.config(text=f"Number of Played Rounds: {round_no}")
    
# def reset_game():
    # global round_no, scrores
    # round_no = 0
    # for keys, items
    


actions = ["rock", "paper", "scissors"]
scrores = {"player": 0, "machine": 0, "draw": 0}
round_no = 0

window = tk.Tk()
window.title("Rock Paper Scissor Game")
window.rowconfigure(0, minsize=100)
window.resizable(0,0)

frm_score = tk.Frame(window, bg="cyan", borderwidth=2, relief="solid")
frm_round_count = tk.Frame(window, bg="orange", borderwidth=2, relief="solid")
frm_round_result = tk.Frame(window)
frm_action = tk.Frame(window)
frm_action = tk.Frame(window)

lbl_score_player = tk.Label(
    frm_score, text=f"Player: {scrores["player"]}", font="arial 15", bg="cyan"
)
lbl_score_machine = tk.Label(
    frm_score, text=f"Computer: {scrores["machine"]}", font="arial 15", bg="cyan"
)
lbl_score_draw = tk.Label(
    frm_score, text=f"Draw: {scrores["draw"]}", font="arial 15", bg="cyan"
)

lbl_score_player.grid(row=0, column=0, padx=10, pady=5)
lbl_score_machine.grid(row=0, column=1, padx=10, pady=5)
lbl_score_draw.grid(row=0, column=2, padx=10, pady=5)

lbl_round_count = tk.Label(
    frm_round_count,
    text=f"Number of Played Rounds: {round_no}",
    font="arial 15",
    bg="orange",
)
lbl_round_count.grid(row=0, column=0, padx=10, pady=10)

lbl_round_result = tk.Label(
    frm_round_result,
    bg="white",
    font="normal 12 bold",
    borderwidth=1,
    relief="solid",
    width=40,
    height=2,
)
lbl_round_result.grid(row=0, column=0, pady=5)

btn_rock = tk.Button(
    frm_action, text="Rock", command=lambda: check_winner("rock"), bg="red", font=15
)
btn_paper = tk.Button(
    frm_action,
    text="Paper",
    command=lambda: check_winner("paper"),
    bg="light green",
    font=15,
)
btn_scissors = tk.Button(
    frm_action,
    text="Scissors",
    command=lambda: check_winner("scissors"),
    bg="light blue",
    font=15,
)
btn_exit = tk.Button(
    frm_action,
    text="EXIT",
    command=lambda: window.destroy(),
    fg="white",
    bg="black",
    font="normal 20 bold",
    borderwidth=2,
)

btn_rock.grid(row=0, column=0, padx=10, pady=5)
btn_paper.grid(row=0, column=1, padx=10, pady=5)
btn_scissors.grid(row=0, column=2, padx=10, pady=5)
btn_exit.grid(row=1, column=1, pady=10)

frm_score.grid(row=0, padx=10, pady=10)
frm_round_count.grid(row=1, padx=10, pady=10)
frm_round_result.grid(row=2, padx=10, pady=10)
frm_action.grid(row=3, padx=10, pady=10)

window.mainloop()
