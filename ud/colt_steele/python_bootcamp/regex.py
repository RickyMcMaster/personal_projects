import re

def is_valid_time(input):
    pattern = re.compile(r'^\d{1,2}:\d{2}$')
    # Colt's version: (r'^\d\d?:\d\d$')
    if pattern.search(input):
        return True
    return False

# print(is_valid_time("1:45"))
# print(is_valid_time("it is 1:45"))

def parse_bytes(input):
    pattern = re.compile(r'\b[0-1]{8}\b')
    return pattern.findall(input)

# print(parse_bytes("10101011 64747474 11110000"))
# print(parse_bytes("9.45"))
# print(parse_bytes('my data is 10101010'))
# print(parse_bytes('1:23'))

def parse_date(input):
    pattern = re.compile(r'^(\d\d?)[/,\.](\d\d?)[/,\.](\d{4})$')
    match = pattern.search(input)
    if match:
        return {k:v for k, v in zip(("d", "m", "y"), match.groups())}
    # N.B. Important!!!! Needed to account for parsing errors!!!
    return None

# print(parse_date("21/07/1975"))
# print(parse_date("21/07/19"))

def censor(input):
    # pattern = re.compile(r'frack[a-z]*', re.IGNORECASE)
    # Colt's version (perhaps better to use word boundaries in case frack in middle of a word):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)

print(censor("FRACKing fracker you"))
print(censor("FRAKCing fracker you"))
print(censor("FRAKCing rfacker you"))
print(censor("frack you"))