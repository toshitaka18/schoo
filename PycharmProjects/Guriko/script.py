import utils
import random

point = 0
computer_point = 0

player_name = input('名前を入力してください')
while point < 10 and computer_point < 10:
    print('-------------------------------------------------')
    print('グリコをはじめます。10ポイント先取で勝利！')
    print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
    player_hand = int(input('数字で入力してください：'))



    if utils.validate(player_hand):
        computer_hand = random.randint(0, 2)

        if player_name == '':
            utils.print_hand(player_hand)
        else:
            utils.print_hand(player_hand, player_name)

        utils.print_hand(computer_hand, 'コンピューター')

        result = utils.judge(player_hand, computer_hand)
        print('結果は' + result + 'でした')
        if result == '勝ち':
            if player_hand == 0:
                point += 3
                print('グリコ！')
            elif player_hand == 1:
                point += 6
                print('チヨコレイト！')
            else:
                point += 6
                print('パイナツプル！')
        elif result == '負け':
            if computer_hand == 0:
                computer_point += 3
            else:
                computer_point += 6
        print('現在の' + player_name + 'のポイントは' + str(point) + ' コンピュータのポイントは' + str(computer_point))

    else:
        print('正しい数値を入力してください')

if point >= 10:
    print(player_name +'の勝利！お疲れさまでした。')
else:
    print('コンピュータの勝利。。残念でした。')