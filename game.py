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
game_over = False
marquee_msg = ""

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
timer_box.move_ip(700,100)