
import json
def decode(data, default={}):
    try:
    	return json.loads(data)
    except ValueError:
    	return default
    
foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
# >>>
# Foo: {'stuff': 5, 'meep': 1}
# Bar: {'stuff': 5, 'meep': 1}
assert foo is bar

def decode(data, default=None):
    """Load JSON data from a string.
    Args:
        data: JSON data to decode
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default
foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
# >>>
# Foo: {'stuff': 5}
# Bar: {'meep': 1}
assert foo is not bar

from datetime import datetime
from typing import Optional
def log_typed(message: str,
              when: Optional[str]=None) -> None:
    """Log a message with a timestamp.
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now().isoformat()
    print(f'{when}: {message}')