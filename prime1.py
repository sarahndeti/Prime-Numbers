__author__ = 'Sarah'
import math

class Prime_Numbers(object):

    def prime_numbers(self, n):

        if isinstance(n, str):
            return "Not an integer!!"

        if n < 0:
            return "Input is less than zero"

        number=0
        divider=2
        prime_list = []
        while divider!=n:

            prime_number=True;

            for i in range(2, int(math.sqrt(divider)+1)):
                if divider%i==0:
                    prime_number=False;
                    break;

            if (prime_number):
                number+=1
                prime_list.append(divider)
            divider+=1

        return prime_list
