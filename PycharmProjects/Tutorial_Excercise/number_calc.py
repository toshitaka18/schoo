a=int(input("整数を入力："))
b=int(input("整数を入力："))
if a < b:
    print('aに小さい値を入力してください')
else:
    #最大公約数
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    print(gcd(a,b))

     #最小公倍数
    def lcm(a,b):
      return a*b//gcd(a,b)
    print(lcm(a,b))