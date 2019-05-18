import json
import random

from .util import logger
from .util.generators import random_word, random_symbol


def generate_password(event, context) -> str:
    """
    AWS Lambda Function handler entrypoint. Returns a JSON.

    >>> handler({}, None)
    '{"statusCode": 200, "body": "..."}'
    """
    logger.debug(__name__)
    logger.debug(json.dumps(event, indent=4))

    try:
        words = random_word(2)
        symbols = random_symbol(2)
        password = f'{words[0].capitalize()}{words[1].capitalize()}'
        password += f'{random.randint(0, 9)}{random.randint(0, 9)}'
        password += f'{symbols}'
    except Exception:
        logger.exception("Exception Raised Generating a Password")
        raise
    finally:
        words = None
        symbols = None

    return json.dumps({'statusCode': 200, 'body': {'password': password}}, indent=4)
