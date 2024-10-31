def create_token_array(text: str) -> list:
    return list(text)

def remove_comments(tokens: list) -> list:
    level = 0
    new_array = []
    for token in tokens:
        if token == "(":
            level += 1
            continue

        if token == ")":
            level -= 1
            # Avoid issue where statements like '1(comment)2' evalulate to '12'
            new_array.append(" ")
            continue
        
        if level == 0:
            new_array.append(token)
    
    return new_array

def convert_string_literals(tokens: list) -> list:
    in_string = False
    current_string = ""
    out = []

    for token in tokens:
        if token == "\"":
            if in_string:
                out.append((current_string.replace("\\n", "\n"), True))
                current_string = ""
                in_string = False
            else:
                in_string = True
            continue
        
        if in_string:
            current_string += token
        else:
            out.append(token)
    
    return out

def _merge_with_letters(tokens: list, symbol) -> list:
    was_symbol = False
    new_list = []
    for token in tokens:
        if type(token) is not str:
            new_list.append(token)
            continue
        
        if token == symbol:
            new_list.append(token)
            was_symbol = True
        else:
            if was_symbol and not token.isdigit():
                new_list[-1] += token
            else:
                new_list.append(token)
            was_symbol = False
    
    return new_list

def merge_dots_with_letters(tokens: list) -> list:
    return _merge_with_letters(tokens, ".")

def merge_dollar_signs_with_letters(tokens: list) -> list:
    return _merge_with_letters(tokens, "$")

def merge_digits(tokens: list) -> list:
    tmp_list = [""]

    in_number = False
    exists_decimal_point = False
    for c in tokens:
        if type(c) is tuple:
            tmp_list.append(c)
            continue
        
        if c in "0123456789.":
            if in_number:
                if c == "." and exists_decimal_point:
                    raise SyntaxError
                
                if c == ".":
                    exists_decimal_point = True
                
                tmp_list[-1] += c
            else:
                in_number = True
                if c == ".":
                    raise SyntaxError
                
                tmp_list.append(c)
        else:
            exists_decimal_point = False
            in_number = False
            tmp_list.append(c)
    
    return tmp_list

def remove_separators(tokens: list) -> list:
    return list(filter(lambda a: a not in ("", " ", ",", "\n", "\t"), tokens))

def convert_numbers(tokens: list) -> list:
    tmp_list = []

    for token in tokens:
        try:
            float(token)
        except:
            tmp_list.append(token)
        else:
            if float(token) == int(float(token)):
                tmp_list.append(int(token))
            else:
                tmp_list.append(float(token))
    
    return tmp_list

def _create_subarrays_with_none(tokens: list) -> list:
    pairs = []

    to_be_closed = []
    for i, token in enumerate(tokens):
        if token == "[":
            to_be_closed.append(i)

        if token == "]":
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

def process(text: str) -> list:
    tokens = create_token_array(text)
    tokens = remove_comments(tokens)
    tokens = convert_string_literals(tokens)
    tokens = merge_dots_with_letters(tokens)
    tokens = merge_dollar_signs_with_letters(tokens)
    tokens = merge_digits(tokens)
    tokens = remove_separators(tokens)
    tokens = convert_numbers(tokens)
    tokens = create_subarrays(tokens)

    return tokens
