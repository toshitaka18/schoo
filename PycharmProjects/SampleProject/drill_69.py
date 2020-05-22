def caught_speeding(speed,is_birthday):
    if is_birthday == 'True':
        speed *= 0.2
    if speed < 60:
        judge = 0
        print(str(judge) + 'チケットなし')
    elif speed >= 60 and speed <80:
        judge = 1
        print(str(judge) + '小チケット')
    else:
        judge = 2
        print(str(judge) + '大チケット')

a = int(input('速度を入力：'))
b = input('誕生日ならTrue入力、それ以外はFalseを入力')

caught_speeding(a,b)
