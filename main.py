import random
import simplegui ## działa tylko na coursera
import math

next_runda = 1
results_comp = 0
results_palyer = 0
choose_game = int(input(
    "Aby zagrac w kamien-spock-papier-jaszczurka-nożyce wybierz 1\nAby zagrac w traf w sekunde 2\nAby zagrac zgadywanie liczb wybierz 3\nAby zagrac w ping ponga wybierz 4"))

if (choose_game == 1):
    print
    "Wybrales rozbudowana wersje kamien papier nozyce powodzenia!"


    def number_to_name(num):
        if num == 0:
            result = "kamien"
        elif num == 1:
            result = "spock"
        elif num == 2:
            result = "papier"
        elif num == 3:
            result = "jaszczurka"
        elif num == 4:
            result = "nozyce"
        return result


    def name_to_number(name):
        if name == "kamien":
            result = 0
        elif name == "spock":
            result = 1
        elif name == "papier":
            result = 2
        elif name == "jaszczurka":
            result = 3
        elif name == "nozyce":
            result = 4
        return result


    def rpsls(name):
        global results_palyer, results_comp
        player_number = name_to_number(name)
        comp_number = random.randrange(0, 5)
        print
        "Twoj wybor:", name
        print
        "Wybor komputera:", number_to_name(comp_number)
        if (comp_number + 1) % 5 == player_number:
            print
            "Wygrywasz!"
            results_palyer += 1
        elif (comp_number + 2) % 5 == player_number:
            print
            "Wygrywasz!"
            results_palyer += 1
        elif comp_number == player_number:
            print
            "Remis!"
        else:
            print
            "Computer Wygrywa!"
            results_comp += 1
        print
        results_palyer, ":", results_comp


    while (next_runda == 1):
        wybor = input("Co wybierasz:")
        rpsls(wybor)
        next_runda = int(input("Aby zagrać raz jeszcze kilknij 1: "))
elif (choose_game == 2):
    print
    "wybrales traf w sekunde gra polega na zatrzymywaniu stopera w rownej skundzie powodzenia!"
    interval = 100
    tick = 0
    seconds = 0
    milisecond = 0
    string = 0
    stop_timer = 0
    success_stop = 0
    stop_check = False
    start_check = False


    def format(t):
        global string
        milisecond = t % 10
        second = int((t / 10) % 10)
        minutes = int(t / 100) % 6
        ten_minutes = int(t / 600) % 600
        string = str(ten_minutes) + ":" + str(minutes) + str(second) + "." + str(milisecond)


    def start():
        global stop_check, start, start_check
        start_check = True
        stop_check = False
        timer.start()


    def stop():
        timer.stop()
        global second, success_stop, stop_timer, stop_check, start_check
        if (stop_check == False and start_check == True):
            stop_check = True
            success_stop = int(success_stop)
            stop_timer = int(stop_timer)
            if (milisecond % 10 == 0 and milisecond != 0):
                stop_timer += 1
                success_stop += 1
            else:
                stop_timer += 1


    def reset():
        global milisecond, stop_timer, success_stop, string
        milisecond = 0
        stop_timer = 0
        success_stop = 0
        timer.stop()
        string = "0"
        stop_check = True


    def tick():
        global milisecond
        milisecond += 1
        format(milisecond)


    def draw(canvas):
        global string
        global stop_timer
        global success_stop
        text = str(string)
        stop_timer = str(stop_timer)
        success_stop = str(success_stop)
        canvas.draw_text(text, (100, 120), 40, "White")
        canvas.draw_text(stop_timer + "/" + success_stop, (190, 20), 20, "White")


    frame = simplegui.create_frame("Stopwatch game", 250, 250)

    frame.add_button("Start", start, 100)
    frame.add_button("Stop", stop, 100)
    frame.add_button("Reset", reset, 100)
    timer = simplegui.create_timer(interval, tick)
    frame.set_draw_handler(draw)
    frame.start()

elif (choose_game == 3):

    print(
        "Wybrales zgadywanie liczb musisz trafic wylosowana liczbe przez komputer, do wyobru masz dwa przedzialy powodzenia!")
    secret_number = 0
    guesses_left = 0


    def new_game():
        print
        "\n"
        print
        "\n \n New game! \n \n"
        print
        "\n"


    def range100():

        global secret_number, guesses_left
        print
        "\n"
        secret_number = random.randint(0, 100)
        guesses_left = 7
        print
        "Nowa gra. Liczba miedzy 0-100. Pozostalo 7 prob"


    def range1000():

        global secret_number, guesses_left
        print
        "\n"
        secret_number = random.randint(0, 1000)
        guesses_left = 10
        print
        "Nowa gra. Liczba miedzy 0-1000. Pozostalo 10 prob."


    def input_handler(guess):
        global guesses_left
        print
        "\n"
        print
        "Wybrana liczba " + guess

        guesses_left = guesses_left - 1

        if guesses_left == 0 and guess != secret_number:
            print
            "Przegrana. Pozostało 0 prob. Ukryta lczba to: " + str(secret_number)
            if secret_number < 100:
                range100()
            if secret_number >= 100:
                range1000()

        elif int(guess) == secret_number:
            print
            "Pozostalo prob: " + str(guesses_left)
            print
            "Zgadles, Wygrna!"
            if secret_number < 100:
                range100()
            elif secret_number >= 100:
                range1000()
        elif int(guess) < secret_number:
            print
            "Pozostalo prob: " + str(guesses_left)
            print
            "Ukrtya liczba jest wieksza od podanej"
        elif int(guess) > secret_number:
            print
            "Pozostalo prob " + str(guesses_left)
            print
            "Ukryta liczba jest mniejsza od podanej!"
        print
        "\n"


    frame = simplegui.create_frame("gameframe", 500, 500)
    frame.add_button("Przedzial [0, 100)", range100)
    frame.add_button("Przedzial [0, 1000)", range1000)
    frame.add_input("Podaj liczbe: ", input_handler, 100)
    frame.start()
    range100()

