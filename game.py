import pgzrun

TITLE = "Quizmaster Game"
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

time_left = 10
score = 0
question_file = "questions.txt"
questions = []
question_count = 0
question_index = 0
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
is_game_over = False
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
    screen.fill("#243E36")
    screen.draw.filled_rect(marquee_box,"#243E36")
    screen.draw.filled_rect(question_box,"#222E50")
    screen.draw.filled_rect(timer_box,"#05A8AA")
    screen.draw.filled_rect(score_box,"#05A8AA")
    screen.draw.filled_rect(skip_box,"#2A1E5C")

    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"#F25C54")

    marquee_msg = "Welcome to the Quizmaster Show! " + f"You are at..Q: {question_index} of {question_count}!"
    screen.draw.textbox(marquee_msg,marquee_box,color = "#F7B267")
    screen.draw.textbox(str(time_left),timer_box,color = "#19180A",shadow = (0.5,0.5),scolor = "grey")
    screen.draw.textbox("Skip",skip_box,color = "#1F0322",angle =-90)
    screen.draw.textbox(f"Score: {score}",score_box,color = "#42033D")
    screen.draw.textbox(question[0].strip(),question_box,color = "#3DFAFF",shadow = (0.5,0.5),scolor = "#1F0322")
    
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color = "#440381")
        index = index + 1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x = marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file():
    global questions, question_count
    q_file = open(question_file,"r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index = question_index + 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for answer_box in answer_boxes:
        if answer_box.collidepoint(pos):
            if index == int(question[5]):
                correct_answer()
            else:
                game_over()
        index = index + 1
    if skip_box.collidepoint(pos):
        skip_question()




pgzrun.go()