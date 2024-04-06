import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
game = True
state = 0
empty = []

while game:
    answer_state = screen.textinput(title=f"Guess the State {state}/50", prompt="What's another state's name?")
    temp_list = data["state"].to_list()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in empty]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for i in temp_list:
        for e in empty:
            if e == answer_state:
                answer_state = screen.textinput(title=f"Guess the State {state}/50", prompt="Pick a different state.")
        if answer_state == 'Exit':
            break
        if i == answer_state:
            state += 1
            empty.append(i)
            text = turtle.Turtle()
            text.color("black")
            text.penup()
            text.hideturtle()
            temp = data[data['state'] == answer_state]
            text.goto(int(temp.iat[0, 1]), int(temp.iat[0, 2]))
            text.write(f"{i}", font=("Courier", 12, "normal"))


