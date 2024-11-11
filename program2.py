import re

def decode_message(message, pattern):
        
# write your code here
    regex_pattern = "^" + pattern.replace("?", ".").replace("*", ".*") + "$"
    return bool(re.match(regex_pattern, message))