elif (choose_game == 4):

    print(
        "Wybrales ping ponga jest to gra dla 2 osob jedna steruje uzywajac W i A druga uzwyajas strzalek GORA i DOL powodzenia!")

    width = 600
    half_width = width / 2
    height = 400
    half_height = height / 2
    ball_radius = 20
    pad_width = 8
    pad_height = 80
    LEFT = False
    RIGHT = True

    paddle1_pos = height / 2.5
    paddle2_pos = height / 2.5
    paddle1_vel = 0
    paddle2_vel = 0
    paddle_vel = 5

    ball_pos = [half_width, half_height]
    ball_vel = [0, 1]


    def spawn_ball(direction):
        global ball_pos, ball_vel
        ball_pos = [half_width, half_height]
        ball_vel[0] = -random.randrange(120, 240) / 100
        if direction == True:
            ball_vel[0] *= -1
        ball_vel[1] = -random.randrange(60, 180) / 100


    def new_game():
        global paddle1_pos, paddle2_pos
        global score1, score2
        score1 = 0
        score2 = 0
        spawn_ball(0)
        paddle1_pos = height / 2.5
        paddle2_pos = height / 2.5


    def draw(c):
        global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

        c.draw_line([half_width, 0], [half_width, height], 1, "blue")
        c.draw_line([pad_width, 0], [pad_width, height], 1, "blue")
        c.draw_line([width - pad_width, 0], [width - pad_width, height], 1, "blue")

        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if ball_pos[0] <= (ball_radius + pad_width) or ball_pos[0] >= (width - pad_width - ball_radius):
            ball_vel[0] *= -1

            if (ball_pos[0] > half_width):
                if (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + pad_height):
                    score1 += 1
                    spawn_ball(LEFT)
                else:
                    ball_vel[0] += .1 * ball_vel[0]

            if (ball_pos[0] < half_width):
                if (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + pad_height):
                    score2 += 1
                    spawn_ball(RIGHT)
                else:
                    ball_vel[0] += .1 * ball_vel[0]

        if ball_pos[1] <= ball_radius or ball_pos[1] >= (height - ball_radius):
            ball_vel[1] *= -1

        c.draw_circle(ball_pos, ball_radius, 2, "White", "Green")

        global paddle1_vel, paddle2_vel

        if (paddle1_pos <= height - pad_height and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0):
            paddle1_pos += paddle1_vel
        elif (paddle2_pos <= height - pad_height and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0):
            paddle2_pos += paddle2_vel

        c.draw_polygon([[0, paddle1_pos], [pad_width, paddle1_pos], [pad_width, (paddle1_pos) + pad_height],
                        [0, (paddle1_pos) + pad_height]], 1, "green", "white")
        c.draw_polygon(
            [[width, paddle2_pos], [width - pad_width, paddle2_pos], [width - pad_width, paddle2_pos + pad_height],
             [width, paddle2_pos + pad_height]], 1, "green", "white")

        c.draw_text(str(score1), [225, 100], 60, "pink")
        c.draw_text(str(score2), [350, 100], 60, "pink")


    def keydown(key):
        global paddle1_vel, paddle2_vel, paddle_vel

        if key == simplegui.KEY_MAP["w"]:
            paddle1_vel = -paddle_vel
        elif key == simplegui.KEY_MAP["s"]:
            paddle1_vel = paddle_vel

        if key == simplegui.KEY_MAP["down"]:
            paddle2_vel = paddle_vel
        elif key == simplegui.KEY_MAP["up"]:
            paddle2_vel = -paddle_vel


    def keyup(key):
        global paddle1_vel, paddle2_vel, paddle_vel

        if key == simplegui.KEY_MAP["w"]:
            paddle1_vel = 0
        elif key == simplegui.KEY_MAP["s"]:
            paddle1_vel = 0

        if key == simplegui.KEY_MAP["down"]:
            paddle2_vel = 0
        elif key == simplegui.KEY_MAP["up"]:
            paddle2_vel = 0


    frame = simplegui.create_frame("Pong", width, height)
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(keydown)
    frame.set_keyup_handler(keyup)
    frame.add_button("Restart", new_game, 200)

    new_game()
    frame.start()
