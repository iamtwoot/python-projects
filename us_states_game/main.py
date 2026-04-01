import turtle
import pandas as pd

def write_state(state_name, x_cor, y_cor):
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(x_cor, y_cor)
    new_state.write(state_name)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(
        title=f"{score}/{len(data.state.values)} States Correct",
        prompt="What`s another state name?",
    ).title()

    if answer_state == "Exit":
        for state in all_states:
            states_to_learn = [s for s in all_states if s not in correct_guesses]
            pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        write_state(
            answer_state,
            state_data.x.item(),
            state_data.y.item()
        )
        correct_guesses.append(answer_state)
        score += 1
