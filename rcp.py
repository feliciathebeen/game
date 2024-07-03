import random

hand_shapes = ['가위', '바위', '보']
computer_pick = random.choice(hand_shapes)
# print(computer_pick)

draws = 0
wins = 0
loses = 0
# random_shapes = random.randint()
# print(random_shapes)

while True:
    try:
        player_pick = input(f"{hand_shapes} 중 하나를 선택해주세요! :")

        if player_pick not in hand_shapes:
            print("정확히 입력해 주세요.")
            continue

        if player_pick == computer_pick:
            draws += 1
            print("비겼습니다.")


        elif (computer_pick == '바위' and player_pick == '가위') or (computer_pick == '가위' and player_pick == '보') or (computer_pick == '보' and player_pick == '바위'):
            loses += 1
            print("졌습니다.")
            print(f"player_pick: {player_pick}, computer_pick: {computer_pick}")
        else:
            wins += 1
            print("이겼습니다.")
            print(f"player_pick: {player_pick}, computer_pick: {computer_pick}")
            play_again = input('한 판 더? (Y/N): ')
            if play_again.upper() == 'Y':
                print("게임을 다시 시작합니다.")
                continue
            else:
                print(f"{wins}승 {draws}무 {loses}패")
                break



    except ValueError:
        print("문자를 다시 확인해 주세요")
