import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


correct_guesses = []
while len(correct_guesses) < 50:
    answer = str(screen.textinput(title = f"{len(correct_guesses)}/50 States Correct", prompt = "Enter a State name:"))
    answer_state = answer.title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state != "" and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


turtle.mainloop()