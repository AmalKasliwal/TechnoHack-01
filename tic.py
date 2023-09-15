import tkinter as tk
from PIL import ImageTk, Image
import random


def play_game(user_choice):
    computer_choice = random.randint(1, 3)

    user_img = get_choice_image(user_choice)
    user_choice_label.config(image=user_img)

    computer_img = get_choice_image(computer_choice)
    computer_choice_label.config(image=computer_img)

    result_text = ""
    if user_choice == computer_choice:
        result_text = "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (
            user_choice == 3 and computer_choice == 2):
        result_text = "You win!"
    else:
        result_text = "Computer wins!"

    result_label.config(text=result_text)

    # Save the result as an image
    result_image = Image.new('RGB', (300, 150), color='white')
    result_draw = ImageDraw.Draw(result_image)
    result_draw.text((10, 10), "Your Choice: {}".format(get_choice_name(user_choice)), fill='black')
    result_draw.text((10, 40), "Computer's Choice: {}".format(get_choice_name(computer_choice)), fill='black')
    result_draw.text((10, 70), "Result: {}".format(result_text), fill='black')
    result_image.save('result.png')


def get_choice_image(choice):
    if choice == 1:
        return ImageTk.PhotoImage(Image.open("rock.jpg"))
    elif choice == 2:
        return ImageTk.PhotoImage(Image.open("page.jpg"))
    else:
        return ImageTk.PhotoImage(Image.open("sissor.jpg"))


def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    else:
        return "Scissors"


def on_rock():
    play_game(1)


def on_paper():
    play_game(2)


def on_scissors():
    play_game(3)


window = tk.Tk()
window.title("Rock, Paper, Scissors")

rock_image = ImageTk.PhotoImage(Image.open("rock.jpg"))
rock_button = tk.Button(window, image=rock_image, command=on_rock)
rock_button.pack(pady=10)

paper_image = ImageTk.PhotoImage(Image.open("page.jpg"))
paper_button = tk.Button(window, image=paper_image, command=on_paper)
paper_button.pack(pady=10)

scissors_image = ImageTk.PhotoImage(Image.open("sissor.jpg"))
scissors_button = tk.Button(window, image=scissors_image, command=on_scissors)
scissors_button.pack(pady=10)
user_label = tk.Label(window, text="user choice:", font=("Arial", 16))
user_label.pack(pady=20)
user_choice_label = tk.Label(window)
user_choice_label.pack()
comp_label = tk.Label(window, text="computer choice:", font=("Arial", 16))
comp_label.pack(pady=20)
computer_choice_label = tk.Label(window)
computer_choice_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack(pady=20)

window.mainloop()
