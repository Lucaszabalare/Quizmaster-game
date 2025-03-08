
import pgzrun

TITLE = "Quizmaster Game: Cat Edition"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)
timer_box = Rect(0,0,150,150)
score_box = Rect(0,0,150,50)

time_left = 9
score = 0
question_file = "questions.txt"
questions = []
question_count = 0
question_index = 0
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
game_over = False
marquee_msg = ""

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)
score_box.move_ip(700,50)

def draw():
    global marquee_msg
    screen.clear()
    screen.fill("#2A0800")
    screen.draw.filled_rect(marquee_box,"#2A0800")
    screen.draw.filled_rect(question_box,"#EF8354")
    screen.draw.filled_rect(timer_box,"#F5A65B")
    screen.draw.filled_rect(score_box,"#F5A65B")
    screen.draw.filled_rect(skip_box,"#F2CD5D")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"#F25C54")

    marquee_msg = "Welcome to the Quizmaster Show! " + f"You are at..Q: {question_index} of {question_count}!"
    screen.draw.textbox(marquee_msg,marquee_box,color = "#FFF05A")
    screen.draw.textbox(str(time_left),timer_box,color = "#A40606",shadow = (0.5,0.5),scolor = "grey")
    screen.draw.textbox("Skip",skip_box,color = "#131200",angle =-90)
    screen.draw.textbox(f"Score: {score}",score_box,color = "#2B2D42")
    screen.draw.textbox("Hi",question_box,color = "#FF2E00",shadow = (0.5,0.5),scolor = "#2A0800")


def update():
    pass

pgzrun.go()