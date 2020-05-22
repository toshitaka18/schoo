#fizzbuzz問題を再現、正しいくつまでカウントするか引数で指定

def fizzbuzz(max_num):
    for i in range(1,max_num ):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

max_num = int(input('数値を入力してください'))
print(fizzbuzz(max_num))
