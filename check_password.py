import sys, hashlib, requests


def check_password(password):
    hashed = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = hashed[:5], hashed[5:]
    url = 'https://api.pwnedpasswords.com/range/' + head
    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise Exception('Request error encountered when accessing "{0}".\nCode: {1}'.format(url, resp.status_code))

    hashes = (line.split(':') for line in resp.text.splitlines())
    count = next((int(count) for i, count in hashes if i == tail), 0)
    return hashed, count


def main(args):
    for password in args:
        password = password.strip()
        try:
            hashed, count = check_password(password)
        except Exception as err:
            print('Password "{0}" could not be checked: {1}'.format(password, err))
        else:
            if count:
                print('Password "{0}" was found with {1} occurrences (hash: {2})'.format(password, count, hashed))
            else:
                print('Password "{0}" was not found (hash: {1})'.format(password, hashed))


if __name__ == '__main__':
    main(sys.argv[1:])
