import random

question_list = {"집밖에 나가는 것 자체가 스케줄 ?": "", "불금에는 북적대는 곳보단 집이지 ?": "", "휴대폰만 있어도 안 심심한가요 ?": "", "카톡, 문자 알림을 잘 확인하지 않나요 ?": "",
                 "아무 생각이 없다. 왜냐하면 아무 생각이 없기 때문이다 라고 자주 느끼나요 ?": "", "당신은 배달앱 VIP인가요 ?": "", "친구와의 약속이 갑작스레 파토났을 때 아쉽다는 생각보다 오예!라는 생각이 더 자주 드나요 ?": ""}

name = input("당신의 이름은 ? ")
print("=====안녕하세요", name, "님, 당신은 집순이일까요?=====")
print("=====모든 질문의 대답을 네, 아니오로 답변해주세요=====")
real_count = int(input("받을 질문의 개수를 입력해주세요 (최대 7개 가능) : "))


def qna(count):
    yes = 0
    keys = random.sample(list(question_list.keys()), count)
    for i in range(count):
        print(keys[i])
        question_list[keys[i]] = input("답변: ")
        if question_list[keys[i]] == "네":
            yes += 1

    return yes


def your_type(yes, count):
    if yes/count >= 0.75:
        print("당신은 집순이 입니다.")
    elif yes/count >= 0.50:
        print("당신은 집을 조금 더 좋아하네요.")
    elif yes/count >= 0.25:
        print("당신은 밖을 조금 더 좋아하네요.")
    else:
        print("당신은 바깥순이 입니다.")


yes_count = qna(real_count)
your_type(yes_count, real_count)
