def in1to10(num,outside_mode):
    if num >=1 and num <=10:
        return True
    elif outside_mode == 'true':
        if num < 0 or num >= 11:
            return True
        else:
            return False


print(in1to10(90,'false'))
