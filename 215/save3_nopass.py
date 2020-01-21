import re
def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    reg = r'^PB-([^A-Za-z0-9]{8})-([^A-Za-z0-9]{8})-([^A-Za-z0-9Z]{8})-([^A-Za-z0-9]{8})$'
    if re.match(reg, key):
        return True
    else:
        return False