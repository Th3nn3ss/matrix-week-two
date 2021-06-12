def get_month_decorator(func):
    """ checks that number being passed as month argument is valid. i.e betweeen 1 - 12"""
    def inner(month):
        if month >= 1 and month <= 12:
            return func(month)
        else:
            raise "whoops. Invalid month"
    return inner


# calling the decorator unto the function
@get_month_decorator
def get_month(month):
    """ returns the expected month string based on the valid month integer passed as an argument """
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September", 10: "October", 11: "Novermber", 12: "December"}

    return months[month]
