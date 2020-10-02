"""Brain Games functions: functions described."""


def is_Prime(num):
    if num > 1:
        # Check if the number has a multiple denominators
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        # Number is prime if it doesn't have any denominators
        else:
            return True
    # If number is less than or equal to 1, it is not prime
    else:
        return False
