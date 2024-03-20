import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
list_state = state_data.state.to_list()
guessed_states = []
not_guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                   prompt="Enter the name of a state:").title()
    if user_answer == "Exit":
        break
    if user_answer in list_state:
        guessed_states.append(user_answer)
        list_state.remove(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coord = state_data[state_data.state == user_answer]
        t.goto(int(coord.x), int(coord.y))
        t.write(user_answer)

df = pandas.DataFrame(list_state)
df.to_csv("states_to_learn.csv")
