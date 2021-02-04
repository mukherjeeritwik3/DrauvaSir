# Creating dictonaires to check if we can execute funtions from key value pair
def dict(s):
    a = {
            'what month it is': 'january',
            'what month is it': 'january',
            'which month it is': 'january',
            'which month is it': 'january',
            'month now': 'january',
            'current month': 'january',
            'can you print': float(53)


    }
    if (s in a):
        return ("yes")
    else:
        return ("invalid")

print(dict("can you prindt"))