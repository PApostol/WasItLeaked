# Was It Leaked - Password Checker
Check if your passwords are listed in leaked password databases.

#### How does it work?
An API call is made with the first 5 characters of SHA1 of your password(s), which returns a list of matches and their occurrences. The full password hash is then checked locally for matches. More occurrences means worse password.

#### Requirements:
- [Python 3.7+](https://www.python.org/downloads/)
- [requests](https://pypi.org/project/requests/)

#### Example
Usage:

`python check_password.py password1 abcd1234567890 alDjf?f0`

Output:

```
Password "password1" was found with 2413945 occurrences (hash: E38AD214943DAAD1D64C102FAEC29DE4AFE9DA3D)
Password "abcd1234567890" was found with 354 occurrences (hash: AE33FB6D42AD13F6AAC090EF70818BB3B0E28B70)
Password "alDjf?f0" was not found (hash: C0A9C84FFB66D385883B2D2311288DD67EEAFE0E)
```
#### Can I check emails and phones as well?
You can manually check for a leaked email or phone [here](https://haveibeenpwned.com/). However, for an automated API call to check emails, you'll need to pay for an [API key](https://haveibeenpwned.com/API/v3#Authorisation).