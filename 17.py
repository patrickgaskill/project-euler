LIMIT = 1000

def word(n):
    small_names = ["zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens_names = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]

    if n == 1000:
        return "one thousand"

    hundreds = n // 100
    tens_units = n % 100
    s = ""

    if hundreds > 0:
        s += f"{small_names[hundreds]} hundred"

        if tens_units > 0:
            s += " and "

    tens = tens_units // 10
    units = tens_units % 10

    if tens >= 2:
        s += tens_names[tens]

        if units > 0:
            s += f" {small_names[units]}"
    elif tens_units > 0:
        s += small_names[tens_units]

    return s

def word_len(n):
    return len(word(n).replace(" ", ""))

print(sum(word_len(n) for n in range(1, LIMIT + 1)))
