# 判断是否为button
def if_button(x):
    if str(type(x)) not in ["<class 'str'>"]:
        return 0
    else:
        if '_btn' in x:
            return 1
        else:
            pass
    return 0

