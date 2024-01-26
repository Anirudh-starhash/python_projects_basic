import turtle
import pandas
import time
screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
# screen.exitonclick()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
missing_states=[]
is_game=True
answered=[]
while is_game:
    with open("me.txt",'r') as f:
        guess=int(f.read())
    answer = turtle.textinput(title=f"States gussed are {guess}/50 ", prompt="What's another state name in US").title()
    if answer=='Exit':
        for x in all_states:
            if x not in answered:
                missing_states.append(x)
        break
    print(answer.capitalize())
    if answer in all_states:
        state = data[data.state == answer]
        if answer not in answered:
            answered.append(answer)
            guess+=1
        if guess==50:
            is_game=False
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(int(state.x),int(state.y))
        timmy.write(answer)
        with open("me.txt","w") as f:
            f.write(str(guess))

data=pandas.DataFrame(missing_states)
data.to_csv("missing_states.csv")





screen.exitonclick()