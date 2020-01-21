import string
import secrets
alphabet = string.ascii_letters + string.digits
def gen_key(parts=4, chars_per_part=8):
    joiner = "-"
    key = ""
    for part in range(parts):
        subKey = ''.join(secrets.choice(alphabet) for i in range(chars_per_part))
        key = key + subKey + joiner