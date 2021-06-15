import re


class PrimeIterator:
    """
    An iterator class that iterates from 1 to a number "n". It stops the iteration with the StopIteration exception when it gets to a number greater than "n".

    To Use:
    >>> nums = PrimeIterator(10)
    >>> next(nums)
    2
    >>> next(nums)
    3
    >>> next(nums)
    5
    >>> next(nums)
    7
    """

    def __init__(self, n=0):
        self.n = n

        # Initialize the iter() method when the object is created.
        iter(self)

    def __iter__(self):
        self.prime = 2
        return self

    def __next__(self):
        """ To return the next number """
        num = self.inter
        while True:
            is_prime = self._isprime(num)

            # If "num" is prime, return num and change current iter variable.
            if is_prime:
                if num <= self.n:
                    self.prime = num + 1
                    return num

                # If the current prime number is greater than "n", then raise an exception
                else:
                    raise StopIteration

            # If "num" is not prime, increase num by one and repeat
            else:
                num += 1

    def _isprime(self, num):
        ''' A function that uses regular expression to check if a number is prime '''
        return re.compile(r'^1?$|^(11+)\1+$').match('1' * num) is None


# Generator for prime numbers
def prime_generator(n):
    """ generates prime numbers from `1` to a number `n`,
    where `n` is greater than 1 """

    for num in range(2, n):

        # Using regular expression check if num is prime.
        if re.compile(r'^1?$|^(11+)\1+$').match('1' * num) is None:
            yield num
