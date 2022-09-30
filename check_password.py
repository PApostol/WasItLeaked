"""
An API call is made with the first 5 characters of SHA1 of your password(s),
which returns a list of matches and their occurrences.
The full password hash is then checked locally for matches.
More occurrences means worse password.
"""
import hashlib
import sys
from typing import List, Tuple

import requests
from requests.exceptions import RequestException


def check_password(password: str) -> Tuple[str, int]:
    """Compute hash and send API request"""
    hashed = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = hashed[:5], hashed[5:]
    url = f'https://api.pwnedpasswords.com/range/{head}'
    resp = requests.get(url)

    if resp.status_code != 200:
        raise RequestException(f'Request error encountered when accessing {url}.\nCode: {resp.status_code}')

    hashes = (line.split(':') for line in resp.text.splitlines())
    count = next((int(count) for i, count in hashes if i == tail), 0)
    return hashed, count


def main(passwords: List[str]) -> None:
    """Check comma separated password(s) against leakd password databases"""
    for password in passwords:
        try:
            hashed, count = check_password(password.strip())
        except Exception as err:
            print(f'Password {password} could not be checked: {err}')
        else:
            if count:
                print(f'Password {password} was found with {count} occurrences (hash: {hashed})')
            else:
                print(f'Password {password} was not found (hash: {hashed})')


if __name__ == '__main__':
    main(sys.argv[1:])
