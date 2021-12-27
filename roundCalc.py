
def roundUpMul(a , b):
    ''' Get Round Up'''
    return GetRoundNum(a * b, 1)

def roundDownMul(a , b):
    ''' Get Round Down'''
    return GetRoundNum(a * b, 0)

def roundMax(a , b):
    ''' Get Round Up of Max'''
    if GetRoundNum(a, 1) > GetRoundNum(b, 1) :
        return GetRoundNum(a, 1)
    else :
        return GetRoundNum(b, 1)

def GetRoundNum(a , i):
    ''' Get Round Up Or Down According to i
    if i == 1 then Round Up
    if i == 0 then Round Down
    else return -1 (error)
    '''
    if i != 0 and i != 1 :
        return -1
    return (((a // 10) + i) * 10)

