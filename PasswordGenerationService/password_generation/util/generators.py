import random

from boto3.dynamodb.conditions import Key
from typing import List
from .service_objects import ddb_table_word_dict


def random_symbol(num: int = 2, seed: object = None) -> str:
    """
    Return a string of random symbols from the following list. Duplicate c

    ['!', '@', '#', '$', '%', '^', '&, '*' ,'(', ')', '-', '_', '=', '+', '`', '~]
    """
    symbols = '~`!@#$%^&*()_-+='
    random.seed(a=seed)
    result = ''
    while num > 0:
        result += symbols[random.randint(0, len(symbols) - 1)]
        num += -1
    return result


def random_word(num: int, seed: object = None) -> List[str]:
    """
    Return a list of random words.
    """
    random.seed(a=seed)
    results = []

    while len(results) < num:
        record = random.randint(0, ddb_table_word_dict.item_count)
        response = ddb_table_word_dict.scan(
            FilterExpression=Key("random_sort").eq(record),
            ProjectionExpression="word",
        )
        results.extend([word["word"] for word in response["Items"]])

    return results
