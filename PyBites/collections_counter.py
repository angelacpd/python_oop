# Using Python's collections.Counter to see how unique
# a random string generator really is

import random
import string

from collections import Counter


def get_random_string():
    return ''.join(random.sample(string.ascii_lowercase + string.digits, 6))


print(Counter(get_random_string() for _ in range(1000000)).most_common(5))
    
