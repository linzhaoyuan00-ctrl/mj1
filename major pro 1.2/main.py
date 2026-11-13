import flet as ft
import json

def main(page: ft.Page):
    page.scroll=ft.ScrollMode.ALWAYS
    page.title = "Haunted Date"
    page.window_width = 520
    page.window_height = 720
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src="666.jpeg",
            fit= ft.BoxFit.FILL,
        )
    )

    def show_login_page():
        in_username = ft.TextField(label="username", width=400)
        in_pw = ft.TextField(label="password", password=True, width=400)

        def login_click(e):
            with open("data.json", "r") as f:
                user_list = json.load(f)
            found = False
            for u in user_list:
                if u["Username"] == in_username.value and u["Password"] == in_pw.value:
                    found = True
                    show_home_page(in_username.value)
                    return
            if not found:
                page.controls.clear()
                scroll_col = ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("LOGIN", size=24),
                            in_username,
                            in_pw,
                            ft.Button("Log In", on_click=login_click),
                            ft.Button("No account? Go to Register", on_click=go_register),
                            ft.Text("Wrong username or password"),
                            ft.Text("")
                        ],
                    )
                )
                page.add(scroll_col)
        def go_register(e):
            show_register_page()
        page.controls.clear()
        scroll_col = ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("LOGIN", size=24),
                    in_username,
                    in_pw,
                    ft.Button("Log In", on_click=login_click),
                    ft.Button("No account? Go to Register", on_click=go_register),
                    ft.Text("")
                ],
            )
        )
        page.add(scroll_col)
    def show_register_page():
        re_first = ft.TextField(label="First Name", width=400)
        re_last = ft.TextField(label="Last Name", width=400)
        re_age = ft.TextField(label="Age", width=400)
        re_gender = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="male", label="male"),
                ft.Radio(value="female", label="female")
            ])
        )
        re_username = ft.TextField(label="username", width=400)
        re_password = ft.TextField(label="password", password=True, width=400)
        def register_click(e):
            with open("data.json", "r") as f:
                user_list = json.load(f)
            is_ok = True
            if re_first.value == "":
                is_ok = False
            if re_last.value == "":
                is_ok = False
            if re_age.value == "":
                is_ok = False
            if re_gender.value is None:
                is_ok = False
            if re_username.value == "":
                is_ok = False
            if re_password.value == "":
                is_ok = False
            if not is_ok:
                page.controls.clear()
                scroll_col = ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("REGISTER", size=24),
                            re_first,
                            re_last,
                            re_age,
                            ft.Text("Gender"),
                            re_gender,
                            re_username,
                            re_password,
                            ft.Button("Register", on_click=register_click),
                            ft.Button("Already have account? Go to Login", on_click=go_login),
                            ft.Text("All fields are required!"),
                            ft.Text("")
                        ],
                    )
                )
                page.add(scroll_col)
                return
            new_user = {
                "Firstname": re_first.value,
                "Lastname": re_last.value,
                "Age": re_age.value,
                "Gender": re_gender.value,
                "Username": re_username.value,
                "Password": re_password.value,
                "Answers": ["", "", "", "", "", "", "", "", "", ""]
            }
            user_list.append(new_user)
            with open("data.json", "w") as f:
                json.dump(user_list, f)
            show_login_page()

        def go_login(e):
            show_login_page()

        page.controls.clear()
        scroll_col = ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("REGISTER", size=24),
                    re_first,
                    re_last,
                    re_age,
                    ft.Text("Gender"),
                    re_gender,
                    re_username,
                    re_password,
                    ft.Button("Register", on_click=register_click),
                    ft.Button("Already have account? Go to Login", on_click=go_login),
                    ft.Text("")
                ],
            )
        )
        page.add(scroll_col)
    def show_home_page(current_username):
        page.controls.clear()
        def go_to_question_page(e):
            show_question_page(current_username)
        def go_to_match_page(e):
            show_match_page(current_username)
        def go_to_login_page(e):
            show_login_page()
        home_view = ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Welcome " + current_username, size=26),
                    ft.Text(""),
                    ft.Button("Answer Questions", on_click=go_to_question_page),
                    ft.Button("Find Match", on_click=go_to_match_page),
                    ft.Button("Logout", on_click=go_to_login_page)
                ]
            )
        )
        page.add(home_view)

    def show_match_page(current_username):
        with open("data.json", "r") as f:
            user_list = json.load(f)
        me = None
        for u in user_list:
            if u["Username"] == current_username:
                me = u
                break
        my_answers = me["Answers"]
        my_gender = me["Gender"]   
        if "" in my_answers:
            page.controls.clear()
            def go_to_question_from_match(e):
                show_question_page(current_username)
            def go_back_home_from_match_warning(e):
                show_home_page(current_username)
            warning_view = ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("You must finish all questionnaire first!", size=20),
                        ft.Button("Go Answer Questions", on_click=go_to_question_from_match),
                        ft.Button("Back Home", on_click=go_back_home_from_match_warning)
                    ]
                )
            )
            page.add(warning_view)
            return

        match_result_list = []
        for other_user in user_list:
            if other_user["Username"] == current_username:
                continue
            if other_user["Gender"] == my_gender:
                continue
            other_ans = other_user["Answers"]
            if "" in other_ans:
                continue
            score = 0
            for i in range(10):
                a = my_answers[i]
                b = other_ans[i]
                if a == b:
                    score = score + 1

            match_result_list.append({
                "username": other_user["Username"],
                "firstname": other_user["Firstname"],
                "score": score
            })

        length = len(match_result_list)
        for i in range(length):
            for j in range(0, length - i - 1):
                if match_result_list[j]["score"] < match_result_list[j + 1]["score"]:
                    temp = match_result_list[j]
                    match_result_list[j] = match_result_list[j + 1]
                    match_result_list[j + 1] = temp

        page.controls.clear()
        def go_back_home_from_match(e):
            show_home_page(current_username)
        match_controls = [
            ft.Text("Match Results", size=24),
            ft.Text("Your answers compared against other users (max score 10)", size=14),
            ft.Text("")
        ]
        if len(match_result_list) == 0:
            match_controls.append(ft.Text("No other completed profiles to match!"))
        else:
            for item in match_result_list:
                match_controls.append(ft.Text(item["firstname"] + " (" + item["username"] + ")  Score: " + str(item["score"]) + "/10"))
            best = match_result_list[0]
            match_controls.append(ft.Text(""))
            match_controls.append(
                ft.Text("BEST MATCH: " + best["firstname"] + " | Score " + str(best["score"]) + "/10", size=18)
            )
        match_controls.append(ft.Button("Back Home", on_click=go_back_home_from_match))
        scroll_view = ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=match_controls,
                scroll="always"
            )
        )
        page.add(scroll_view)

    def show_question_page(current_username):
        with open("data.json", "r") as f:
            user_list = json.load(f)
        q1 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Gaming or Movies", label="Gaming or Movies"),
                ft.Radio(value="Sport or fitness", label="Sport or fitness"),
                ft.Radio(value="Hanging with Friends", label="Hanging with Friends"),
                ft.Radio(value="Arts and Hobbies", label="Arts and Hobbies")
            ])
        )
        q2 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Pop or Hip-Hop", label="Pop or Hip-Hop"),
                ft.Radio(value="Rock", label="Rock"),
                ft.Radio(value="Electronic", label="Electronic"),
                ft.Radio(value="R&B", label="R&B")
            ])
        )
        q3 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Dogs", label="Dogs"),
                ft.Radio(value="Cats", label="Cats"),
                ft.Radio(value="Both", label="Both"),
                ft.Radio(value="neither", label="neither")
            ])
        )
        q4 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Spring", label="Spring"),
                ft.Radio(value="Summer", label="Summer"),
                ft.Radio(value="Fall", label="Fall"),
                ft.Radio(value="Winter", label="Winter")
            ])
        )
        q5 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Introvert", label="Introvert"),
                ft.Radio(value="Extrovert", label="Extrovert"),
                ft.Radio(value="Both", label="Both")
            ])
        )
        q6 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Team", label="Team activities"),
                ft.Radio(value="Alone", label="Individual activities")
            ])
        )
        q7 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Long-term partnership leading to marriage", label="Long-term partnership leading to marriage"),
                ft.Radio(value="Casual dating to see where things go", label="Casual dating to see where things go"),
                ft.Radio(value="Deep emotional connection", label="Deep emotional connection"),
                ft.Radio(value="Finding a best friend to travel", label="Finding a best friend to travel")
            ])
        )
        q8 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Address it right away until it is completely resolved", label="Address it right away until it is completely resolved"),
                ft.Radio(value="Take time alone to calm down before discussing it", label="Take time alone to calm down before discussing it"),
                ft.Radio(value="Apologize quickly to keep the peace and move on", label="Apologize quickly to keep the peace and move on"),
                ft.Radio(value="Use humor or change the subject to lighten the tension", label="Use humor or change the subject to lighten the tension")
            ])
        )
        q9 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="Working out or going for a long run", label="Working out or going for a long run"),
                ft.Radio(value="Talking it through with friends or a partner", label="Talking it through with friends or a partner"),
                ft.Radio(value="Unwinding alone with music, movies, or games", label="Unwinding alone with music, movies, or games"),
                ft.Radio(value="Taking a nap or resting quietly", label="Taking a nap or resting quietly")
            ])
        )
        q10 = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="A genuine, explicit apology", label="A genuine, explicit apology"),
                ft.Radio(value="Give verbal assurances that the relationship is stable", label="Give verbal assurances that the relationship is stable"),
                ft.Radio(value="A clear plan for how to avoid the issue next time", label="A clear plan for how to avoid the issue next time"),
                ft.Radio(value="A return to normal routine and lightheartedness", label="A return to normal routine and lightheartedness")
            ])
        )

        def submit_click(e):
            answers = [
                q1.value, q2.value, q3.value, q4.value, q5.value,
                q6.value, q7.value, q8.value, q9.value, q10.value
            ]
            all_answered = True
            for ans in answers:
                if ans is None:
                    all_answered = False
            if not all_answered:
                page.controls.clear()
                scroll_col = ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Haunted Date Questions", size=24),
                            ft.Text("1. What do you like doing?", size=18), q1,
                            ft.Text("2. What music do you like?", size=18), q2,
                            ft.Text("3. Which pets do you prefer?", size=18), q3,
                            ft.Text("4. What is your favourite season?", size=18), q4,
                            ft.Text("5. Are you an introvert or extrovert?", size=18), q5,
                            ft.Text("6. What is your biggest need when repairing after a fight?", size=18), q6,
                            ft.Text("7. What is your ideal relationship goal?", size=18), q7,
                            ft.Text("8. When an argument starts, what is your immediate instinct?", size=18), q8,
                            ft.Text("9. How do you deal with stress?", size=18), q9,
                            ft.Text("10. What is your ideal living environment?", size=18), q10,
                            ft.Button("Submit", on_click=submit_click),
                            ft.Button("Back Home", on_click=go_back_home_from_question),
                            ft.Text("Please answer all questions.")
                        ],
                    )
                )
                page.add(scroll_col)
                return
            for u in user_list:
                if u["Username"] == current_username:
                    u["Answers"] = answers
            with open("data.json", "w") as f:
                json.dump(user_list, f)
            show_home_page(current_username)

        def go_back_home_from_question(e):
            show_home_page(current_username)

        page.controls.clear()
        scroll_col = ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Haunted Date Questions", size=24),
                    ft.Text("1. What do you like doing?", size=18), q1,
                    ft.Text("2. What music do you like?", size=18), q2,
                    ft.Text("3. Which pets do you prefer?", size=18), q3,
                    ft.Text("4. What is your favourite season?", size=18), q4,
                    ft.Text("5. Are you an introvert or extrovert?", size=18), q5,
                    ft.Text("6. What is your biggest need when repairing after a fight?", size=18), q6,
                    ft.Text("7. What is your ideal relationship goal?", size=18), q7,
                    ft.Text("8. When an argument starts, what is your immediate instinct?", size=18), q8,
                    ft.Text("9. How do you deal with stress?", size=18), q9,
                    ft.Text("10. What is your ideal living environment?", size=18), q10,
                    ft.Button("Submit", on_click=submit_click),
                    ft.Button("Back Home", on_click=go_back_home_from_question),
                    ft.Text("")
                ],
            )
        )
        page.add(scroll_col)
    show_login_page()
ft.run(main)



