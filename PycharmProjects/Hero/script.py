
from random import randint
from time import sleep
import sys

ENEMEY_INFO = [
               {
                   "name": "コイキング",
                   "status":
                   {
                       "hp":10,
                       "atk": randint(1, 3)
                   }
               },
               {
                   "name": "ピカチュウ",
                   "status":
                   {
                       "hp":100,
                       "atk": randint(3, 15)
                    }
                },
               {
                   "name": "カイリュウ",
                   "status":
                   {
                       "hp":500,
                       "atk": randint(15, 75)
                    }
                }
               ]

def set_player():
    player_hp = randint(50, 100)
    player_atk = randint(20, 50)
    player_param = player_hp, player_atk
    return player_param

def show_player(param):
    hp, atk = param
    print("HP: {0}".format(hp))
    print("ATK: {0}".format(atk))

def set_enemy():
    ene_index = randint(0, len(ENEMEY_INFO) - 1)
    enemy_info = ENEMEY_INFO[ene_index]
    ene_name = enemy_info["name"]
    ene_hp = enemy_info["status"]["hp"]
    ene_atk = enemy_info["status"]["atk"]
    enemy_param = ene_name, ene_hp, ene_atk
    return enemy_param

def calc_dmg(atk,from_who, to_who):
    total_atk = atk
    print("{0}:{1}に{2}のダメージを与えた!".format(from_who, to_who, total_atk))
    return total_atk

def judge(player_hp, enemy_hp):
    if player_hp < 0:
        ply_win_flag = False
    elif enemy_hp < 0:
        ply_win_flag = True
    return ply_win_flag


if __name__ == "__main__":
    print("ようこそポケモンの世界へ")
    start_flag  = int(input("冒険を始めますか?:[1:始める/0:やめる]:"))
    if start_flag != 1:
        sys.exit()
    else:
        while True:
            # プレイヤー情報生成
            player_info = set_player()
            # プレイヤー情報取得
            ply_hp = player_info[0]
            ply_atk = player_info[1]

            # 敵情報生成
            enemy_info = set_enemy()
            # 敵情報の取得
            ene_name = enemy_info[0]
            ene_hp = enemy_info[1]
            ene_atk = enemy_info[2]

            select_mode = int(input("[1:冒険に出かける/2:自分の状態を知る/0:休息を取る]:"))
            if select_mode == 0:
                exit()
            if select_mode == 2:
                show_player(player_info)
            else:
                # 攻撃の順番
                atk_index = 0
                for i in range(randint(1, 5)):
                    print(".")
                    sleep(1)
                print("{0}があらわれた!".format(ene_name))
                # 戦闘開始
                while ply_hp > 0 and ene_hp > 0:
                    if atk_index % 2 == 0:
                        total_atk = calc_dmg(ply_atk, "主人公のポケモン", ene_name)
                        ene_hp -= total_atk
                    else:
                        total_atk = calc_dmg(ene_atk, ene_name, "主人公のポケモン")
                        ply_hp -= total_atk
                    atk_index += 1
                    # 1秒待って戦闘ログを出力
                    sleep(1)

                player_win_flag = judge(ply_hp, ene_hp)
                # ゲーム判定
                if player_win_flag:
                    print("{0}を倒した！おめでとう!経験値を得た！".format(ene_name))
                else:
                    print("主人公のポケモンは倒れた、、目の前が真っ暗になった、、")