from django import template

register = template.Library()

mydict = {
    'Farvardin': 'فروردین',
    'Ordibehesht': 'اردیبهشت',
    'Khordad': 'خرداد',
    'Tir': 'تیر',
    'Mordad': 'مرداد',
    'Shahrivar': 'شهریور',
    'Mehr': 'مهر',
    'Aban': 'آبان',
    'Azar': 'آذر',
    'Dey': 'دی',
    'Bahman': 'بهمن',
    'Esfand': 'اسفند',
    'Monday': 'شنبه',
    'Sunday': 'یکشنبه',
    'Tuesday': 'دوشنبه',
    'Wednesday': 'سه شنبه',
    'Thursday': 'چهارشنبه',
    'Friday': 'پنجشنبه',
    'Saturday': 'جمعه',
}

@register.filter
def e2p(value:str):
    """Turns English names to persian names"""

    new_list = []
    value = value.split()
    for word in value:
        if word in mydict:
            new_list.append(mydict[word])
        else:
            new_list.append(word)
    new_str = ' '.join(new_list)
    return new_str