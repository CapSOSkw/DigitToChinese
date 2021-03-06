import re

_chineseDigit = {
    'Lower': {
        '0': '零',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九'},

    'Upper': {
        '0': '零',
        '1': '壹',
        '2': '贰',
        '3': '叁',
        '4': '肆',
        '5': '伍',
        '6': '陆',
        '7': '柒',
        '8': '捌',
        '9': '玖'
    }
}
_unit = ["", '十', '百', '千']

def reversed_enumerate(l):
    return zip(reversed(range(len(l))), reversed(l))


def converter(num: int, lower=True):
    result = ""

    if num == 0:
        return '零'

    while num >= 10:
        num_length = len(str(num))

        if num_length <= 4:
            for num_of_digit, u in reversed_enumerate(_unit):
                quotient = num // 10 ** num_of_digit
                if quotient == 0:
                    result += '零'
                else:
                    result += '{0}{1}'.format(_chineseDigit["Lower"][str(quotient)], u) if lower else '{0}{1}'.format(_chineseDigit["Upper"][str(quotient)], u)
                    num %= 10 ** num_of_digit

        elif 4 < num_length <= 8:
            ten_thousand = num // 10000
            result += converter(ten_thousand, lower=lower) + '万'
            num %= 10000
            if num < 10:
                result += '零'

        else:
            billion = num // 100000000
            result += converter(billion, lower=lower) + '亿'
            num %= 100000000
            if num < 10:
                result += '零'

    result += '{}'.format(_chineseDigit["Lower"][str(num)]) if lower else '{}'.format(_chineseDigit["Upper"][str(num)])
    result = re.sub(r'(^零+)|(零+$)', "", result)
    result = re.sub(r'零+', '零', result)

    return result


# def converter1(args):
#     result = ""
#
#     num = args['number'] or args[0]
#     lower = args['lower'] or args[1]
#
#     if num == 0:
#         return '零'
#
#     while num >= 10:
#         num_length = len(str(num))
#
#         if num_length <= 4:
#             for num_of_digit, u in reversed_enumerate(_unit):
#                 quotient = num // 10 ** num_of_digit
#                 if quotient == 0:
#                     result += '零'
#                 else:
#                     result += f'{_chineseDigit["Lower"][str(quotient)]}{u}' if lower else f'{_chineseDigit["Upper"][str(quotient)]}{u}'
#                     num %= 10 ** num_of_digit
#
#         elif 4 < num_length <= 8:
#             ten_thousand = num // 10000
#             result += converter(ten_thousand, lower=lower) + '万'
#             num %= 10000
#             if num < 10:
#                 result += '零'
#
#         else:
#             billion = num // 100000000
#             result += converter(billion, lower=lower) + '亿'
#             num %= 100000000
#             if num < 10:
#                 result += '零'
#
#     result += f'{_chineseDigit["Lower"][str(num)]}' if lower else f'{_chineseDigit["Upper"][str(num)]}'
#     result = re.sub(r'(^零+)|(零+$)', "", result)
#     result = re.sub(r'零+', '零', result)
#     print(result)
#     return result

