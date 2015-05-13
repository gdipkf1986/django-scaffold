__author__ = 'Jovi'

import string
import random


def random_string(length=10, excludes='1lLiI0oO', source_string=(string.ascii_letters + string.digits)):
    return ''.join([source_string[x] for x in random.sample(range(0, len(source_string)-1), length) if str(source_string[x]) not in excludes])
