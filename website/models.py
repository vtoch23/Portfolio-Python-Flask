import numpy as np
import numpy_financial as npf


class InvalidInput(Exception):
    pass


def wordlist():
    words = []

    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())

    return words


def filter_forbidden(string: str):
    new_string = "".join([character for character in string if character.isalpha()])
    return new_string


class LotteryNumbers:
    def __init__(self, nums):
        self.list = nums

    def number_of_hits(self, numbers: list):
        try:
            print(f"number of hits: {len([number for number in numbers if number in self.list])}")
            return len([number for number in numbers if number in self.list])
        except InvalidInput as e:
            return f'error number of hits", {e}'
  
    def hits_in_place(self, numbers: list):
        try:
            print(f"matched numbers: {[number for number in numbers if number in self.list]}")
            return [number for number in numbers if number in self.list]
        except InvalidInput as e:
            return f'error hits in place", {e}'


def generate_strong_password(a=True, b=True, c=True):
    from random import choice
    import string
    list = ["!", "?", "=", "+", "-", "(", ")", "#"]
    str = ""
    for i in range(len(list)):
        char = list[i]
        str += char
    digits = string.digits
    letters = string.ascii_lowercase
    alphabet1 = letters
    alphabet2 = digits + letters
    alphabet3 = digits + str + letters
    alphabet4 = letters + str
    password = ''
    try:
        for i in range(int(a)):
            if b is False and c is False:
                password += choice(alphabet1)
            elif b is True and c is False:
                password += choice(alphabet2)
            elif c is True and b is False:
                password += choice(alphabet4)
            else:
                password += choice(alphabet3)
    except InvalidInput as e:
        return f'Invalid input", {e}'
    return password


class Investment:

    def __init__(self, price: int, deposit: int, term: int, fixed: int, rate: float):
        self.price = price
        self.deposit = deposit
        self.term = term
        self.fixed = fixed
        self.rate = rate

    def calc_deposit(self):
        try:
            deposit_amount = (self.deposit/self.price)*100
            print(f"the deposit amount submitted is: {deposit_amount}")
            return int(deposit_amount)
        except Exception as er:
            return (f"error while calculating deposit {er.args}")

    def mortgage_calc(self):
        try:
            mortgage = self.price-self.deposit
            return int(mortgage)
        except Exception as er:
            print("error while calculating mortgage" + er.args)

    def monthly(self):
        try:
            mortgage = self.mortgage_calc()
            months = self.term*12

            payment = (self.rate/12) * (1/(1-(1+self.rate/12)**(-months)))*mortgage
            return abs(round(payment, 2))
        except:
            print("error while calculating payment")

    def salary(self):
        try:
            salary = self.mortgage_calc() / 4.75
            return int(salary)
        except:
            print("error while calculating salary")

    def new_price(self, price, increase, fix):
        try:
            if fix > 0:
                price =  self.new_price(price+price*increase/100, increase, fix-1)

            return int(price)
        except:
            print("error while calculating new price")

    def balance(self):
        principal = self.mortgage_calc()
        per = np.arange(self.fixed*12) + 1
        ipmt = npf.ipmt(self.rate/12, per, self.term*12, principal)
        ppmt = npf.ppmt(self.rate/12, per, self.term*12, principal)
        pmt = npf.pmt(self.rate/12, self.term*12, principal)
        np.allclose(ipmt + ppmt, pmt)
        fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}'
        for payment in per:
            index = payment - 1
            principal = principal + ppmt[index]
        return round(principal, 2)


def is_it_valid(pic: str):
    list23 = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if len(pic) == 11:
        birthday = pic[0:6]
        day = birthday[0:2]
        day = int(day)
        month = birthday[2:4]
        month = int(month)
        year = birthday[4:]
        century = pic[6]
        personal_id = pic[7:10]
        control = pic[10]
        result23 = birthday + personal_id
        result = int(result23)/31
        result = str(result)
        dot = result.find(".")
        left = result[0:dot]
        left = "0"
        parts2 = left+result[dot:]
        number = float(parts2)
        identifier = round(number*31)
        if check_day(day, month, year, century) and check_month(month) and check_century(century) and check_control(list23, control, identifier):
            return True
        else:
            return False
    else:
        return False


def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    return False


def check_day(day, month, year, century):
    months31 = [1, 0o1, 3, 0o3, 5, 0o5, 7, 0o7, 8, 10, 12]
    months30 = [4, 0o4, 6, 0o6, 9, 11]

    if century == "-":
        year = "19"+year
    elif century == "+":
        year = "18" + year
    elif century == "A":
        year = "20"+year
    year = int(year)
    if leap_year(year) == True and month == 2:
        return day > 0 and day <= 29

    elif leap_year(year) == False and month == 2:
        if month == 2:
            return day > 0 and day <= 28
    elif month in months31 or month == 8:
        return day > 0 and day <= 31
    elif month in months30 or month == 9:
        return day > 0 and day <= 30


def check_month(month):
    return month > 0 and month <= 12


def check_century(century):
    return century == "+" or century == "-" or century == "A"


def check_control(list, control, identifier):
    control_character = list[identifier]
    return control_character == control


def check_year(year):
    return year > 0


def most_common_words(filename: str, lower_limit: int):

    with open(filename) as file:
        content = file.read()
        content = content.strip()
        content = content.replace(".", "")
        content = content.replace("\n", " ")
        words = content.split(" ")
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}

def most_common_word(filename: str):

    with open(filename) as file:
        content = file.read()
        content = content.strip()
        content = content.rstrip(".")
        content = content.replace("\n", " ")
        content = content.replace(".", " ")
        words = content.split(" ")
        for word in words:
            lower_limit = 0
            count = words.count(word)
            if count > lower_limit:
                lower_limit = count
                most_common = word

        return most_common