def english():
    first_number = int(input("please enter your desired number\n"))
    second_number = int(input("please enter your second number\n"))
    count = input("Please enter the operation you want to perform on the numbers? You can use words such as: multiplication, division, caret, addition, subtraction, out of part, remainder and exponent! Preferably use English words, for example: addition or subtraction!\n".lower().strip())
    if count == "multiplication":
        answer = first_number * second_number
        return answer
    else:
        pass
    if count == "division":
        answer1 = first_number / second_number
        return answer1
    else:
        pass
    if count == "caret":
        answer2 = first_number ** second_number
        return answer2
    else:
        pass
    if count == "addition":
        answer3 = first_number + second_number
        return answer3
    else:
        pass
    if count == "subtraction":
        answer4 = first_number - second_number
        return answer4
    else:
        pass
    if count == "remainder":
        answer5 = first_number % second_number
        return answer5
    else:
        pass
    if count == "out of part":
        answer6 = first_number // second_number
        return answer6
    else:
        pass
def persian():
    adad_aval = int(input("لطفاً عدد مورد نظرتان را وارد کنید\n"))
    adad_dovom = int(input("لطفاً عدد دوم خود را وارد کنید؟\n"))
    hesab = input("لطفاً عملیاتی که میخواهید روی عددها انجام شود وارد کنید؟ میتوانید از کلماتی به نامهای: ضرب، تقسیم، جمع، تفریق، خارج قسمت، باقیمانده و توان استفاده کنید! ترجیحاً از کلمات فارسی استفاده کنید برای مثال: جمع یا تفریق!\n".strip())
    if hesab == "ضرب":
        javab = adad_aval * adad_dovom
        return javab
    else:
        pass
    if hesab == "تقسیم":
        javab1 = adad_aval / adad_dovom
        return javab1
    else:
        pass
    if hesab == "توان":
        javab2 = adad_aval ** adad_dovom
        return javab2
    else:
        pass
    if hesab == "جمع":
        javab3 = adad_aval + adad_dovom
        return javab3
    else:
        pass
    if hesab == "تفریق":
        javab4 = adad_aval - adad_dovom
        return javab4
    else:
        pass
    if hesab == "باقیمانده":
        javab5 = adad_aval % adad_dovom
        return javab5
    else:
        pass
    if hesab == "خارج قسمت":
        javab6 = adad_aval // adad_dovom
        return javab6
    else:
        pass
def language_selecter(english, persian):
    language = input("please select a language between english and persian, type en or english for english, pe or persian for persian\n")
    if language.lower().strip() == "en" or language.lower().strip() == "english":
        return english()
    elif language.lower().strip() == "pe" or language.lower().strip() == "persian":
        return persian()
    else:
        return "invalid language, please restart the program again"
        return "زبان نامعتبر، لطفاً برنامه را دوباره اجرا کنید"
calculater = language_selecter(english, persian)
print(calculater)