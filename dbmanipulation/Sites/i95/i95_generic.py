


def fix_MM(mm):
    retmm = ''
    try:
        remains = str(mm).split('.')[1]
    except IndexError:
        return mm 
    if len(remains) == 1: remains = remains + '0'
    if len(remains) == 3: remains = remains[:2]
    if int(remains) <= 19:
        retmm = int(mm)
    elif int(remains) <= 39:
        retmm = int(mm) + 0.2
    elif int(remains) <= 59:
        retmm = int(mm) + 0.4
    elif int(remains) <= 79:
        retmm = int(mm) + 0.6
    elif int(remains) <= 99:
        retmm = int(mm) + 0.8
    return retmm
    
    
if __name__ == '__main__':
    fix_MM(157)