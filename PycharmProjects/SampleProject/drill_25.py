input = [3,5,9,12,15,21,29,35,42,51,62,78,81,92,93]
print(str(input.index(9) + 1) + '番目にあります')

def search (num_free):
    for i,n in enumerate(input):
        if n == num_free:
            print(str(i + 1)+'番目にあります。')
            return
    else:
        print('その数は含まれていません')

search(9)