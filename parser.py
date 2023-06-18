# dictionary of accepted things
OPERATORS = ["==", "!=",
             ">", ">=",
             "<", "<="]
VAR_LETTERS = "pqrst"
FIRST_LIST = {
    "statement": ["if"],
    "condition" : ["p", "q", "r", "s", "t"],
    "variabel" : ["p", "q", "r", "s", "t"],
    "operator" : ["==", "!=", ">", ">=", "<", "<="],
    "aksi"     : ["pass"]
}

# (variable, is_terminal)
STACK = []

def parse(words):
    # Initialization routine
    STACK.clear()
    STACK.append(("#", 1))
    STACK.append(("statement", 0))
    grammar_correct = True
    ptr = 0
    symbol = ""

    stack_top, terminal = STACK[-1]
    while stack_top != "#" and ptr < len(words) and grammar_correct:
        symbol = words[ptr]
        if not(terminal):
            if stack_top == "statement" and symbol == "if":
                STACK.pop()
                STACK.append(("aksi", 0))
                STACK.append((":", 1))
                STACK.append(("condition", 0))
                STACK.append(("if", 1))
            elif stack_top == "condition" and symbol in VAR_LETTERS:
                STACK.pop()
                STACK.append(("variabel", 0))
                STACK.append(("operator", 0))
                STACK.append(("variabel", 0))
            elif stack_top == "variabel":
                if symbol[-1] == ":":
                    symbol = symbol[:-1]

                if symbol[:-1] in VAR_LETTERS:
                    STACK.pop()
                    STACK.append((symbol, 1))
            elif stack_top == "operator" and symbol in OPERATORS:
                STACK.pop()
                STACK.append((symbol, 1))
            elif stack_top == "aksi" and symbol == "pass":
                STACK.pop()
                STACK.append(("pass", 1))
            else:
                grammar_correct = False
        else:
            if stack_top == "if":
                STACK.pop()
                ptr += 1
            elif stack_top in VAR_LETTERS:
                STACK.pop()
                if symbol[-1] == ":":
                    STACK.pop()
                ptr += 1
            elif stack_top in OPERATORS:
                STACK.pop()
                ptr += 1
            elif stack_top == "pass":
                STACK.pop()
                ptr += 1
            elif stack_top == ":":
                STACK.pop()
                ptr += 1
            else:
                grammar_correct = False

        stack_top, terminal = STACK[-1]

    grammar_correct = False if STACK != [("#", 1)] else True
    if not(grammar_correct):
        print("Something is wrong with the grammar of your input!")
        print(f"expected: {' | '.join(FIRST_LIST[STACK[-1][0]])}, get: {words[ptr]}")
    else:
        print("All clear! No problem detected")
