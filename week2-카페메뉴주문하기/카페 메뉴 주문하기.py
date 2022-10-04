
from datetime import datetime

print("\n※ 디저트 카페에 오신 것을 환영합니다! ※\n")
print("※ 주문을 중단하고 싶으시다면 'q'를 눌러주세요! 아래는 메뉴판입니다. ※\n")


menu_desert = {"치즈 케이크": 5000, "티라미수": 4500,
               "크로플": 3500, "와플": 3000, "초코 브라우니": 3500}
menu_baverage = {"아메리카노": 3000, "바닐라 라떼": 4000, "녹차 라떼": 4000,
                 "자몽허니 블랙티": 4500, "블루베리 요거트 스무디": 5500, "생딸기 프라푸치노": 6000}

print("디저트류 ->", menu_desert)
print("음료 ->", menu_baverage)

desert = []
baverage = []

while True:
    item = input("\n장바구니에 담고 싶은 디저트 1개를 선택해주세요 : ")
    if item == "q":
        break
    else:
        desert.append(item)
        print(item, "메뉴가 장바구니에 담겼습니다.")

    item = input("\n장바구니에 담고 싶은 음료 1개를 선택해주세요 : ")
    if item == "q":
        break
    else:
        baverage.append(item)
        print(item, "메뉴가 장바구니에 담겼습니다.")

    print("="*30)

print("\n※ 장바구니에 담긴 디저트를 알려드립니다. ※")
print(desert)
print("\n※ 장바구니에 담긴 음료를 알려드립니다. ※")
print(baverage)

desert_basket = set(desert)
baverage_basket = set(baverage)
while True:
    item = input("\n장바구니에서 삭제하고 싶은 디저트 1개를 선택해주세요 : ")
    if item == "q":
        break
    else:
        desert_basket = desert_basket - set([item])
        print("\n현재 디저트 장바구니 현황입니다.")
        print(desert_basket)
    item = input("\n장바구니에서 삭제하고 싶은 음료 1개를 선택해주세요 : ")
    if item == "q":
        break
    else:
        baverage_basket = baverage_basket - set([item])
        print("\n현재 음료 장바구니 현황입니다.")
        print(baverage_basket)
print("\n※ 최종 장바구니에 담긴 내역을 알려드립니다 ※")
print("디저트 :", desert_basket, "음료 : ", baverage_basket)

print("\n===========영수증을 출력해드리겠습니다.=========")

print("주문 시각 :", datetime.now())

total_basket = desert_basket | baverage_basket
print("주문 내역:", total_basket)
total_desert = 0
total_baverage = 0
for i in desert_basket:
    total_desert += menu_desert[i]
for j in baverage_basket:
    total_baverage += menu_baverage[j]

total_money = 0
total_money = total_desert + total_baverage
print("주문하신 메뉴의 총 금액은", total_money, "원 입니다.")
print("※ 카페를 이용해주셔서 감사합니다. ※")
