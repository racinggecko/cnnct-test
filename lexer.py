import re

# Token types
TOKEN_TYPES = {
    'PRINT': r'print',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'ASSIGN': r'::',
    'NEW_VAR': r'new var_[a-zA-Z_][a-zA-Z0-9_]*:',
    'NEW_FX': r'new fx [a-zA-Z_][a-zA-Z0-9_]*:',
    'CALL_FX': r'call fx [a-zA-Z_][a-zA-Z0-9_]*',
    'LBRACE': r'{',
    'RBRACE': r'}',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'STRING': r'"[^"]*"',
    'COMMENT': r'\/\/.*',
    'NEWLINE': r'\n',
    'WHITESPACE': r'\s+'
}

TOKEN_PATTERN = '|'.join(f'(?P<{token}>{pattern})' for token, pattern in TOKEN_TYPES.items())

def tokenize(code):
    tokens = []
    position = 0

    while position < len(code):
        match = re.match(TOKEN_PATTERN, code[position:])
        if match:
            token_type = match.lastgroup
            token_value = match.group()
            tokens.append((token_type, token_value))
            position += len(token_value)
        else:
            position += 1
    
    return tokens

# Example code
cnnct_code = """
new var_x: 10
new fx my_function: {
    print{"Hello, Cnnct!"}
}
call fx my_function
"""

tokens = tokenize(cnnct_code)

for token_type, token_value in tokens:
    print(f"Token type: {token_type}, Token value: {token_value}")
 
