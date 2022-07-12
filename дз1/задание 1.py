duration = int(input())
one_minute = 60
one_house = 3600
one_day = 86400
one_week = 604800
if one_minute >= duration:
    s = duration
    print(s, 'сек')
elif one_house >= duration:
    m, s = duration // 60 % 60, duration % 60
    print(m, 'мин', s, 'сек')
elif one_day >= duration:
    h, m, s = duration // 3600 % 24, duration // 60 % 60, duration % 60
    print(h,'час', m, 'мин', s, 'сек')
else:
    d, h, m, s = duration // 86400 % 30, duration // 3600 % 24, duration // 60 % 60, duration % 60
    print(d, 'день', h, 'час', m, 'мин', s, 'сек')
