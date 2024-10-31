STR_T = 0
INT_T = 1
FLOAT_T = 2
IDENTIFIER_T = 3

from pprint import pprint

def atomize(text: str) -> list[str]:
    return list(text)

def collect_strings(tokens: list[str]):

    in_str = False
    current_str = ""
    out = []

    for token in tokens:

        if token == '"':
            if in_str:
                out.append((current_str, STR_T))
                current_str = ""
                in_str = False
            
            else:
                in_str = True
            
        else:
            if in_str:
                current_str += token
            
            else:
                out.append(token)
    
    return out

def collect_keywords(tokens):
    out = []
    current_str = ""
    was_in_identifier = False

    for token in tokens:
        if type(token) is not str:
            out.append(token)
            continue
        
        if token.isidentifier():
            current_str += token
            was_in_identifier = True
        
        else:
            if was_in_identifier:
                out.append((current_str, IDENTIFIER_T))
                current_str = ""
                was_in_identifier = False
            
            out.append(token)
        
    return out

def clean_up_whitespace(tokens):
    out = []

    for token in tokens:
        if token in ("\n", " ", "\t"):
            continue

        out.append(token)
    
    return out

def _create_subarrays_with_none(tokens: list) -> list:
    pairs = []

    to_be_closed = []
    for i, token in enumerate(tokens):
        if token == "(":
            to_be_closed.append(i)

        if token == ")":
            pairs.append((to_be_closed.pop(), i))

    for left, right in pairs:
        # Insert None to preserve indexing throughout the loop.
        tokens = tokens[:left] + [tokens[left + 1: right]] + [None for _ in range(left, right)] + tokens[right + 1:]
    return tokens

def _remove_none(tokens: list) -> list:
    tmp_list = []

    for token in tokens:
        if token is not None:
            if type(token) is list:
                tmp_list.append(_remove_none(token))
            else:
                tmp_list.append(token)
    
    return tmp_list

def create_subarrays(tokens: list) -> list:
    tokens = _create_subarrays_with_none(tokens)
    tokens = _remove_none(tokens)
    return tokens
            

def process(text):
    buf = atomize(text)
    buf = collect_strings(buf)
    buf = collect_keywords(buf)
    buf = clean_up_whitespace(buf)
    buf = create_subarrays(buf)

    return buf

with open("main.bruh", "r") as file:
    text = file.read()

buf = process(text)
pprint(buf)